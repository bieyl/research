#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 (Academic Lobster) - 主程序入口
为每一位研究者，都拥有平等的科研智能支持。
"""

import sys
import os
import click
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from summarizer import PaperSummarizer
from keyword_extractor import KeywordExtractor
from lab_log import LabLogAssistant
from ppt_outline import PPTOutliner
from reference_formatter import ReferenceFormatter
from voice_interface import VoiceInterface


@click.group()
@click.version_option(version='1.0.0', prog_name='学术龙虾')
def cli():
    """🦞 学术龙虾 - 科研全流程 AI 助手"""
    pass


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output', '-o', default=None, help='输出文件路径')
def summarize(pdf_path, output):
    """生成论文摘要"""
    summarizer = PaperSummarizer()
    summary = summarizer.generate_summary(pdf_path)
    
    click.echo("\n📚 论文摘要")
    click.echo("=" * 50)
    click.echo(f"【研究问题】{summary.get('research_question', 'N/A')}")
    click.echo(f"【研究方法】{summary.get('method', 'N/A')}")
    click.echo(f"【核心结论】{summary.get('conclusion', 'N/A')}")
    click.echo(f"【创新点】{summary.get('innovation', 'N/A')}")
    click.echo(f"【关键词】{', '.join(summary.get('keywords', []))}")
    click.echo("=" * 50)
    
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(str(summary))
        click.echo(f"✓ 摘要已保存到：{output}")


@cli.command()
@click.argument('text_path', type=click.Path(exists=True))
def keywords(text_path):
    """提取关键词"""
    extractor = KeywordExtractor()
    result = extractor.extract(text_path)
    
    click.echo("\n🔑 关键词提取")
    click.echo("=" * 50)
    click.echo("关键词：")
    for kw in result.get('keywords', []):
        click.echo(f"  • {kw}")
    click.echo(f"\n学科分类：{result.get('category', 'N/A')}")
    click.echo("=" * 50)


@cli.command()
@click.option('--voice', '-v', is_flag=True, help='使用语音输入')
@click.option('--output', '-o', default=None, help='输出文件路径')
def lablog(voice, output):
    """生成实验日志"""
    assistant = LabLogAssistant()
    
    if voice:
        click.echo("🎤 请开始说话（说'结束'完成输入）...")
        raw_data = assistant.voice_input()
    else:
        click.echo("📝 请输入实验数据（输入'END'完成）：")
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        raw_data = '\n'.join(lines)
    
    report = assistant.generate_report(raw_data)
    
    click.echo("\n📝 实验日报")
    click.echo("=" * 50)
    click.echo(report)
    click.echo("=" * 50)
    
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(report)
        click.echo(f"✓ 报告已保存到：{output}")


@cli.command()
@click.option('--output', '-o', default=None, help='输出文件路径')
def ppt(output):
    """生成 PPT 大纲"""
    outliner = PPTOutliner()
    
    click.echo("📄 请输入本周研究进展：")
    progress = input()
    
    outline = outliner.generate(progress)
    
    click.echo("\n📊 PPT 大纲")
    click.echo("=" * 50)
    for slide in outline.get('slides', []):
        click.echo(f"P{slide['page']} {slide['title']}")
        for point in slide.get('points', []):
            click.echo(f"   • {point}")
    click.echo("=" * 50)
    
    if output:
        import json
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(outline, f, ensure_ascii=False, indent=2)
        click.echo(f"✓ 大纲已保存到：{output}")


@cli.command()
@click.argument('reference')
@click.option('--format', '-f', 'fmt', type=click.Choice(['gb', 'apa', 'ieee']), default='gb', help='输出格式')
def reference(reference, fmt):
    """格式化参考文献"""
    formatter = ReferenceFormatter()
    result = formatter.format(reference, fmt)
    
    click.echo("\n📖 参考文献格式化")
    click.echo("=" * 50)
    for format_name, formatted in result.items():
        click.echo(f"【{format_name}】{formatted}")
    click.echo("=" * 50)


@cli.command()
def voice():
    """语音交互模式"""
    interface = VoiceInterface()
    click.echo("\n🎤 语音交互模式已启动")
    click.echo("支持指令：")
    click.echo("  • '总结这篇论文' - 文献摘要")
    click.echo("  • '生成实验日报' - 实验日志")
    click.echo("  • '导出参考文献' - 参考文献格式化")
    click.echo("  • '退出' - 退出程序")
    click.echo("=" * 50)
    
    interface.listen_and_execute()


@cli.command()
def gui():
    """启动图形界面"""
    try:
        from gui import MainWindow
        from PyQt6.QtWidgets import QApplication
        
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except ImportError:
        click.echo("❌ PyQt6 未安装，请运行：pip install PyQt6")


@cli.command()
def init():
    """初始化配置"""
    from config import Config
    config = Config()
    config.init()
    click.echo("✓ 配置初始化完成")
    click.echo(f"数据目录：{config.data_dir}")


if __name__ == '__main__':
    cli()
