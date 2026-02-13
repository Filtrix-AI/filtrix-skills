# filtrix-image-gen

Generate and edit images using multiple AI providers — OpenAI (gpt-image-1), Google Gemini (Flash & Pro), and fal.ai (SeedReam, Flux, Recraft).

Built from [Filtrix AI](https://www.filtrix.ai)'s production image generation pipeline. Zero dependencies, pure Python stdlib.

## Features

- **Text-to-Image** — Generate images from text prompts
- **Image-to-Image** — Edit existing images with AI (style transfer, modifications, inpainting)
- **Multi-provider** — OpenAI, Gemini (Flash + Pro), fal.ai with 5+ models
- **High resolution** — Up to 4K output (Gemini Pro)
- **Prompt guide** — Built-in writing tips + 100+ curated prompts at [filtrix.ai/prompts](https://www.filtrix.ai/prompts)

## Quick Start

```bash
# Set your API key
export GOOGLE_API_KEY=your-key-here

# Generate an image
python scripts/generate.py --provider gemini --prompt "a fox in a forest, watercolor style" --size 1024x1024

# Edit an existing image
python scripts/edit.py --provider gemini --image input.png --prompt "make it look like a oil painting"

# High-res with Gemini Pro
python scripts/generate.py --provider gemini --model gemini-3-pro-image-preview --prompt "..." --size 16:9 --resolution 2K
```

## Supported Models

| Provider | Model | Best For |
|----------|-------|----------|
| Gemini | `gemini-2.5-flash-image` (default) | Fast, cheap, iterative work |
| Gemini | `gemini-3-pro-image-preview` | Premium quality, up to 4K |
| OpenAI | `gpt-image-1` | Photorealistic, artistic |
| fal.ai | `seedream45` (default) | Asian aesthetics, anime |
| fal.ai | `flux-pro` | Photorealism |
| fal.ai | `recraft-v3` | Design, illustration |

## File Structure

```
filtrix-image-gen/
├── SKILL.md              # Agent instructions (auto-loaded by compatible agents)
├── scripts/
│   ├── generate.py       # Text-to-image generation
│   └── edit.py           # Image-to-image editing
└── references/
    ├── openai.md          # OpenAI-specific details
    ├── gemini.md          # Gemini-specific details
    ├── fal.md             # fal.ai-specific details
    └── prompts.md         # Prompt writing guide
```

## License

MIT
