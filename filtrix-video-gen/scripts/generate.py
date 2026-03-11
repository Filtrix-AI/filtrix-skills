#!/usr/bin/env python3
"""
Filtrix MCP video generator.

Submits `generate_video_text` and optionally polls `get_video_status`
until completion, then downloads the video.
"""

import argparse
import json
import sys
import time
import uuid

from mcp_client import (
    McpClient,
    build_output_path,
    download_binary,
    extract_error_message,
    extract_request_id,
    extract_status,
    extract_video_url,
    get_mcp_env,
    is_failure_status,
    is_success_status,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate videos via Filtrix MCP")
    parser.add_argument("--prompt", required=True, help="Video generation prompt")
    parser.add_argument("--aspect-ratio", default="16:9", help="Aspect ratio, e.g. 16:9, 9:16, 1:1")
    parser.add_argument("--idempotency-key", default=None, help="Optional idempotency key")
    parser.add_argument("--wait", action="store_true", help="Poll until a terminal status and download output")
    parser.add_argument("--poll-interval", type=int, default=8, help="Polling interval in seconds")
    parser.add_argument("--timeout", type=int, default=600, help="Polling timeout in seconds")
    parser.add_argument("--output", default=None, help="Output video path used when downloading")
    parser.add_argument("--print-json", action="store_true", help="Print raw tool payloads")
    args = parser.parse_args()

    request_key = args.idempotency_key or f"vid-{uuid.uuid4().hex}"

    try:
        endpoint, api_key = get_mcp_env()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    client = McpClient(endpoint=endpoint, api_key=api_key)

    try:
        client.initialize()
        submit_payload = client.call_tool(
            "generate_video_text",
            {
                "prompt": args.prompt,
                "aspect_ratio": args.aspect_ratio,
                "idempotency_key": request_key,
            },
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.print_json:
        print(json.dumps(submit_payload, ensure_ascii=False, indent=2))

    if submit_payload.get("ok") is not True:
        print(f"ERROR: generation failed: {json.dumps(submit_payload, ensure_ascii=False)}", file=sys.stderr)
        sys.exit(1)

    request_id = extract_request_id(submit_payload)
    if not request_id:
        print(f"ERROR: missing request_id in response: {json.dumps(submit_payload, ensure_ascii=False)}", file=sys.stderr)
        sys.exit(1)

    print(
        f"ACCEPTED: request_id={request_id} "
        f"idempotency_key={request_key} aspect_ratio={args.aspect_ratio}"
    )

    if not args.wait:
        print(f"Use: python scripts/status.py --request-id {request_id}")
        return

    poll_interval = max(1, args.poll_interval)
    timeout = max(1, args.timeout)
    started = time.monotonic()
    last_status: str | None = None

    while True:
        try:
            status_payload = client.call_tool("get_video_status", {"request_id": request_id})
        except RuntimeError as exc:
            print(f"ERROR: status polling failed: {exc}", file=sys.stderr)
            sys.exit(1)

        if args.print_json:
            print(json.dumps(status_payload, ensure_ascii=False, indent=2))

        status_text = extract_status(status_payload) or "unknown"
        if status_text != last_status:
            print(f"STATUS: {status_text}")
            last_status = status_text

        if is_success_status(status_text):
            video_url = extract_video_url(status_payload) or extract_video_url(submit_payload)
            if not video_url:
                print("OK: completed but no video_url was returned yet.")
                if not args.print_json:
                    print(json.dumps(status_payload, ensure_ascii=False))
                return

            try:
                video_bytes = download_binary(video_url)
            except RuntimeError as exc:
                print(f"ERROR: {exc}", file=sys.stderr)
                sys.exit(1)

            out_path = build_output_path(video_url, args.output, request_id=request_id)
            out_path.write_bytes(video_bytes)
            print(f"OK: {out_path} ({len(video_bytes)} bytes)")
            print(f"request_id={request_id} video_url={video_url}")
            return

        if is_failure_status(status_text):
            message = extract_error_message(status_payload) or "Video generation failed."
            print(
                f"ERROR: request_id={request_id} status={status_text} message={message}",
                file=sys.stderr,
            )
            if not args.print_json:
                print(json.dumps(status_payload, ensure_ascii=False), file=sys.stderr)
            sys.exit(1)

        if time.monotonic() - started >= timeout:
            print(f"ERROR: timed out after {timeout}s waiting for request_id={request_id}", file=sys.stderr)
            sys.exit(1)

        time.sleep(poll_interval)


if __name__ == "__main__":
    main()
