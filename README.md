# odoo-mcp-terminal — 17.0

International fork of [`l10n_bg_claude_terminal`](https://github.com/rosenvladimirov/l10n-bulgaria) — Claude Code terminal in Odoo backend (chatter, list, kanban) with AI Tokenizer (Qdrant/Ollama) integration via the MCP Docker stack.

This branch targets **Odoo 17.0** — backported from 18.0 with API adaptations:

- `Chatter` import path: `@mail/core/web/chatter` (was `@mail/chatter/web_portal/chatter` in 18+)
- RPC: service-based `useService("rpc")` (was functional `import { rpc }` in 18+)
- View tags: `<tree>` (was `<list>` in 18+)

⚠️ Untested on a live Odoo 17 instance — backport adapted from source diff
between Odoo 17 and 18 cores. Report issues at the repo.

## Modules

- **`mcp_terminal`** — Claude Code terminal in chatter/list/kanban + AI Tokenizer status widget. Connects to an MCP Docker stack (claude-terminal, qdrant, ollama).

## Mutually exclusive with

- `l10n_bg_claude_terminal` (the BG-localized sibling). Both modules cannot be installed in the same database — Odoo enforces this via the `excludes` manifest field on both sides.

## License

AGPL-3.0 — see [LICENSE](LICENSE).
