#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能推荐模块
Smart Recommender - 实验 - 文献智能关联推荐

这是学术龙虾的独家核心功能：
- 录入实验时，自动推荐相关论文
- 阅读论文时，自动推荐相关实验
- 写论文时，自动推荐支撑数据
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class SmartRecommender:
    """智能推荐引擎"""
    
    def __init__(self, kg_path: str = "~/.academic_lobster/knowledge_graph.json"):
        """
        初始化推荐引擎
        
        Args:
            kg_path: 知识图谱数据路径
        """
        self.kg_path = Path(kg_path).expanduser()
        self.kg = self._load_kg()
    
    def _load_kg(self) -> Dict:
        """加载知识图谱"""
        if self.kg_path.exists():
            with open(self.kg_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'nodes': [], 'edges': []}
    
    def recommend_papers_for_experiment(self, experiment_text: str, top_n: int = 5) -> List[Dict]:
        """
        为实验推荐相关论文
        
        Args:
            experiment_text: 实验描述文本
            top_n: 返回数量
        
        Returns:
            推荐论文列表
        """
        # 提取实验关键词
        exp_keywords = self._extract_keywords(experiment_text)
        
        scores = []
        
        for node in self.kg.get('nodes', []):
            if node['type'] != 'paper':
                continue
            
            paper = node['data']
            
            # 计算相似度分数
            score = self._calculate_similarity(
                exp_keywords,
                paper.get('keywords', []),
                paper.get('method', ''),
                paper.get('research_question', '')
            )
            
            if score > 0:
                scores.append({
                    'paper': paper,
                    'score': score,
                    'reason': self._get_recommend_reason(score, paper)
                })
        
        # 按分数排序
        scores.sort(key=lambda x: x['score'], reverse=True)
        
        return scores[:top_n]
    
    def recommend_experiments_for_paper(self, paper_keywords: List[str], top_n: int = 5) -> List[Dict]:
        """
        为论文推荐相关实验
        
        Args:
            paper_keywords: 论文关键词
            top_n: 返回数量
        
        Returns:
            推荐实验列表
        """
        scores = []
        
        for node in self.kg.get('nodes', []):
            if node['type'] != 'experiment':
                continue
            
            experiment = node['data']
            
            # 计算相似度分数
            score = self._calculate_similarity(
                paper_keywords,
                experiment.get('tags', []),
                experiment.get('method', ''),
                experiment.get('purpose', '')
            )
            
            if score > 0:
                scores.append({
                    'experiment': experiment,
                    'score': score,
                    'reason': self._get_recommend_reason(score, experiment)
                })
        
        scores.sort(key=lambda x: x['score'], reverse=True)
        
        return scores[:top_n]
    
    def _extract_keywords(self, text: str) -> List[str]:
        """
        从文本提取关键词
        
        简化实现：基于规则提取
        实际项目中应使用 NLP 模型
        """
        # 常见科研关键词
        research_terms = [
            'ResNet', 'Transformer', 'BERT', 'CNN', 'RNN', 'LSTM',
            '注意力机制', '残差连接', '迁移学习', '数据增强',
            '准确率', '损失函数', '训练', '测试', '验证',
            '温度', '压力', '浓度', '时间', '收率', '效率'
        ]
        
        keywords = []
        for term in research_terms:
            if term in text:
                keywords.append(term)
        
        return keywords
    
    def _calculate_similarity(
        self,
        query_keywords: List[str],
        target_keywords: List[str],
        target_method: str = '',
        target_description: str = ''
    ) -> float:
        """
        计算相似度分数
        
        Args:
            query_keywords: 查询关键词
            target_keywords: 目标关键词
            target_method: 目标方法描述
            target_description: 目标描述
        
        Returns:
            相似度分数 0-100
        """
        score = 0.0
        
        # 关键词匹配（最高 60 分）
        query_set = set(k.lower() for k in query_keywords)
        target_set = set(k.lower() for k in target_keywords)
        
        if query_set and target_set:
            overlap = len(query_set & target_set)
            total = len(query_set | target_set)
            if total > 0:
                score += (overlap / total) * 60
        
        # 方法匹配（最高 25 分）
        query_text = ' '.join(query_keywords).lower()
        if query_text and target_method:
            if query_text in target_method.lower() or target_method.lower() in query_text:
                score += 25
            elif any(k in target_method.lower() for k in query_keywords):
                score += 15
        
        # 描述匹配（最高 15 分）
        if query_text and target_description:
            if any(k in target_description.lower() for k in query_keywords):
                score += 15
        
        return min(score, 100)
    
    def _get_recommend_reason(self, score: float, item: Dict) -> str:
        """获取推荐理由"""
        if score >= 80:
            return "高度相关"
        elif score >= 60:
            return "中度相关"
        elif score >= 40:
            return "弱相关"
        else:
            return "可能相关"
    
    def generate_citation_suggestion(self, experiment_id: str) -> str:
        """
        生成论文引用建议
        
        Args:
            experiment_id: 实验 ID
        
        Returns:
            引用建议文本
        """
        # 获取相关论文
        related_papers = []
        
        for node in self.kg.get('nodes', []):
            if node['type'] == 'experiment' and node['id'] == experiment_id:
                # 找到实验节点
                experiment = node['data']
                related_paper_ids = experiment.get('related_papers', [])
                
                for paper_node in self.kg.get('nodes', []):
                    if paper_node['type'] == 'paper' and paper_node['id'] in related_paper_ids:
                        related_papers.append(paper_node['data'])
        
        if not related_papers:
            return "暂无关联论文，建议添加相关文献。"
        
        # 生成引用建议
        suggestion = "📚 建议在论文中引用以下文献支撑本实验：\n\n"
        
        for i, paper in enumerate(related_papers, 1):
            suggestion += f"[{i}] {paper.get('authors', ['Unknown'])[0]} et al. "
            suggestion += f"\"{paper.get('title')}\". "
            suggestion += f"{paper.get('year', 'N/A')}\n"
            
            # 添加关联说明
            if paper.get('method') and experiment.get('method'):
                suggestion += f"    关联点：本实验方法 \"{experiment.get('method')}\" "
                suggestion += f"基于该论文的 \"{paper.get('method')}\"\n"
        
        return suggestion


