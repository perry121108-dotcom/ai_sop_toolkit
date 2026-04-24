import shutil
from pathlib import Path

import click


@click.group()
def main():
    """AI 開發系統化 SOP 工具套件"""


@main.command()
def init():
    """在當前目錄初始化 AI 開發 Skill 環境"""
    template_dir = Path(__file__).parent / "templates"
    current_dir = Path.cwd()

    click.echo("🚀 正在注入 AI 開發系統化 SOP 技能...")

    mapping = {
        "cursorrules.tpl": ".cursorrules",
        "claude_md.tpl": "CLAUDE.md",
        "task_md.tpl": "TASK.md",
        "project_rules_tpl.md": "PROJECT_RULES.md",
    }

    for tpl, target in mapping.items():
        source = template_dir / tpl
        dest = current_dir / target

        if dest.exists():
            if click.confirm(f"⚠️ {target} 已存在，是否覆蓋？", default=False):
                shutil.copy(source, dest)
                click.echo(f"✅ 已更新 {target}")
        else:
            shutil.copy(source, dest)
            click.echo(f"✅ 已建立 {target}")

    click.echo("\n🎉 初始化成功！現在你可以讓 AI 讀取這些檔案並開始開發。")
    click.echo("提示：請先讓 AI 閱讀 PROJECT_RULES.md 以同步開發目標。")


if __name__ == "__main__":
    main()
