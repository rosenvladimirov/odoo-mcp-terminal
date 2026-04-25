# odoo-mcp-terminal — 16.0

International fork of [`l10n_bg_claude_terminal`](https://github.com/rosenvladimirov/l10n-bulgaria/tree/16.0/l10n_bg_claude_terminal) — Claude Code terminal in Odoo backend (chatter, list, kanban) with AI Tokenizer (Qdrant/Ollama) integration via the MCP Docker stack.

This branch targets **Odoo 16.0**. AI Tokenizer features backported from 19.0
in 16.0.1.28.0 (2026-04-25).

⚠️ **Partial port — UNTESTED on a live Odoo 16 instance:**
- Python models (`ai_*`, `res_company`, `res_config_settings`) — backported as-is from 19.0; expected to work but unverified.
- Existing JS (`terminal_chatter`, `terminal_listview`, `terminal_kanbanview`) — already adapted for Odoo 16 (OWL 1, ChatterTopbar, 3-arg patch).
- New JS `ai_tokenizer_status.js` — written for OWL 2 / Odoo 17+. **Will not load** in Odoo 16 without an OWL 1 rewrite.
- Cron `data/ai_tokenizer_cron.xml`, views `ai_tokenizer_views.xml` — should load if dependent models exist.

The AI status widget (frontend tile) needs a manual port to OWL 1 components or a service-only re-design before 16.0 install will be fully usable.

## Modules

- **`mcp_terminal`** — Claude Code terminal in chatter/list/kanban view + AI Tokenizer backend (Python only in 16; OWL 1 widget rewrite pending).

## Mutually exclusive with

- `l10n_bg_claude_terminal` (the BG-localized sibling). Both modules cannot be installed in the same database — Odoo enforces this via the `excludes` manifest field on both sides.

## License

AGPL-3.0 — see [LICENSE](LICENSE).