# 测试代码
if __name__ == '__main__':
    recommender = SmartRecommender()
    
    # 测试实验→论文推荐
    print("=" * 60)
    print("测试：为实验推荐论文")
    print("=" * 60)
    
    experiment_text = "使用 ResNet-50 进行图像分类，引入注意力机制，准确率提升 2%"
    
    recommendations = recommender.recommend_papers_for_experiment(experiment_text)
    
    print(f"\n实验描述：{experiment_text}\n")
    print("推荐论文：")
    
    for i, rec in enumerate(recommendations, 1):
        paper = rec['paper']
        print(f"\n{i}. {paper.get('title')}")
        print(f"   作者：{', '.join(paper.get('authors', []))}")
        print(f"   年份：{paper.get('year')}")
        print(f"   相关性：{rec['score']:.1f}分 - {rec['reason']}")
    
    # 测试论文→实验推荐
    print("\n" + "=" * 60)
    print("测试：为论文推荐实验")
    print("=" * 60)
    
    paper_keywords = ['ResNet', '注意力机制', '图像分类']
    
    recommendations = recommender.recommend_experiments_for_paper(paper_keywords)
    
    print(f"\n论文关键词：{', '.join(paper_keywords)}\n")
    print("相关实验：")
    
    for i, rec in enumerate(recommendations, 1):
        exp = rec['experiment']
        print(f"\n{i}. {exp.get('purpose')}")
        print(f"   日期：{exp.get('date')}")
        print(f"   结果：{exp.get('result')}")
        print(f"   相关性：{rec['score']:.1f}分 - {rec['reason']}")
