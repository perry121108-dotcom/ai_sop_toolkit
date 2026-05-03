# ai_agent_sop_toolkit

[![CI](https://github.com/perry121108-dotcom/ai_agent_sop_toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/perry121108-dotcom/ai_agent_sop_toolkit/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A pip-installable Python CLI that bootstraps AI agent collaboration files into any new project in under 5 seconds.

```bash
pip install -e .
ai-sop init
```

---

## What It Does

Run `ai-sop init` inside any project folder and get 6 structured files instantly:

```
$ ai-sop init

🚀 Initializing Agent Team SOP (V1.3)...
✅ Created .cursorrules
✅ Created CLAUDE.md
✅ Created TASK.md
✅ Created WORKLOG.md
✅ Created PROJECT_RULES.md
✅ Created AGENTS.md

🎉 Done! Your AI agent team is ready.
💡 AI will switch roles based on AGENTS.md (PM → Architect → Builder → Tester → Liaison)
```

These files give AI assistants (Cursor, Claude Code, etc.) a consistent structure for requirement discovery, task tracking, validation, and agent handoffs.

---

## Generated Files

| File | Purpose |
|------|---------|
| `.cursorrules` | Core SOP instructions for AI coding assistants |
| `CLAUDE.md` | Project rules and guardrails |
| `TASK.md` | Task progress tracking |
| `WORKLOG.md` | Session-by-session work log |
| `PROJECT_RULES.md` | Goals, scope, and constraints template |
| `AGENTS.md` | 5-role agent team: PM · Architect · Builder · Tester · Liaison |

---

## Install

```bash
git clone https://github.com/perry121108-dotcom/ai_agent_sop_toolkit
cd ai_agent_sop_toolkit
pip install -e .
```

Verify:

```bash
ai-sop --version
# ai-sop, version 1.3.0

ai-sop --help
# Usage: ai-sop [OPTIONS] COMMAND [ARGS]...
#   AI Agent Team SOP toolkit (V1.3)
```

---

## Usage

```bash
# Go to any new project
cd my-new-project

# Scaffold AI collaboration files
ai-sop init
```

If a file already exists, the CLI asks before overwriting — nothing is deleted silently.

---

## Project Structure

```
ai_agent_sop_toolkit/
├── pyproject.toml
├── setup.py
├── README.md
├── ai_sop_toolkit/
│   ├── cli.py          ← Click CLI entrypoint
│   └── templates/      ← 6 SOP template files
└── tests/
```

---

## Run Tests

```bash
python -m pytest
```

---

## Why This Exists

After working on multiple AI-assisted development projects, I kept rebuilding the same task tracking, agent role, and handoff structure from scratch. This CLI packages that pattern so any new project starts with structure instead of chaos.

---

## Roadmap

- `--force` flag to skip overwrite prompts
- Named profiles (`ai-sop init --profile minimal`)
- PyPI publish

---

## License

MIT
