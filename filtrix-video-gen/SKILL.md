---
name: filtrix-video-gen
description: Generate videos through Filtrix Remote MCP. Use when users ask for text-to-video generation, video task polling, or downloading completed videos with generate_video_text and get_video_status.
---

# Filtrix Video Gen (MCP)

This skill is MCP-only.

- Endpoint: `https://mcp.filtrix.ai/mcp`
- Auth: `Authorization: Bearer <FILTRIX_MCP_API_KEY>`
- Primary tools:
  - `generate_video_text`
  - `get_video_status`

## Setup

Required:
- `FILTRIX_MCP_API_KEY`

Optional:
- `FILTRIX_MCP_URL` (default: `https://mcp.filtrix.ai/mcp`)

## Generate Video

```bash
python scripts/generate.py \
  --prompt "a cinematic drone shot over a neon city at night" \
  [--aspect-ratio 16:9] \
  [--idempotency-key KEY] \
  [--wait] \
  [--poll-interval 8] \
  [--timeout 600] \
  [--output /tmp/video.mp4]
```

Default behavior submits a request and prints `request_id`.
Add `--wait` to poll until completion and download the final video.

## Check Status

```bash
python scripts/status.py \
  --request-id YOUR_REQUEST_ID \
  [--download] \
  [--output /tmp/video.mp4]
```

## Idempotency

`idempotency_key` prevents duplicate billing on retries.
If omitted, scripts auto-generate one UUID-based key.

## References

- [MCP Tools Reference](references/mcp-tools.md)
- [Video Prompt Guide](references/prompts.md)
