#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 v2 路演演示脚本
5 分钟完整演示流程，现场路演直接用
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from knowledge_graph import KnowledgeGraph
from smart_recommend import SmartRecommender
from ppt_outline import PPTOutliner
from lab_log import LabLogAssistant

# 初始化
kg = KnowledgeGraph(db_path=':memory:')  # 演示用内存数据库
recommender = SmartRecommender(kg_path=':memory:')
ppt_outliner = PPTOutliner()
lab_log = LabLogAssistant()


def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def print_section(text):
    print(f"\n【{text}】")
    print("-" * 50)


def print_step(num, text):
    print(f"\n▶ 步骤{num}: {text}")


def wait(seconds=1):
    time.sleep(seconds)


def demo_opening():
    """开场（30 秒）"""
    print_header("🦞 学术龙虾 v2 · 科研知识大脑")
    
    print_section("痛点")
    print("""
在座的评委老师可能都带过研究生。
您有没有遇到过这种情况：

学生读了两年论文，
但知识是碎片化的，
问他这个领域有哪些方法，他说不清楚。

为什么？因为缺少知识的大脑。
    """)
    wait(2)
    
    print_section("解决方案")
    print("""
学术龙虾 v2 不是又一个文献管理工具，
而是科研知识的大脑。

三大核心功能：
1. 知识图谱 - 让碎片化知识形成体系
2. 智能关联 - 让实验和论文相互支撑
3. 一键生成 - 让重复劳动自动化
    """)
    wait(2)
    
    print_section("价值")
    print("""
所有数据本地存储，安全可控；
联网爬取合规透明，尊重知识产权。

愿景：让每一位研究者，都拥有平等的科研智能支持。
    """)
    wait(2)


def demo_knowledge_graph():
    """功能演示 1：知识图谱（90 秒）"""
    print_header("功能演示 1: 知识图谱（独家）")
    
    print_step(1, "添加 ResNet 原始论文")
    kg.add_paper({
        'id': 'paper_001',
        'title': 'Deep Residual Learning for Image Recognition',
        'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
        'year': 2016,
        'research_question': '深层网络训练退化问题',
        'method': '残差连接',
        'conclusion': '可训练 152 层网络，ImageNet 错误率降低',
        'keywords': ['深度学习', '残差学习', '图像识别', 'CNN'],
        'category': '计算机视觉'
    })
    print("✅ 已添加：ResNet 原始论文")
    wait(1)
    
    print_step(2, "添加 Identity Mappings 论文")
    kg.add_paper({
        'id': 'paper_002',
        'title': 'Identity Mappings in Deep Residual Networks',
        'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
        'year': 2016,
        'research_question': '深层网络训练退化问题',
        'method': '改进的残差连接（pre-activation）',
        'conclusion': '恒等映射进一步提升性能',
        'keywords': ['深度学习', '残差学习', '图像识别', 'CNN'],
        'category': '计算机视觉'
    })
    print("✅ 已添加：Identity Mappings 论文")
    wait(1)
    
    print_step(3, "添加你的实验")
    kg.add_experiment({
        'id': 'exp_001',
        'date': '2026-03-12',
        'purpose': '改进 ResNet 残差块',
        'method': '引入注意力机制',
        'result': '准确率 87% → 89%',
        'conclusion': '注意力机制有效',
        'tags': ['注意力机制', 'ResNet 改进']
    })
    print("✅ 已添加：ResNet 改进实验")
    wait(1)
    
    print_step(4, "查看知识图谱")
    print("\n🌳 科研知识图谱（文字树状）")
    print("-" * 50)
    print(kg.export_to_text())
    
    print("\n💡 关键点：")
    print("注意看，系统自动把相同研究问题的论文组织在一起，")
    print("并把你的实验和基础论文关联起来。")
    print("这是市面上没有的功能。")
    wait(3)


def demo_smart_recommend():
    """功能演示 2：智能推荐（60 秒）"""
    print_header("功能演示 2: 实验 - 文献智能关联（独家）")
    
    print_step(1, "输入实验描述")
    exp_text = "使用 ResNet-50 进行图像分类，引入注意力机制，准确率提升 2%"
    print(f"实验：{exp_text}")
    wait(1)
    
    print_step(2, "基础模式（本地推荐）")
    print("🔍 本地模式推荐结果：")
    print("-" * 50)
    
    recommendations = recommender.recommend_papers_for_experiment(exp_text)
    
    for i, rec in enumerate(recommendations, 1):
        paper = rec['paper']
        stars = "★" * int(rec['score'] / 20)
        print(f"\n{i}. {paper['title']}")
        print(f"   相关性：{stars} ({rec['score']:.0f}分)")
        print(f"   匹配理由：{rec['reason']}")
        print(f"   来源：本地知识库")
    
    wait(2)
    
    print_step(3, "进阶模式（联网补充，可选）")
    print("""
🌐 联网模式补充推荐（模拟）：

1. ECA-Net: Efficient Channel Attention (Wang et al., CVPR 2020)
   来源：arXiv (公开摘要)
   相关性：★★★☆☆ (78 分)
   匹配理由：轻量级通道注意力，适合你的场景
   链接：https://arxiv.org/abs/1910.03151
   ⚠️ 声明：仅获取公开摘要，未存储全文

2. CBAM: Convolutional Block Attention Module (Woo et al., ECCV 2018)
   来源：arXiv (公开摘要)
   相关性：★★★☆☆ (75 分)
   匹配理由：空间 + 通道注意力，可对比你的方法
   链接：https://arxiv.org/abs/1807.06521
   ⚠️ 声明：仅获取公开摘要，未存储全文

🔒 合规声明：
- 仅爬取公开、免费的标题/摘要
- 尊重知识产权，不提供全文下载
- 爬取内容仅用于临时推荐，不本地存储
    """)
    wait(3)


