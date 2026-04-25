# odoo-mcp-terminal

International fork of [`l10n_bg_claude_terminal`](https://github.com/rosenvladimirov/l10n-bulgaria/tree/18.0/l10n_bg_claude_terminal) — Claude Code terminal in Odoo backend (chatter, list, kanban) with AI Tokenizer (Qdrant/Ollama) integration via the MCP Docker stack.

## Branches

| Branch | Odoo version | Module version |
|---|---|---|
| `16.0` | 16.0 | mcp_terminal |
| `18.0` | 18.0 | mcp_terminal |
| `19.0` | 19.0 | mcp_terminal |

## Modules

- **`mcp_terminal`** — Claude Code terminal in chatter/list/kanban + AI Tokenizer status widget. Connects to an MCP Docker stack (claude-terminal, qdrant, ollama).

## Mutually exclusive with

- `l10n_bg_claude_terminal` (the BG-localized sibling). Both modules cannot be installed in the same database — Odoo enforces this via the `excludes` manifest field on both sides.

## License

AGPL-3.0 — see [LICENSE](LICENSE).
