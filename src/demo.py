#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾演示脚本
Demo Script - 用于大赛现场演示
"""

import sys
import time
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from summarizer import PaperSummarizer
from lab_log import LabLogAssistant
from ppt_outline import PPTOutliner
from reference_formatter import ReferenceFormatter


def print_header(text: str):
    """打印标题"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def print_step(step: int, text: str):
    """打印步骤"""
    print(f"\n【步骤 {step}】{text}")
    print("-" * 40)


def demo_summarizer():
    """演示文献摘要功能"""
    print_header("功能演示 1: 文献智能摘要")
    
    print_step(1, "上传论文 PDF")
    print("📄 文件：resnet.pdf (Deep Residual Learning for Image Recognition)")
    
    print_step(2, "点击'生成摘要'")
    print("⏳ 处理中...")
    time.sleep(1)
    
    print_step(3, "查看结果")
    
    summarizer = PaperSummarizer()
    # 使用示例数据演示（无需真实 PDF 文件）
    summary = summarizer.generate_summary('resnet_demo')
    
    print("\n📚 论文摘要")
    print("-" * 40)
    print(f"【研究问题】{summary['research_question']}")
    print(f"【研究方法】{summary['method']}")
    print(f"【核心结论】{summary['conclusion']}")
    print(f"【创新点】{summary['innovation']}")
    print(f"【关键词】{', '.join(summary['keywords'])}")
    print("-" * 40)
    
    print("\n✅ 演示完成！原本需要 2 小时的文献阅读，现在只需 30 秒。")


def demo_lablog():
    """演示实验日志功能"""
    print_header("功能演示 2: 实验日志助手")
    
    print_step(1, "输入实验数据")
    raw_data = "温度 60°C/70°C/80°C，反应时间 2h，产物收率 45%/62%/38%"
    print(f"📝 输入：{raw_data}")
    
    print_step(2, "点击'生成日报'")
    print("⏳ 处理中...")
    time.sleep(1)
    
    print_step(3, "查看结果")
    
    assistant = LabLogAssistant()
    report = assistant.generate_report(raw_data)
    
    print("\n📝 实验日报")
    print("-" * 40)
    print(report)
    print("-" * 40)
    
    print("\n✅ 演示完成！原本需要 30 分钟的实验报告，现在只需 1 分钟。")


def demo_ppt():
    """演示 PPT 大纲功能"""
    print_header("功能演示 3: 组会 PPT 大纲")
    
    print_step(1, "输入研究进展")
    progress = "本周完成了 ResNet-50 在自定义数据集上的迁移学习，准确率 87%，遇到小样本过拟合问题"
    print(f"📄 输入：{progress}")
    
    print_step(2, "点击'生成 PPT 大纲'")
    print("⏳ 处理中...")
    time.sleep(1)
    
    print_step(3, "查看结果")
    
    outliner = PPTOutliner()
    outline = outliner.generate(progress)
    
    print("\n📊 PPT 大纲")
    print("-" * 40)
    for slide in outline['slides']:
        print(f"P{slide['page']} {slide['title']}")
        for point in slide['points']:
            print(f"   • {point}")
    print("-" * 40)
    
    print("\n✅ 演示完成！原本需要 2 小时的 PPT 准备，现在只需 30 分钟。")


def demo_reference():
    """演示参考文献格式化功能"""
    print_header("功能演示 4: 参考文献格式化")
    
    print_step(1, "输入参考文献")
    ref = "He K, Zhang X, Ren S, Sun J. Deep Residual Learning for Image Recognition. CVPR 2016."
    print(f"📖 输入：{ref}")
    
    print_step(2, "选择格式并点击'格式化'")
    print("⏳ 处理中...")
    time.sleep(1)
    
    print_step(3, "查看结果")
    
    formatter = ReferenceFormatter()
    result = formatter.format(ref)
    
    print("\n📖 格式化结果")
    print("-" * 40)
    for fmt, formatted in result.items():
        print(f"【{fmt}】{formatted}")
    print("-" * 40)
    
    print("\n✅ 演示完成！原本需要 15 分钟的格式调整，现在只需 5 秒。")


def run_full_demo():
    """运行完整演示"""
    print("\n" + "🦞" * 30)
    print("  学术龙虾 (Academic Lobster)")
    print("  中关村北纬龙虾大赛・学术赛道参赛作品")
    print("🦞" * 30)
    
    print("\n📢 开场介绍:")
    print("-" * 60)
    print("各位评委好，我是学术龙虾。")
    print("在中国，每年有 100 万研究生投入科研，")
    print("但普通课题组往往没有经费聘请科研助理。")
    print("学术龙虾是一款完全本地化的 AI 科研助手，")
    print("让每一位研究者，无论身处何种实验室，")
    print("都能获得平等的智能支持。")
    print("下面我用 3 分钟演示核心功能。")
    print("-" * 60)
    
    # 演示各个功能
    demo_summarizer()
    time.sleep(1)
    
    demo_lablog()
    time.sleep(1)
    
    demo_ppt()
    time.sleep(1)
    
    demo_reference()
    
    # 结尾
    print_header("价值总结")
    print("\n📢 结尾介绍:")
    print("-" * 60)
    print("学术龙虾不追求大而全，")
    print("我们专注解决一个核心问题：")
    print("让资源有限的研究者，也能获得智能科研支持。")
    print("所有数据本地处理，安全可控；")
    print("所有功能真实可落地，可直接用于课题组。")
    print("好的科研工具，不应是少数人的特权。")
    print("学术龙虾，为每一位认真做研究的人服务。")
    print("谢谢！")
    print("-" * 60)
    
    print("\n" + "🦞" * 30)
    print("  演示结束")
    print("🦞" * 30 + "\n")


if __name__ == '__main__':
    run_full_demo()
