#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
科研知识图谱模块
Knowledge Graph - 构建"问题 - 方法 - 结论"知识网络

这是学术龙虾的独家核心功能，市面上没有同类产品。
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class KnowledgeGraph:
    """科研知识图谱"""
    
    def __init__(self, db_path: str = "~/.academic_lobster/knowledge_graph.json"):
        """
        初始化知识图谱
        
        Args:
            db_path: 数据存储路径
        """
        self.db_path = Path(db_path).expanduser()
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.graph = self._load_graph()
    
    def _load_graph(self) -> Dict:
        """加载图谱数据"""
        if self.db_path.exists():
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'nodes': [],  # 节点：论文、实验、问题、方法
            'edges': [],  # 边：关联关系
            'metadata': {
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
        }
    
    def _save_graph(self):
        """保存图谱数据"""
        self.graph['metadata']['updated_at'] = datetime.now().isoformat()
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.graph, f, ensure_ascii=False, indent=2)
    
    def add_paper(self, paper: Dict) -> str:
        """
        添加论文节点（带重复检查）
        
        Args:
            paper: 论文信息
                {
                    'id': 'paper_001',
                    'title': 'Deep Residual Learning...',
                    'authors': ['He K', ...],
                    'year': 2016,
                    'research_question': '深层网络训练退化问题',
                    'method': '残差连接',
                    'conclusion': '可训练 152 层网络',
                    'keywords': ['深度学习', '残差学习', ...],
                    'category': '计算机视觉'
                }
        
        Returns:
            节点 ID 或已存在的 ID
        """
        # 检查是否已存在相同标题的论文（去重）
        title = paper.get('title', '').strip()
        for existing_node in self.graph['nodes']:
            if existing_node['type'] == 'paper':
                existing_title = existing_node['data'].get('title', '').strip()
                if existing_title == title:
                    # 发现重复，返回已存在的 ID
                    return existing_node['id']
        
        node_id = paper.get('id', f"paper_{len(self.graph['nodes']) + 1}")
        
        node = {
            'id': node_id,
            'type': 'paper',
            'data': paper
        }
        
        self.graph['nodes'].append(node)
        self._save_graph()
        
        # 自动建立关联
        self._auto_link(node)
        
        return node_id
    
    def add_experiment(self, experiment: Dict) -> str:
        """
        添加实验节点（带重复检查）
        
        Args:
            experiment: 实验信息
                {
                    'id': 'exp_001',
                    'date': '2026-03-10',
                    'purpose': '探究温度对收率的影响',
                    'method': '控制变量法',
                    'result': '70°C 时收率最高 62%',
                    'conclusion': '最佳温度区间 65-75°C',
                    'related_papers': ['paper_001'],  # 关联的论文
                    'tags': ['温度优化', '反应工程']
                }
        
        Returns:
            节点 ID 或已存在的 ID
        """
        # 检查是否已存在相同目的的实验（去重）
        purpose = experiment.get('purpose', '').strip()
        for existing_node in self.graph['nodes']:
            if existing_node['type'] == 'experiment':
                existing_purpose = existing_node['data'].get('purpose', '').strip()
                if existing_purpose == purpose:
                    # 发现重复，返回已存在的 ID
                    return existing_node['id']
        
        node_id = experiment.get('id', f"exp_{len(self.graph['nodes']) + 1}")
        
        node = {
            'id': node_id,
            'type': 'experiment',
            'data': experiment
        }
        
        self.graph['nodes'].append(node)
        self._save_graph()
        
        # 自动建立关联
        self._auto_link(node)
        
        return node_id
    
    def _auto_link(self, new_node: Dict):
        """
        自动建立节点关联
        
        基于：
        - 共同关键词
        - 相似研究方法
        - 相同研究领域
        """
        new_data = new_node['data']
        new_keywords = set(new_data.get('keywords', []))
        new_method = new_data.get('method', '').lower()
        new_category = new_data.get('category', '')
        
        for existing_node in self.graph['nodes']:
            if existing_node['id'] == new_node['id']:
                continue
            
            existing_data = existing_node['data']
            existing_keywords = set(existing_data.get('keywords', []))
            existing_method = existing_data.get('method', '').lower()
            existing_category = existing_data.get('category', '')
            
            # 计算相似度
            keyword_overlap = len(new_keywords & existing_keywords)
            method_similar = new_method and existing_method and (
                new_method in existing_method or existing_method in new_method
            )
            same_category = new_category and new_category == existing_category
            
            # 如果相似度足够高，建立关联
            if keyword_overlap >= 2 or method_similar or same_category:
                edge = {
                    'source': new_node['id'],
                    'target': existing_node['id'],
                    'type': 'related',
                    'reason': self._get_link_reason(
                        keyword_overlap, method_similar, same_category
                    )
                }
                
                # 避免重复边
                if not self._edge_exists(edge):
                    self.graph['edges'].append(edge)
        
        self._save_graph()
    
    def _get_link_reason(self, keyword_overlap: int, method_similar: bool, same_category: bool) -> str:
        """获取关联原因"""
        reasons = []
        if keyword_overlap >= 2:
            reasons.append(f"{keyword_overlap} 个共同关键词")
        if method_similar:
            reasons.append("相似研究方法")
        if same_category:
            reasons.append("相同学科领域")
        return "，".join(reasons)
    
    def _edge_exists(self, edge: Dict) -> bool:
        """检查边是否已存在"""
        for e in self.graph['edges']:
            if (e['source'] == edge['source'] and e['target'] == edge['target']) or \
               (e['source'] == edge['target'] and e['target'] == edge['source']):
                return True
        return False
    
    def get_related_papers(self, experiment_id: str) -> List[Dict]:
        """
        获取与实验相关的论文
        
        Args:
            experiment_id: 实验 ID
        
        Returns:
            相关论文列表
        """
        related = []
        
        # 查找关联边
        for edge in self.graph['edges']:
            if edge['source'] == experiment_id:
                related.append(edge['target'])
            elif edge['target'] == experiment_id:
                related.append(edge['source'])
        
        # 获取论文节点
        papers = []
        for node in self.graph['nodes']:
            if node['id'] in related and node['type'] == 'paper':
                papers.append(node['data'])
        
        return papers
    
    def get_knowledge_map(self, category: Optional[str] = None) -> Dict:
        """
        生成领域知识地图
        
        Args:
            category: 学科分类，None 表示全部
        
        Returns:
            知识地图（树状结构）
        """
        # 按研究问题分组
        question_groups = {}
        
        for node in self.graph['nodes']:
            if node['type'] != 'paper':
                continue
            
            if category and node['data'].get('category') != category:
                continue
            
            question = node['data'].get('research_question', '未知问题')
            
            if question not in question_groups:
                question_groups[question] = {
                    'question': question,
                    'methods': {}
                }
            
            method = node['data'].get('method', '未知方法')
            if method not in question_groups[question]['methods']:
                question_groups[question]['methods'][method] = []
            
            question_groups[question]['methods'][method].append({
                'title': node['data'].get('title'),
                'year': node['data'].get('year'),
                'conclusion': node['data'].get('conclusion')
            })
        
        return {
            'total_papers': len([n for n in self.graph['nodes'] if n['type'] == 'paper']),
            'total_experiments': len([n for n in self.graph['nodes'] if n['type'] == 'experiment']),
            'knowledge_tree': question_groups
        }
    
    def get_statistics(self) -> Dict:
        """获取图谱统计信息"""
        papers = [n for n in self.graph['nodes'] if n['type'] == 'paper']
        experiments = [n for n in self.graph['nodes'] if n['type'] == 'experiment']
        
        return {
            'total_nodes': len(self.graph['nodes']),
            'total_edges': len(self.graph['edges']),
            'papers': len(papers),
            'experiments': len(experiments),
            'categories': list(set(p['data'].get('category', '其他') for p in papers)),
            'keywords': self._get_top_keywords(10)
        }
    
    def _get_top_keywords(self, top_n: int) -> List[Dict]:
        """获取高频关键词"""
        keyword_count = {}
        
        for node in self.graph['nodes']:
            for kw in node['data'].get('keywords', []):
                keyword_count[kw] = keyword_count.get(kw, 0) + 1
        
        sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
        return [{'keyword': k, 'count': c} for k, c in sorted_keywords[:top_n]]
    
    def export_to_text(self) -> str:
        """导出为文本格式的知识地图"""
        stats = self.get_statistics()
        knowledge_map = self.get_knowledge_map()
        
        text = "🦞 学术龙虾 · 科研知识图谱\n"
        text += "=" * 60 + "\n\n"
        
        text += f"📊 统计信息\n"
        text += f"   论文数量：{stats['papers']}\n"
        text += f"   实验数量：{stats['experiments']}\n"
        text += f"   关联关系：{stats['total_edges']}\n"
        text += f"   涉及领域：{', '.join(stats['categories'])}\n\n"
        
        text += f"🔑 高频关键词\n"
        for kw in stats['keywords']:
            text += f"   • {kw['keyword']} ({kw['count']}次)\n"
        text += "\n"
        
        text += f"🌳 知识树\n"
        for question, data in knowledge_map['knowledge_tree'].items():
            text += f"\n【研究问题】{question}\n"
            for method, papers in data['methods'].items():
                text += f"  └─【方法】{method}\n"
                for p in papers:
                    text += f"      • {p['title']} ({p['year']})\n"
                    if p['conclusion']:
                        text += f"        → {p['conclusion']}\n"
        
        return text


# 测试代码
if __name__ == '__main__':
    kg = KnowledgeGraph()
    
    # 添加示例论文
    kg.add_paper({
        'id': 'paper_001',
        'title': 'Deep Residual Learning for Image Recognition',
        'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
        'year': 2016,
        'research_question': '深层网络训练退化问题',
        'method': '残差连接',
        'conclusion': '可训练 152 层网络',
        'keywords': ['深度学习', '残差学习', '图像识别', 'CNN'],
        'category': '计算机视觉'
    })
    
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
    
    # 添加示例实验
    kg.add_experiment({
        'id': 'exp_001',
        'date': '2026-03-10',
        'purpose': '改进 ResNet 残差块',
        'method': '引入注意力机制',
        'result': '准确率 87% → 89%',
        'conclusion': '注意力机制有效',
        'related_papers': ['paper_001', 'paper_002'],
        'tags': ['注意力机制', 'ResNet 改进']
    })
    
    # 输出知识地图
    print(kg.export_to_text())
    
    # 查询相关论文
    print("\n📚 与实验 exp_001 相关的论文：")
    for p in kg.get_related_papers('exp_001'):
        print(f"  • {p['title']}")
