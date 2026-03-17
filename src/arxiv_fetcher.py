"""
arxiv_fetcher.py - arXiv 论文实时抓取模块

功能：
- 根据关键词搜索 arXiv 论文
- 获取经典高引用论文
- 获取最新发表论文
- 返回结构化论文数据
"""

import arxiv
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ArxivFetcher:
    """arXiv 论文抓取器"""
    
    def __init__(self, max_results: int = 10):
        """
        初始化抓取器
        
        Args:
            max_results: 每次搜索返回的最大结果数
        """
        self.max_results = max_results
        self.client = arxiv.Client()
    
    def search_by_keywords(self, keywords: str, max_results: int = None) -> List[Dict]:
        """
        根据关键词搜索论文
        
        Args:
            keywords: 搜索关键词（支持布尔逻辑）
            max_results: 返回结果数
            
        Returns:
            论文列表
        """
        if max_results is None:
            max_results = self.max_results
            
        try:
            # 构建搜索查询
            search = arxiv.Search(
                query=keywords,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.Relevance,
                sort_order=arxiv.SortOrder.Descending
            )
            
            papers = []
            for result in self.client.results(search):
                paper = self._parse_result(result)
                papers.append(paper)
            
            logger.info(f"搜索 '{keywords}' 找到 {len(papers)} 篇论文")
            return papers
            
        except Exception as e:
            logger.error(f"搜索失败：{e}")
            return []
    
    def get_classic_papers(self, keywords: str, max_results: int = 5) -> List[Dict]:
        """
        获取经典高引用论文（按引用数排序）
        
        Args:
            keywords: 搜索关键词
            max_results: 返回结果数
            
        Returns:
            经典论文列表
        """
        try:
            # arXiv 不直接提供引用数，我们按时间排序获取早期论文
            # 实际应用中可以集成 Semantic Scholar API 获取引用数
            search = arxiv.Search(
                query=keywords,
                max_results=max_results * 3,  # 多获取一些用于筛选
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Ascending  # 最早的论文
            )
            
            papers = []
            for result in self.client.results(search):
                # 筛选 2020 年之前的论文作为"经典"
                if result.published.year < 2020:
                    paper = self._parse_result(result)
                    paper['tag'] = '📜 经典奠基'
                    paper['tag_type'] = 'classic'
                    papers.append(paper)
                    
                    if len(papers) >= max_results:
                        break
            
            logger.info(f"找到 {len(papers)} 篇经典论文")
            return papers
            
        except Exception as e:
            logger.error(f"获取经典论文失败：{e}")
            return []
    
    def get_recent_papers(self, keywords: str, max_results: int = 5, months: int = 24) -> List[Dict]:
        """
        获取最新研究论文
        
        Args:
            keywords: 搜索关键词
            max_results: 返回结果数
            months: 时间范围（月）
            
        Returns:
            最新论文列表
        """
        try:
            # 计算时间范围
            cutoff_date = datetime.now() - timedelta(days=months * 30)
            
            search = arxiv.Search(
                query=keywords,
                max_results=max_results * 3,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending  # 最新的论文
            )
            
            papers = []
            for result in self.client.results(search):
                # 筛选最近发表的论文
                if result.published >= cutoff_date:
                    paper = self._parse_result(result)
                    paper['tag'] = '🆕 最新进展'
                    paper['tag_type'] = 'recent'
                    papers.append(paper)
                    
                    if len(papers) >= max_results:
                        break
            
            logger.info(f"找到 {len(papers)} 篇最新论文")
            return papers
            
        except Exception as e:
            logger.error(f"获取最新论文失败：{e}")
            return []
    
    def _parse_result(self, result: arxiv.Result) -> Dict:
        """
        解析 arXiv 结果
        
        Args:
            result: arXiv 搜索结果
            
        Returns:
            结构化论文数据
        """
        # 提取作者姓名
        authors = [author.name for author in result.authors]
        
        # 提取主分类
        categories = result.categories if result.categories else []
        primary_category = categories[0] if categories else 'Unknown'
        
        # 构建论文数据
        paper = {
            'title': result.title,
            'authors': authors,
            'year': result.published.year,
            'month': result.published.month,
            'published': result.published.strftime('%Y-%m-%d'),
            'arxiv_id': result.entry_id.split('/')[-1],
            'arxiv_url': result.entry_id,
            'pdf_url': result.pdf_url,
            'abstract': result.summary[:500] + '...' if len(result.summary) > 500 else result.summary,
            'categories': categories,
            'primary_category': primary_category,
            'method': self._extract_method(result),
            'research_question': self._extract_research_question(result),
            'source': 'arXiv 实时抓取'
        }
        
        return paper
    
    def _extract_method(self, result: arxiv.Result) -> str:
        """从摘要中提取方法关键词"""
        abstract_lower = result.summary.lower()
        
        methods = []
        method_keywords = {
            'transformer': 'Transformer 架构',
            'convolutional': '卷积神经网络',
            'attention': '注意力机制',
            'residual': '残差连接',
            'generative': '生成模型',
            'diffusion': '扩散模型',
            'contrastive': '对比学习',
            'self-supervised': '自监督学习',
            'reinforcement': '强化学习',
            'graph neural': '图神经网络',
        }
        
        for keyword, method_name in method_keywords.items():
            if keyword in abstract_lower:
                methods.append(method_name)
        
        return '; '.join(methods[:3]) if methods else '深度学习方法'
    
    def _extract_research_question(self, result: arxiv.Result) -> str:
        """从摘要中提取研究问题"""
        abstract_lower = result.summary.lower()
        
        # 常见问题关键词
        if 'classification' in abstract_lower:
            return '图像/文本分类问题'
        elif 'detection' in abstract_lower:
            return '目标检测问题'
        elif 'segmentation' in abstract_lower:
            return '图像分割问题'
        elif 'generation' in abstract_lower:
            return '内容生成问题'
        elif 'translation' in abstract_lower:
            return '翻译问题'
        elif 'representation' in abstract_lower:
            return '表征学习问题'
        elif 'optimization' in abstract_lower:
            return '优化问题'
        else:
            return '深度学习相关问题'
    
    def get_paper_details(self, arxiv_id: str) -> Optional[Dict]:
        """
        根据 arXiv ID 获取论文详情
        
        Args:
            arxiv_id: arXiv ID（如 1706.03762）
            
        Returns:
            论文详情
        """
        try:
            search = arxiv.Search(id_list=[arxiv_id])
            result = next(self.client.results(search))
            return self._parse_result(result)
        except Exception as e:
            logger.error(f"获取论文详情失败：{e}")
            return None


