# odoo-mcp-terminal — master (upcoming Odoo 20.0)

International fork of [`l10n_bg_claude_terminal`](https://github.com/rosenvladimirov/l10n-bulgaria) — Claude Code terminal in Odoo backend (chatter, list, kanban) with AI Tokenizer (Qdrant/Ollama) integration via the MCP Docker stack.

This branch tracks **Odoo `master`** (= upcoming 20.0). The `master` branch
in `odoo/odoo` is a moving target — incompatibilities can land daily.
This branch is updated reactively, not proactively.

## Differences from 19.0

- `Chatter` import path: `@mail/chatter/web_portal_project/chatter` (was `@mail/chatter/web_portal/chatter`)
- rpc, list view tag, all other patterns: unchanged from 19.0

⚠️ Untested on a live `master` Odoo. Use only for development tracking
of upcoming 20.0 — not for production. Pin to `19.0` for stable use.

## Modules

- **`mcp_terminal`** — Claude Code terminal in chatter/list/kanban + AI Tokenizer status widget. Connects to an MCP Docker stack (claude-terminal, qdrant, ollama).

## Mutually exclusive with

- `l10n_bg_claude_terminal` (the BG-localized sibling). Both modules cannot be installed in the same database — Odoo enforces this via the `excludes` manifest field on both sides.

## License

AGPL-3.0 — see [LICENSE](LICENSE).
