# odoo-mcp-terminal — 16.0

International fork of [`l10n_bg_claude_terminal`](https://github.com/rosenvladimirov/l10n-bulgaria/tree/16.0/l10n_bg_claude_terminal) — Claude Code terminal in Odoo backend (chatter, list, kanban) connected to the MCP Docker stack.

This branch targets **Odoo 16.0**. The 16.0 branch does **not** include the AI Tokenizer (Qdrant/Ollama) features that are present in 18.0/19.0 — only the terminal UI.

## Modules

- **`mcp_terminal`** — Claude Code terminal in chatter/list/kanban view.

## Mutually exclusive with

- `l10n_bg_claude_terminal` (the BG-localized sibling). Both modules cannot be installed in the same database — Odoo enforces this via the `excludes` manifest field on both sides.

## License

AGPL-3.0 — see [LICENSE](LICENSE).
