# Filtrix Skills

Open-source agent skills from [Filtrix AI](https://www.filtrix.ai) — battle-tested capabilities extracted from building AI image and video generation products.

## What Is This?

This is a collection of **agent skills** — modular capabilities that any AI coding agent can use. If you use Claude Code, Cursor, Copilot, Windsurf, OpenClaw, or any of the [20+ supported agents](https://skills.sh), you can install these skills and your agent will know how to generate and edit images for you.

We built [Filtrix AI](https://app.filtrix.ai), an AI image generation platform. These skills package our production-tested API patterns, prompt expertise, and multi-provider routing into reusable modules that any agent can pick up.

## Available Skills

| Skill | What It Does | Supported Providers |
|-------|-------------|-----------|
| [filtrix-image-gen](./filtrix-image-gen/) | Generate images from text + edit existing images with AI | OpenAI, Google Gemini, fal.ai (5+ models) |

More skills coming soon — video generation, batch processing, and more.

## Installation

### Option 1: One-Line Install (Recommended)

Works with Claude Code, Cursor, Windsurf, Copilot, and [20+ other agents](https://skills.sh):

```bash
npx skills add Filtrix-AI/filtrix-skills
```

This downloads the skills into your project's skills directory. Your agent will automatically detect and use them.

### Option 2: ClawHub (for OpenClaw users)

```bash
npm i -g clawhub          # Install ClawHub CLI (one-time)
clawhub install filtrix-image-gen
```

### Option 3: Manual Install

1. Clone this repo (or download the skill folder):
   ```bash
   git clone https://github.com/Filtrix-AI/filtrix-skills.git
   ```
2. Copy the skill folder you want into your agent's skills directory:
   ```bash
   # For Claude Code:
   cp -r filtrix-skills/filtrix-image-gen .claude/skills/

   # For Cursor:
   cp -r filtrix-skills/filtrix-image-gen .cursor/skills/

   # For OpenClaw:
   cp -r filtrix-skills/filtrix-image-gen ~/.openclaw/skills/
   ```

## Setup (After Install)

Each skill needs API keys from the providers you want to use. Set them as environment variables:

```bash
# Pick one or more — you only need keys for providers you want to use

# Google Gemini (recommended — fast and cheap)
export GOOGLE_API_KEY=your-key-here    # Get at: https://aistudio.google.com

# OpenAI (best quality)
export OPENAI_API_KEY=your-key-here    # Get at: https://platform.openai.com

# fal.ai (most model variety)
export FAL_KEY=your-key-here           # Get at: https://fal.ai/dashboard
```

Add these to your `~/.zshrc` or `~/.bashrc` to persist across sessions.

## Usage

Once installed, just ask your agent naturally:

> "Generate an image of a fox in a forest, watercolor style"

> "Edit this image to look like a cyberpunk scene"

> "Create a 2K landscape photo of a sunset over mountains using Gemini Pro"

Your agent reads the skill's instructions and handles the rest — picking the right provider, setting parameters, and returning the image.

## What Makes These Different

- **Zero dependencies** — Pure Python stdlib. No `pip install` needed.
- **Multi-provider** — One skill, multiple AI backends. Bring your own API keys.
- **Production-tested** — Every API call pattern is verified against real production traffic at [Filtrix AI](https://app.filtrix.ai).
- **Prompt expertise** — 100+ curated prompts at [filtrix.ai/prompts](https://www.filtrix.ai/prompts), with a built-in writing guide.
- **Generate + Edit** — Text-to-image and image-to-image editing in one package.

## Contributing

Issues and PRs welcome. If you find a better prompt pattern or want to add a new provider, open a PR.

## License

MIT

## Links

- [Filtrix AI App](https://app.filtrix.ai) — Full-featured AI image generation platform
- [Prompt Library](https://www.filtrix.ai/prompts) — 100+ curated AI prompts with copy-paste examples
- [skills.sh](https://skills.sh) — The open agent skills ecosystem
