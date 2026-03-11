# MCP Install Guide

Use this guide to connect Filtrix MCP in Cursor / Claude Desktop.

## 1) Create Filtrix MCP API key

Create a key in Filtrix key-management page.

## 2) Add server config

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

## 3) Restart client

Restart Cursor / Claude Desktop.

## 4) Verify tools

Call:

1. `get_account_credits`
2. `generate_image_text`

If both work, installation is complete.

## 5) Troubleshooting

- `401 Unauthorized`: key invalid / revoked / malformed header
- `402`: insufficient credits
- `409 already_deducted`: duplicate `idempotency_key`
