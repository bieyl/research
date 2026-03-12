#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 v2 单元测试套件
Test Suite - 确保核心功能稳定可靠

运行方式：
    python test_suite.py

依赖：
    pip install pytest
"""

import unittest
import sys
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from knowledge_graph import KnowledgeGraph
from smart_recommend import SmartRecommender
from reference_formatter import ReferenceFormatter
from ppt_outline import PPTOutliner
from lab_log import LabLogAssistant


class TestKnowledgeGraph(unittest.TestCase):
    """知识图谱测试"""
    
    def setUp(self):
        """测试前准备"""
        self.kg = KnowledgeGraph(db_path="/tmp/test_kg.json")
    
    def test_add_paper(self):
        """测试添加论文"""
        paper = {
            'id': 'test_001',
            'title': 'Test Paper',
            'authors': ['Author A'],
            'year': 2024,
            'research_question': 'Test Question',
            'method': 'Test Method',
            'conclusion': 'Test Conclusion',
            'keywords': ['test', 'keyword']
        }
        
        node_id = self.kg.add_paper(paper)
        self.assertEqual(node_id, 'test_001')
    
    def test_add_duplicate_paper(self):
        """测试论文去重"""
        paper1 = {
            'id': 'test_002',
            'title': 'Duplicate Paper',
            'authors': ['Author A'],
            'year': 2024,
            'research_question': 'Test',
            'method': 'Test',
            'conclusion': 'Test',
            'keywords': []
        }
        
        paper2 = {
            'id': 'test_003',
            'title': 'Duplicate Paper',  # 相同标题
            'authors': ['Author B'],
            'year': 2025,
            'research_question': 'Test',
            'method': 'Test',
            'conclusion': 'Test',
            'keywords': []
        }
        
        id1 = self.kg.add_paper(paper1)
        id2 = self.kg.add_paper(paper2)
        
        # 应该返回相同的 ID（去重）
        self.assertEqual(id1, id2)
    
    def test_add_experiment(self):
        """测试添加实验"""
        experiment = {
            'id': 'exp_001',
            'title': 'Test Experiment',
            'purpose': 'Test Purpose',
            'method': 'Test Method',
            'results': 'Test Results',
            'tags': ['test']
        }
        
        node_id = self.kg.add_experiment(experiment)
        self.assertEqual(node_id, 'exp_001')


class TestSmartRecommender(unittest.TestCase):
    """智能推荐测试"""
    
    def setUp(self):
        """测试前准备"""
        self.recommender = SmartRecommender(kg_path="/tmp/test_kg.json")
    
    def test_extract_keywords(self):
        """测试关键词提取"""
        text = "使用 ResNet 进行图像分类，采用注意力机制"
        keywords = self.recommender._extract_keywords(text)
        
        self.assertIn('ResNet', keywords)
        self.assertIn('注意力机制', keywords)
    
    def test_calculate_similarity(self):
        """测试相似度计算"""
        query_kw = ['ResNet', '图像分类']
        target_kw = ['ResNet', 'CNN']
        
        score = self.recommender._calculate_similarity(
            query_kw, target_kw, 'ResNet method', 'image classification'
        )
        
        self.assertGreater(score, 0)


class TestReferenceFormatter(unittest.TestCase):
    """参考文献格式化测试"""
    
    def setUp(self):
        """测试前准备"""
        self.formatter = ReferenceFormatter()
    
    def test_gb_format(self):
        """测试 GB/T 7714 格式"""
        paper = {
            'title': 'Deep Residual Learning',
            'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
            'year': 2016,
            'journal': 'CVPR'
        }
        
        formatted = self.formatter.format(paper, style='gb')
        
        self.assertIn('He K', formatted)
        self.assertIn('2016', formatted)
        self.assertIn('Deep Residual Learning', formatted)
    
    def test_apa_format(self):
        """测试 APA 格式"""
        paper = {
            'title': 'Deep Residual Learning',
            'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
            'year': 2016,
            'journal': 'CVPR'
        }
        
        formatted = self.formatter.format(paper, style='apa')
        
        self.assertIn('He', formatted)
        self.assertIn('(2016)', formatted)


class TestPPTOutliner(unittest.TestCase):
    """PPT 大纲生成测试"""
    
    def setUp(self):
        """测试前准备"""
        self.outliner = PPTOutliner()
    
    def test_generate_outline(self):
        """测试 PPT 大纲生成"""
        papers = [
            {'title': 'Paper 1', 'method': 'Method 1', 'conclusion': 'Conclusion 1'}
        ]
        experiment = {
            'title': 'Test Exp',
            'purpose': 'Test',
            'method': 'Test',
            'results': 'Test'
        }
        
        outline = self.outliner.generate(papers, experiment)
        
        self.assertIn('slides', outline)
        self.assertGreater(len(outline['slides']), 0)


class TestLabLogAssistant(unittest.TestCase):
    """实验日志助手测试"""
    
    def setUp(self):
        """测试前准备"""
        self.assistant = LabLogAssistant()
    
    def test_generate_log(self):
        """测试实验日志生成"""
        experiment_data = {
            'title': 'Test Experiment',
            'purpose': 'Test Purpose',
            'method': 'Test Method',
            'results': 'Test Results',
            'conclusion': 'Test Conclusion'
        }
        
        log = self.assistant.generate(experiment_data)
        
        self.assertIn('实验报告', log)
        self.assertIn('Test Experiment', log)


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 添加测试
    suite.addTests(loader.loadTestsFromTestCase(TestKnowledgeGraph))
    suite.addTests(loader.loadTestsFromTestCase(TestSmartRecommender))
    suite.addTests(loader.loadTestsFromTestCase(TestReferenceFormatter))
    suite.addTests(loader.loadTestsFromTestCase(TestPPTOutliner))
    suite.addTests(loader.loadTestsFromTestCase(TestLabLogAssistant))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回结果
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
