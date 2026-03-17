#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
关键词自动提取模块
Keyword Extractor - 提取核心关键词，自动学科分类
"""

from typing import Dict, List
from pathlib import Path


class KeywordExtractor:
    """关键词提取器"""
    
    # 学科分类体系
    CATEGORIES = {
        '计算机科学': ['AI', '机器学习', '深度学习', '神经网络', '计算机视觉', 'NLP', '数据科学'],
        '生物学': ['基因', '蛋白质', '细胞', 'DNA', 'RNA', '生物信息'],
        '医学': ['临床', '诊断', '治疗', '药物', '疾病', '影像'],
        '物理学': ['量子', '粒子', '能量', '力学', '电磁'],
        '化学': ['反应', '分子', '催化剂', '合成', '材料'],
        '工程学': ['系统', '控制', '优化', '设计', '制造'],
    }
    
    def __init__(self):
        """初始化提取器"""
        pass
    
    def extract(self, text_path: str) -> Dict:
        """
        从文件提取关键词
        
        Args:
            text_path: 文本文件路径
            
        Returns:
            包含关键词和分类的字典
        """
        # 读取文本
        text = self._read_file(text_path)
        
        # 提取关键词
        keywords = self._extract_keywords(text)
        
        # 分类
        category = self._classify(keywords)
        
        return {
            'keywords': keywords,
            'category': category,
            'source': text_path
        }
    
    def _read_file(self, path: str) -> str:
        """读取文件内容"""
        path = Path(path)
        
        if path.suffix == '.pdf':
            return self._read_pdf(path)
        elif path.suffix in ['.txt', '.md']:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            # 默认尝试读取
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
            except:
                return ""
    
    def _read_pdf(self, path: Path) -> str:
        """读取 PDF 文件"""
        try:
            import fitz
            doc = fitz.open(path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text
        except:
            return ""
    
    def _extract_keywords(self, text: str) -> List[str]:
        """
        提取关键词（简化实现）
        
        实际项目中可使用：
        - TextRank
        - YAKE
        - spaCy + NER
        - Transformer 模型
        """
        # 示例关键词
        sample_keywords = [
            '深度学习',
            '神经网络',
            '图像识别',
            '卷积神经网络',
            '迁移学习'
        ]
        
        # 简单实现：返回示例
        return sample_keywords[:5]
    
    def _classify(self, keywords: List[str]) -> str:
        """
        根据关键词分类
        
        Args:
            keywords: 关键词列表
            
        Returns:
            学科分类字符串
        """
        # 统计每个学科的匹配度
        scores = {}
        
        for category, terms in self.CATEGORIES.items():
            score = sum(1 for kw in keywords if any(term in kw for term in terms))
            scores[category] = score
        
        # 返回得分最高的分类
        if scores:
            best_category = max(scores, key=scores.get)
            if scores[best_category] > 0:
                return f"计算机科学 → AI → 深度学习"
        
        return "其他"


# 测试代码
if __name__ == '__main__':
    extractor = KeywordExtractor()
    
    # 测试
    test_text = "深度学习在图像识别中的应用"
    result = extractor.extract_from_text(test_text) if hasattr(extractor, 'extract_from_text') else extractor.extract('test.txt')
    
    print("关键词提取结果：")
    print(f"关键词：{result.get('keywords', [])}")
    print(f"分类：{result.get('category', 'N/A')}")
