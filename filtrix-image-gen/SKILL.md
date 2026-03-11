---
name: filtrix-image-gen
description: Generate images through Filtrix Remote MCP. Use when users ask to create or generate images. Supports gpt-image-1, nano-banana, and nano-banana-2 through one MCP endpoint.
---

# Filtrix Image Gen (MCP)

This skill is MCP-only.

- Endpoint: `https://mcp.filtrix.ai/mcp`
- Auth: `Authorization: Bearer <FILTRIX_MCP_API_KEY>`
- Primary tool: `generate_image_text`

Available MCP tools:

- `get_account_credits`
- `generate_image_text`
- `generate_video_text`
- `get_video_status`

## Setup

Required:
- `FILTRIX_MCP_API_KEY`

Optional:
- `FILTRIX_MCP_URL` (default: `https://mcp.filtrix.ai/mcp`)

## Generate

```bash
python scripts/generate.py \
  --prompt "..." \
  [--mode gpt-image-1|nano-banana|nano-banana-2] \
  [--size 1024x1024|1536x1024|1024x1536|auto] \
  [--resolution 1K|2K|4K] \
  [--search-mode] \
  [--enhance-mode] \
  [--idempotency-key KEY] \
  [--output PATH]
```

## Mode Mapping

- `gpt-image-1`: general quality route
- `nano-banana`: fast generation route
- `nano-banana-2`: advanced generation route

## Idempotency

`idempotency_key` prevents duplicate billing on retries.
If omitted, the script auto-generates one UUID-based key.

## Edit Status

`edit.py` is disabled until public MCP edit tool is available.

## References

- [MCP Install Guide](references/mcp-install.md)
- [MCP Tools Reference](references/mcp-tools.md)
- [gpt-image-1 Mode](references/gpt-image-1.md)
- [nano-banana Mode](references/nano-banana.md)
- [nano-banana-2 Mode](references/nano-banana-2.md)
- [Prompt Guide](references/prompts.md)
