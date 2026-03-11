# filtrix-image-gen (MCP)

Generate images through Filtrix Remote MCP.

## MCP Endpoint

- URL: `https://mcp.filtrix.ai/mcp`
- Auth: `Authorization: Bearer <FILTRIX_MCP_API_KEY>`

## Supported Modes

| Mode | Notes |
|------|-------|
| `gpt-image-1` | Best general quality |
| `nano-banana` | Fast generation |
| `nano-banana-2` | Advanced controls |

## Setup

```bash
export FILTRIX_MCP_API_KEY=your-mcp-key
# optional
export FILTRIX_MCP_URL=https://mcp.filtrix.ai/mcp
```

## Usage

### Generate Images

```bash
# default mode: gpt-image-1
python scripts/generate.py --prompt "a fox in a forest, watercolor style"

# nano-banana
python scripts/generate.py --prompt "cinematic sunset over mountains" --mode nano-banana --size 1536x1024

# nano-banana-2 with advanced options
python scripts/generate.py \
  --prompt "futuristic city at night" \
  --mode nano-banana-2 \
  --size 1024x1536 \
  --resolution 2K \
  --enhance-mode
```

On success:

```
OK: /tmp/filtrix_mcp_gpt-image-1_20260311_120000.png (1820826 bytes)
mode=gpt-image-1 idempotency_key=gen-... credits_used=10
```

## Parameters

- `--prompt` required
- `--mode` optional, default `gpt-image-1`
- `--size` optional, default `1024x1024`
- `--resolution` optional, only used by `nano-banana-2`
- `--search-mode` optional, only used by `nano-banana-2`
- `--enhance-mode` optional, only used by `nano-banana-2`
- `--idempotency-key` optional, auto-generated if omitted
- `--output` optional file path

## Image Editing Status

`edit.py` is intentionally disabled in MCP mode right now.
Current public MCP provides `generate_image_text` only.

## References

- [MCP Install Guide](./references/mcp-install.md)
- [gpt-image-1 Mode](./references/gpt-image-1.md)
- [nano-banana Mode](./references/nano-banana.md)
- [nano-banana-2 Mode](./references/nano-banana-2.md)
- [Prompt Guide](./references/prompts.md)

## License

MIT
