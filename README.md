# ai-dev-sop-toolkit

A lightweight Python CLI toolkit that bootstraps an AI-driven development SOP into any new project directory.

After installation, run `ai-sop init` inside a target project folder to generate:

- `.cursorrules`
- `CLAUDE.md`
- `TASK.md`
- `PROJECT_RULES.md`

These files help standardize requirement discovery, task tracking, validation, and development guardrails for AI-assisted coding workflows.

## Project Structure

```text
ai-dev-sop-toolkit/
├── setup.py
├── README.md
└── ai_sop_toolkit/
    ├── __init__.py
    ├── cli.py
    └── templates/
        ├── cursorrules.tpl
        ├── claude_md.tpl
        ├── task_md.tpl
        └── project_rules_tpl.md
```

## Installation

From the project root:

```bash
pip install -e .
```

Using editable mode means you can update template files without reinstalling the package.

If you want to install it as a normal package later:

```bash
pip install .
```

## Usage

Move into any new or existing project folder and run:

```bash
ai-sop init
```

The CLI will copy the built-in templates into the current working directory. If a target file already exists, the tool will ask whether it should be overwritten.

## Generated Files

- `.cursorrules`: Core SOP instructions for AI coding assistants.
- `CLAUDE.md`: Project rules and prohibitions.
- `TASK.md`: Task progress tracking template.
- `PROJECT_RULES.md`: Project alignment template for goals, scope, and constraints.

## Local Testing

Run the test suite from the project root:

```bash
python -m pytest
```

Or with the Windows launcher:

```bash
py -m pytest
```

## Publish To GitHub

Create a new repository and push this folder:

```bash
git init
git add .
git commit -m "Initial release of ai-dev-sop-toolkit"
git branch -M main
git remote add origin https://github.com/<your-account>/ai-dev-sop-toolkit.git
git push -u origin main
```

Before publishing, update the repository URL in `setup.py` and `pyproject.toml` if you move this project to a different GitHub repository.

## Development Notes

- Entry point: `ai-sop`
- Main CLI implementation: `ai_sop_toolkit/cli.py`
- Template assets live in: `ai_sop_toolkit/templates/`

## Roadmap Ideas

- Add customizable template profiles.
- Support non-interactive overwrite flags such as `--force`.
- Publish to PyPI after final package validation.

## License

MIT
