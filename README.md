# Filtrix Skills

Open-source agent skills from [Filtrix AI](https://www.filtrix.ai) — battle-tested capabilities extracted from building AI image and video generation products.

## Why These Skills?

We've spent months building [Filtrix AI](https://app.filtrix.ai), an AI image generation platform serving thousands of users. Along the way, we figured out what works: which API parameters actually matter, how to write prompts that produce great results, and how to handle the quirks of each AI provider.

Instead of keeping that knowledge locked in our product, we're open-sourcing it as agent skills that anyone can use.

## What's Inside

| Skill | Description | Providers |
|-------|-------------|-----------|
| [filtrix-image-gen](./filtrix-image-gen/) | Generate and edit images via multiple AI providers | OpenAI, Google Gemini, fal.ai |

More skills coming soon — video generation, batch processing, and more.

## Quick Install

### Via [skills.sh](https://skills.sh) (works with 20+ agents)

```bash
npx skills add Filtrix-AI/filtrix-skills
```

### Via [ClawHub](https://clawhub.com) (OpenClaw)

```bash
clawhub install filtrix-image-gen
```

### Manual

Copy the skill folder into your agent's skills directory.

## What Makes These Different

- **Zero dependencies** — Pure Python stdlib. No `pip install` needed.
- **Multi-provider** — One skill, multiple AI backends. Bring your own API keys.
- **Production-tested parameters** — Every API call pattern is verified against real production traffic.
- **Prompt expertise included** — 100+ curated prompts at [filtrix.ai/prompts](https://www.filtrix.ai/prompts), with a built-in prompt writing guide.
- **Generate + Edit** — Text-to-image and image-to-image in one package.

## Requirements

- Python 3.10+
- API key(s) for your chosen provider(s):
  - OpenAI: `OPENAI_API_KEY` → [platform.openai.com](https://platform.openai.com)
  - Google Gemini: `GOOGLE_API_KEY` → [aistudio.google.com](https://aistudio.google.com)
  - fal.ai: `FAL_KEY` → [fal.ai/dashboard](https://fal.ai/dashboard)

## Contributing

Issues and PRs welcome. If you find a better prompt pattern or want to add a new provider, open a PR.

## License

MIT

## Links

- [Filtrix AI App](https://app.filtrix.ai) — Full-featured AI image generation platform
- [Prompt Library](https://www.filtrix.ai/prompts) — 100+ curated AI prompts
- [Filtrix Website](https://www.filtrix.ai)
