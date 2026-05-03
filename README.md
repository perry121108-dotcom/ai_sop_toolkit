# ai_agent_sop_toolkit

[![CI](https://github.com/perry121108-dotcom/ai_agent_sop_toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/perry121108-dotcom/ai_agent_sop_toolkit/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A pip-installable Python CLI that bootstraps AI agent collaboration files into any new project in under 5 seconds.

可安裝的 Python CLI 工具，在任何新專案中 5 秒內建立完整的 AI Agent 協作 SOP 結構。

```bash
pip install -e .
ai-sop init
```

---

## What It Does / 功能說明

Run `ai-sop init` inside any project folder and get 6 structured files instantly:

在任意專案資料夾執行 `ai-sop init`，立即產生 6 個協作結構檔：

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

這些檔案讓 Cursor、Claude Code 等 AI 助手在每個專案中保持一致的需求釐清、任務追蹤、驗收流程與角色交接結構。

---

## Generated Files / 產生的檔案

| 檔案 | 用途 |
|------|------|
| `.cursorrules` | AI 助手核心 SOP 指令 / Core SOP instructions for AI coding assistants |
| `CLAUDE.md` | 專案規則與限制 / Project rules and guardrails |
| `TASK.md` | 任務進度追蹤 / Task progress tracking |
| `WORKLOG.md` | 逐次作業紀錄 / Session-by-session work log |
| `PROJECT_RULES.md` | 目標、範圍與限制模板 / Goals, scope, and constraints template |
| `AGENTS.md` | 五角色 Agent Team：PM · Architect · Builder · Tester · Liaison |

---

## Install / 安裝

```bash
git clone https://github.com/perry121108-dotcom/ai_agent_sop_toolkit
cd ai_agent_sop_toolkit
pip install -e .
```

驗證安裝 / Verify:

```bash
ai-sop --version
# ai-sop, version 1.3.0

ai-sop --help
# Usage: ai-sop [OPTIONS] COMMAND [ARGS]...
```

---

## Usage / 使用方式

```bash
# 進入任意新專案資料夾 / Go to any new project
cd my-new-project

# 建立 AI 協作結構 / Scaffold AI collaboration files
ai-sop init
```

如果目標檔案已存在，CLI 會詢問是否覆蓋，不會靜默刪除任何內容。

If a file already exists, the CLI asks before overwriting — nothing is deleted silently.

---

## Project Structure / 專案結構

```
ai_agent_sop_toolkit/
├── pyproject.toml
├── setup.py
├── README.md
├── ai_sop_toolkit/
│   ├── cli.py          ← Click CLI 入口點 / entrypoint
│   └── templates/      ← 6 個 SOP 模板檔案 / SOP template files
└── tests/
```

---

## Run Tests / 執行測試

```bash
python -m pytest
```

---

## Why This Exists / 為什麼做這個工具

在多個 AI 協作開發專案中，我發現每次都要從零重建任務追蹤、Agent 角色定義與交接結構，非常費時。這個 CLI 把這套做法打包成可重複使用的工具，讓新專案一開始就有結構，而不是從混亂開始。

After working on multiple AI-assisted development projects, I kept rebuilding the same task tracking, agent role, and handoff structure from scratch. This CLI packages that pattern so any new project starts with structure instead of chaos.

---

## Roadmap

- `--force` 旗標，跳過覆蓋確認 / skip overwrite prompts
- 命名 profile（`ai-sop init --profile minimal`）
- 發布到 PyPI / PyPI publish

---

## License

MIT
