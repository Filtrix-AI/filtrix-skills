#!/usr/bin/env python3
"""
Filtrix MCP Image Editor (disabled for now).

Current public Filtrix MCP exposes text-to-image only (`generate_image_text`).
Image editing tool is intentionally disabled in this skill until MCP edit API
is published.
"""

import sys


def main() -> None:
    print(
        "ERROR: Image edit is temporarily unavailable in MCP mode. "
        "Use scripts/generate.py for text-to-image, or wait for generate_image_edit.",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
