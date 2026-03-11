# MCP Tools Reference

Filtrix MCP endpoint:

- URL: `https://mcp.filtrix.ai/mcp`
- Auth header: `Authorization: Bearer <FILTRIX_MCP_API_KEY>`

This page documents MCP tool names, input arguments, and typical outputs.

## Tools

### `get_account_credits`

Purpose: query current account credits and subscription status.

Input arguments:

- none

Typical output:

- `ok` boolean
- `credits` number
- `tier` string or null
- `status` string or null

Example `tools/call` arguments:

```json
{}
```

### `generate_image_text`

Purpose: generate one image from text prompt.

Input arguments:

- `prompt` required, string, `1..4000`
- `mode` optional, enum, default `gpt-image-1`
  - `gpt-image-1`
  - `nano-banana`
  - `nano-banana-2`
- `model` optional, string
  - backward-compatible alias; prefer `mode`
- `size` optional, enum, default `1024x1024`
  - `1024x1024`
  - `1536x1024`
  - `1024x1536`
  - `auto`
- `resolution` optional, enum, default `1K`
  - `1K`
  - `2K`
  - `4K`
  - used by `nano-banana-2`
- `search_mode` optional, boolean, default `false`
  - used by `nano-banana-2`
- `enhance_mode` optional, boolean, default `false`
  - used by `nano-banana-2`
- `idempotency_key` required, string, `8..128`

Typical output:

- `ok` boolean
- `image` string, storage path
- `image_path` string, same as `image`
- `image_url` string or null, signed URL
- `image_url_error` string or null
- `credits_used` number
- `mode` string
- `model` string (normalized model name)

Example `tools/call` arguments:

```json
{
  "prompt": "a cinematic fox in snow, film still",
  "mode": "gpt-image-1",
  "size": "1024x1024",
  "idempotency_key": "img-001-demo"
}
```

### `generate_video_text`

Purpose: start text-to-video generation task.

Input arguments:

- `prompt` required, string, `1..4000`
- `aspect_ratio` optional, string, default `16:9`
- `idempotency_key` required, string, `8..128`

Typical output:

- `ok` boolean
- downstream task payload from video backend
  - typically includes request/task id and status fields

Example `tools/call` arguments:

```json
{
  "prompt": "a drone shot over neon city at night",
  "aspect_ratio": "16:9",
  "idempotency_key": "vid-001-demo"
}
```

### `get_video_status`

Purpose: query status for a previously created video request.

Input arguments:

- `request_id` required, string

Typical output:

- `ok` boolean
- downstream status payload from video backend

Example `tools/call` arguments:

```json
{
  "request_id": "your-request-id"
}
```

## Idempotency Rules

- Reusing the same `idempotency_key` for the same user and same feature prevents duplicate billing.
- Duplicate replay normally returns an `already_deducted` style response (often mapped to HTTP `409` downstream).
- New generation intent should use a new `idempotency_key`.

## Common Error Patterns

- `401 Unauthorized`: invalid or revoked MCP API key
- `402`: insufficient credits
- `409`: duplicate `idempotency_key`
- `400`: invalid tool arguments