# 关键词映射（中文 -> arXiv 搜索词）
KEYWORD_MAP = {
    'transformer': 'transformer OR attention mechanism',
    '注意力': 'attention mechanism OR self-attention',
    '卷积': 'convolutional neural network OR CNN',
    'cnn': 'convolutional neural network',
    'resnet': 'residual learning OR resnet',
    '残差': 'residual learning OR residual network',
    '图像分类': 'image classification',
    '图像识别': 'image recognition',
    'bert': 'BERT OR bidirectional encoder representations',
    'nlp': 'natural language processing OR NLP',
    '语言模型': 'language model OR LM',
    '深度学习': 'deep learning',
    '机器学习': 'machine learning',
    '生成模型': 'generative model OR GAN OR diffusion',
    '扩散模型': 'diffusion model OR stable diffusion',
    '图神经网络': 'graph neural network OR GNN',
    '强化学习': 'reinforcement learning OR RL',
    '目标检测': 'object detection',
    '语义分割': 'semantic segmentation',
    '自监督': 'self-supervised learning',
    '对比学习': 'contrastive learning',
}


def translate_keywords(chinese_keywords: str) -> str:
    """
    将中文关键词翻译为 arXiv 搜索词
    
    Args:
        chinese_keywords: 中文关键词
        
    Returns:
        arXiv 搜索词
    """
    arxiv_keywords = []
    
    for cn, en in KEYWORD_MAP.items():
        if cn in chinese_keywords:
            arxiv_keywords.append(en)
    
    if arxiv_keywords:
        return ' OR '.join(arxiv_keywords)
    else:
        # 如果没有匹配，直接返回原文（可能是英文）
        return chinese_keywords


# 测试函数
if __name__ == '__main__':
    fetcher = ArxivFetcher()
    
    print("=== 测试 arXiv 实时抓取 ===\n")
    
    # 测试 1: Transformer 经典论文
    print("📜 获取 Transformer 经典论文...")
    classic = fetcher.get_classic_papers('transformer OR attention', max_results=3)
    for paper in classic:
        print(f"  [{paper['year']}] {paper['title'][:60]}...")
        print(f"    作者：{', '.join(paper['authors'][:3])}{'...' if len(paper['authors']) > 3 else ''}")
        print(f"    arXiv: {paper['arxiv_id']}")
        print()
    
    # 测试 2: 最新论文
    print("🆕 获取 Transformer 最新论文...")
    recent = fetcher.get_recent_papers('transformer OR vision transformer', max_results=3, months=12)
    for paper in recent:
        print(f"  [{paper['published']}] {paper['title'][:60]}...")
        print(f"    作者：{', '.join(paper['authors'][:3])}{'...' if len(paper['authors']) > 3 else ''}")
        print(f"    arXiv: {paper['arxiv_id']}")
        print()
    
    # 测试 3: 关键词翻译
    print("🔤 关键词翻译测试:")
    test_keywords = ['Transformer 注意力机制', 'CNN 图像分类', 'BERT NLP']
    for kw in test_keywords:
        translated = translate_keywords(kw)
        print(f"  {kw} -> {translated[:50]}...")
