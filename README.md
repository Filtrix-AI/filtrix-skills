# Filtrix Skills

Open-source agent skills from [Filtrix AI](https://www.filtrix.ai).

This repository is MCP-first. Skills call Filtrix Remote MCP and do not require direct provider API keys.

## Available Skills

| Skill | What It Does | Access |
|-------|-------------|--------|
| [filtrix-image-gen](./filtrix-image-gen/) | Text-to-image generation via Filtrix MCP | Filtrix MCP API key |
| [filtrix-video-gen](./filtrix-video-gen/) | Text-to-video generation + task polling via Filtrix MCP | Filtrix MCP API key |
| [seedance-2-0-prompting-skills](./seedance-2-0-prompting-skills/) | Seedance 2.0 prompt design framework for stable motion and shot control | No MCP call required |

## Install Skills

```bash
npx skills add Filtrix-AI/filtrix-skills
```

For local testing:

```bash
npx -y skills add /absolute/path/to/filtrix-skills --yes
```

## Shared MCP Setup

All Filtrix MCP skills use the same server config.

### 1) Create API key

Create an MCP API key from your Filtrix account key-management page.

### 2) Add MCP server in your client

```json
{
  "mcpServers": {
    "filtrix": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://mcp.filtrix.ai/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer <YOUR_FILTRIX_MCP_API_KEY>"
      }
    }
  }
}
```

### 3) Restart client and verify

Run:

1. `get_account_credits`
2. `generate_image_text` or `generate_video_text`

If these return valid responses, MCP is ready.

## Tool References

- Image tools: [filtrix-image-gen/references/mcp-tools.md](./filtrix-image-gen/references/mcp-tools.md)
- Video tools: [filtrix-video-gen/references/mcp-tools.md](./filtrix-video-gen/references/mcp-tools.md)

## Environment Variables (script mode)

```bash
export FILTRIX_MCP_API_KEY=your-mcp-key
# optional
export FILTRIX_MCP_URL=https://mcp.filtrix.ai/mcp
```

## Notes

- `filtrix-image-gen/scripts/edit.py` is currently disabled in MCP mode.

## License

MIT

## Links

- [Filtrix AI App](https://app.filtrix.ai)
- [Prompt Library](https://www.filtrix.ai/prompts)
- [skills.sh](https://skills.sh)
