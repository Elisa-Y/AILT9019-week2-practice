# AILT9019-week2-practice
This repository contains my Week 2 practice for AILT9019 AI Literacy II.

## What's inside

- `SKILL.md` — a custom skill that turns rough meeting notes into a short action list.
- `mcp_server.py` — a small MCP server that exposes one tool: `get_today_date`.
- `.mcp.json` — configuration file that registers the MCP server with CodeBuddy.
- `requirements.txt` — Python dependencies for the MCP server.
- `test_mcp.py` — a small script to test the MCP tool.

## Skill: Meeting-notes cleaner

Purpose: turn rough meeting notes into a short action list.

Use when: the user pastes text marked `[MEETING NOTES]`.

Steps:
1. List every action item as `owner, task, due date`.
2. List open questions separately.
3. Change nothing else.

## MCP tool: get_today_date

A minimal MCP server that returns today's date in `YYYY-MM-DD` format.

To run it locally:

```bash
pip install -r requirements.txt
python mcp_server.py