def demo_ppt_generation():
    """功能演示 3：PPT 一键生成（60 秒）"""
    print_header("功能演示 3: 组会 PPT 大纲 + 讲稿（独家）")
    
    print_step(1, "输入本周进展")
    progress = """
本周完成了 ResNet-50 在自定义数据集上的迁移学习，
引入注意力机制，准确率从 87% 提升到 89%。
遇到小样本过拟合问题，下周计划尝试数据增强。
    """
    print(f"进展：{progress.strip()}")
    wait(1)
    
    print_step(2, "生成 PPT 大纲 + 讲稿")
    outline = ppt_outliner.generate(progress.strip())
    
    print("\n📊 组会 PPT 大纲（5 页标准版）")
    print("=" * 70)
    
    for slide in outline['slides'][:5]:  # 只显示前 5 页
        print(f"\n{'━' * 35}")
        print(f"P{slide['page']} {slide['title']}")
        print(f"{'━' * 35}")
        for point in slide['points']:
            print(f"• {point}")
        print(f"\n【讲稿】")
        print(f"（根据要点自动生成可直接朗读的讲稿）")
    
    print("\n" + "=" * 70)
    
    print("\n💡 价值：")
    print("原本 2-3 小时的组会准备，现在 5 分钟完成。")
    print("讲稿可以直接朗读，不需要额外准备。")
    wait(3)


def demo_closing():
    """结尾（60 秒）"""
    print_header("价值总结")
    
    print_section("三大核心价值")
    print("""
1. 知识图谱
   → 让碎片化知识形成体系
   
2. 智能关联
   → 让实验和论文相互支撑
   
3. 一键生成
   → 让重复劳动自动化
    """)
    wait(2)
    
    print_section("安全合规")
    print("""
所有数据本地存储，安全可控；
联网爬取合规透明，尊重知识产权。
    """)
    wait(1)
    
    print_section("愿景")
    print("""
让每一位研究者，
都拥有平等的科研智能支持。

学术龙虾 v2，为每一位认真做研究的人服务。

谢谢！
    """)
    wait(2)
    
    print_header("演示结束 · Q&A")


def run_full_demo():
    """运行完整 5 分钟演示"""
    print("\n\n")
    print("🦞" * 35)
    print("  学术龙虾 v2 · 科研知识大脑")
    print("  中关村北纬龙虾大赛 · 5 分钟路演演示")
    print("🦞" * 35)
    print("\n总时长：约 5 分钟")
    print("按 Enter 键开始演示...")
    input()
    
    # 开场（30 秒）
    demo_opening()
    print("\n按 Enter 继续...")
    input()
    
    # 功能 1（90 秒）
    demo_knowledge_graph()
    print("\n按 Enter 继续...")
    input()
    
    # 功能 2（60 秒）
    demo_smart_recommend()
    print("\n按 Enter 继续...")
    input()
    
    # 功能 3（60 秒）
    demo_ppt_generation()
    print("\n按 Enter 继续...")
    input()
    
    # 结尾（60 秒）
    demo_closing()
    
    print("\n\n")
    print("🦞" * 35)
    print("  演示完成")
    print("🦞" * 35)
    print("\n")


if __name__ == '__main__':
    print("\n学术龙虾 v2 路演演示脚本")
    print("=" * 50)
    print("模式选择：")
    print("1. 完整演示（5 分钟，按 Enter 键逐步进行）")
    print("2. 自动演示（3 分钟，自动播放）")
    print("3. 单功能测试")
    print()
    
    choice = input("请选择模式 (1/2/3): ").strip()
    
    if choice == '1':
        run_full_demo()
    elif choice == '2':
        # 自动播放模式
        demo_opening()
        demo_knowledge_graph()
        demo_smart_recommend()
        demo_ppt_generation()
        demo_closing()
    elif choice == '3':
        print("\n功能测试：")
        print("1. 知识图谱")
        print("2. 智能推荐")
        print("3. PPT 生成")
        sub_choice = input("选择功能 (1/2/3): ").strip()
        
        if sub_choice == '1':
            demo_knowledge_graph()
        elif sub_choice == '2':
            demo_smart_recommend()
        elif sub_choice == '3':
            demo_ppt_generation()
    else:
        print("无效选择，运行完整演示")
        run_full_demo()
