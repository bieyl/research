#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
组会 PPT 大纲生成模块
PPT Outliner - 根据研究进展生成汇报结构
"""

from typing import Dict, List
from datetime import datetime


class PPTOutliner:
    """PPT 大纲生成器"""
    
    # 标准汇报模板
    TEMPLATES = {
        'weekly': [
            {'page': 1, 'title': '标题页', 'points': ['研究进展汇报', '姓名、日期'], 'chart_type': None},
            {'page': 2, 'title': '本周工作概述', 'points': ['完成的主要工作', '关键进展'], 'chart_type': 'list'},
            {'page': 3, 'title': '研究背景', 'points': ['问题定义', '研究意义'], 'chart_type': 'text'},
            {'page': 4, 'title': '相关工作', 'points': ['方法 A', '方法 B', '现有方法的不足'], 'chart_type': 'table'},
            {'page': 5, 'title': '方法设计', 'points': ['整体架构', '关键改进'], 'chart_type': 'diagram'},
            {'page': 6, 'title': '实验设置', 'points': ['数据集', '评估指标', '对比方法'], 'chart_type': 'table'},
            {'page': 7, 'title': '实验结果', 'points': ['主要结果', '对比分析'], 'chart_type': 'chart'},
            {'page': 8, 'title': '问题分析', 'points': ['遇到的问题', '可能原因'], 'chart_type': 'list'},
            {'page': 9, 'title': '下一步计划', 'points': ['待完成工作', '预期目标'], 'chart_type': 'timeline'},
            {'page': 10, 'title': '致谢', 'points': ['感谢导师和同门'], 'chart_type': None},
        ],
        'proposal': [
            {'page': 1, 'title': '标题页', 'points': ['开题报告', '姓名、日期'], 'chart_type': None},
            {'page': 2, 'title': '研究背景', 'points': ['领域现状', '存在问题'], 'chart_type': 'text'},
            {'page': 3, 'title': '研究目标', 'points': ['核心目标', '预期贡献'], 'chart_type': 'list'},
            {'page': 4, 'title': '研究内容', 'points': ['主要内容 1', '主要内容 2', '主要内容 3'], 'chart_type': 'diagram'},
            {'page': 5, 'title': '技术路线', 'points': ['方法设计', '实验方案'], 'chart_type': 'flowchart'},
            {'page': 6, 'title': '进度安排', 'points': ['阶段 1', '阶段 2', '阶段 3'], 'chart_type': 'timeline'},
            {'page': 7, 'title': '预期成果', 'points': ['论文', '专利', '系统'], 'chart_type': 'list'},
            {'page': 8, 'title': '参考文献', 'points': ['关键文献列表'], 'chart_type': 'text'},
        ],
    }
    
    def __init__(self):
        """初始化生成器"""
        pass
    
    def generate(self, progress: str, template_type: str = 'weekly') -> Dict:
        """
        生成 PPT 大纲
        
        Args:
            progress: 研究进展描述
            template_type: 模板类型（weekly/proposal）
            
        Returns:
            PPT 大纲字典
        """
        # 获取模板
        template = self.TEMPLATES.get(template_type, self.TEMPLATES['weekly'])
        
        # 根据进展内容微调大纲
        outline = self._customize_template(template, progress)
        
        return {
            'title': '研究进展汇报',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'slides': outline
        }
    
    def _customize_template(self, template: List[Dict], progress: str) -> List[Dict]:
        """
        根据进展内容自定义模板
        
        Args:
            template: 标准模板
            progress: 研究进展
            
        Returns:
            自定义后的大纲
        """
        # 简化实现：返回原模板
        # 实际项目中应分析 progress 内容，调整大纲
        
        outline = []
        for slide in template:
            outline.append(slide.copy())
        
        return outline


# 测试代码
if __name__ == '__main__':
    outliner = PPTOutliner()
    
    # 测试
    progress = "本周完成了 ResNet-50 在自定义数据集上的迁移学习，准确率 87%，遇到小样本过拟合问题"
    
    outline = outliner.generate(progress)
    
    print("PPT 大纲")
    print("=" * 50)
    for slide in outline['slides']:
        print(f"P{slide['page']} {slide['title']}")
        for point in slide['points']:
            print(f"   • {point}")
    print("=" * 50)
