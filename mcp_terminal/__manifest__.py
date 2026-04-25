# Copyright 2026 Rosen Vladimirov <vladimirov.rosen@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "MCP Terminal (Chatter & List View)",
    "version": "16.0.1.18.0",
    "category": "Productivity",
    "summary": "Claude Code terminal in chatter, list & kanban — MCP Docker stack (international)",
    "author": "Rosen Vladimirov, BL Consulting",
    "maintainers": ["rosen-vladimirov"],
    "website": "https://github.com/rosenvladimirov/odoo-mcp-terminal",
    "license": "AGPL-3",
    "depends": ["mail", "web", "bus", "hr"],
    "excludes": ["l10n_bg_claude_terminal"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_users_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "mcp_terminal/static/src/scss/terminal.scss",
            "mcp_terminal/static/src/scss/terminal_live_refresh.scss",
            "mcp_terminal/static/src/js/terminal_refresh_service.js",
            "mcp_terminal/static/src/js/terminal_live_refresh.js",
            "mcp_terminal/static/src/js/terminal_utils.js",
            "mcp_terminal/static/src/js/terminal_chatter.js",
            "mcp_terminal/static/src/xml/terminal_chatter.xml",
            "mcp_terminal/static/src/js/terminal_listview.js",
            "mcp_terminal/static/src/xml/terminal_listview.xml",
            "mcp_terminal/static/src/js/terminal_kanbanview.js",
            "mcp_terminal/static/src/xml/terminal_kanbanview.xml",
        ],
    },
    "installable": True,
    "application": False,
}
