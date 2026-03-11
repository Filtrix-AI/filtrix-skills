# Filtrix Skills

Open-source agent skills from [Filtrix AI](https://www.filtrix.ai).

This repository is MCP-first. Skills call Filtrix Remote MCP and do not require direct provider API keys.

## Available Skills

| Skill | What It Does | Access |
|-------|-------------|--------|
| [filtrix-image-gen](./filtrix-image-gen/) | Text-to-image generation via Filtrix MCP | Filtrix MCP API key |

## Install Skill

### Option 1: One-Line Install

```bash
npx skills add Filtrix-AI/filtrix-skills
```

### Option 2: Manual Install

```bash
git clone https://github.com/Filtrix-AI/filtrix-skills.git
```

Then copy the target skill folder into your agent's skills directory.

## Install MCP (for end users)

### Step 1: Create API key

Create an MCP API key from your Filtrix account key-management page.

### Step 2: Add MCP server in your client

Use `mcp-remote` to connect stdio clients to Filtrix remote MCP.

Cursor / Claude Desktop config example:

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

### Step 3: Verify

After restart, run these tools in your MCP client:

1. `get_account_credits`
2. `generate_image_text`

If both succeed, MCP is ready.

## MCP Tools and Parameters

Tool reference is documented here:

- [MCP Tools Reference](./filtrix-image-gen/references/mcp-tools.md)

Current toolset:

- `get_account_credits`
- `generate_image_text`
- `generate_video_text`
- `get_video_status`

## Environment Variables (for script mode)

```bash
export FILTRIX_MCP_API_KEY=your-mcp-key
# optional
export FILTRIX_MCP_URL=https://mcp.filtrix.ai/mcp
```

## Notes

- `filtrix-image-gen/scripts/edit.py` is currently disabled in MCP mode.
- Image editing will return when MCP edit tool is published.

## License

MIT

## Links

- [Filtrix AI App](https://app.filtrix.ai)
- [Prompt Library](https://www.filtrix.ai/prompts)
- [skills.sh](https://skills.sh)
