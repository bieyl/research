#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 Web 界面 v2
集成知识图谱和智能推荐的核心功能
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, render_template_string, request, jsonify
from knowledge_graph import KnowledgeGraph
from smart_recommend import SmartRecommender
from summarizer import PaperSummarizer
from lab_log import LabLogAssistant
from ppt_outline import PPTOutliner
from reference_formatter import ReferenceFormatter

app = Flask(__name__)

# 初始化模块
kg = KnowledgeGraph()
recommender = SmartRecommender()
summarizer = PaperSummarizer()
lab_log = LabLogAssistant()
ppt_outliner = PPTOutliner()
ref_formatter = ReferenceFormatter()

# 内存缓存（性能优化）
cache = {}

# HTML 模板 - 优化版
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🦞 学术龙虾 v2 - 科研知识大脑</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #fff;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        
        /* Header */
        .header {
            text-align: center;
            padding: 30px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 30px;
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .header p { color: #888; font-size: 1.1em; }
        
        /* Stats Bar */
        .stats-bar {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .stat-value { font-size: 2em; font-weight: bold; color: #667eea; }
        .stat-label { color: #888; margin-top: 5px; }
        
        /* Main Grid */
        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }
        @media (max-width: 1024px) { .main-grid { grid-template-columns: 1fr; } }
        
        /* Panels */
        .panel {
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 25px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .panel h2 { font-size: 1.5em; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
        
        /* Forms */
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; color: #ccc; }
        textarea, input[type="text"] {
            width: 100%;
            padding: 12px;
            background: rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 8px;
            color: #fff;
            font-size: 1em;
        }
        textarea:focus, input:focus { outline: none; border-color: #667eea; }
        
        /* Buttons */
        .btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            transition: transform 0.2s;
        }
        .btn:hover { transform: translateY(-2px); }
        .btn-secondary { background: rgba(255,255,255,0.1); }
        
        /* Results */
        .result-box {
            margin-top: 20px;
            padding: 15px;
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        /* Knowledge Graph Visualization */
        .kg-viz {
            margin-top: 20px;
            padding: 20px;
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
            min-height: 300px;
        }
        .kg-node {
            display: inline-block;
            padding: 8px 16px;
            margin: 5px;
            border-radius: 20px;
            font-size: 0.9em;
            cursor: pointer;
        }
        .kg-node.paper { background: rgba(102, 126, 234, 0.3); border: 1px solid #667eea; }
        .kg-node.experiment { background: rgba(118, 75, 162, 0.3); border: 1px solid #764ba2; }
        
        /* Recommendations */
        .rec-item {
            padding: 15px;
            margin: 10px 0;
            background: rgba(0,0,0,0.2);
            border-radius: 8px;
            border-left: 3px solid #667eea;
            transition: all 0.3s;
        }
        .rec-item:hover { transform: translateX(5px); }
        .rec-item.rec-classic { border-left-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
        .rec-item.rec-recent { border-left-color: #10b981; background: rgba(16, 185, 129, 0.1); }
        
        .rec-tag {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.85em;
            margin-bottom: 8px;
            font-weight: bold;
        }
        .rec-classic .rec-tag { background: rgba(245, 158, 11, 0.2); color: #f59e0b; }
        .rec-recent .rec-tag { background: rgba(16, 185, 129, 0.2); color: #10b981; }
        
        .rec-score { float: right; color: #667eea; font-weight: bold; }
        
        /* Loading */
        .loading { text-align: center; padding: 20px; color: #888; }
        .spinner {
            border: 3px solid rgba(255,255,255,0.1);
            border-top-color: #667eea;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        
        /* Tabs */
        .tabs { display: flex; gap: 10px; margin-bottom: 20px; }
        .tab { padding: 8px 16px; background: rgba(255,255,255,0.1); border-radius: 8px; cursor: pointer; }
        .tab.active { background: #667eea; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🦞 学术龙虾 v2</h1>
            <p>科研知识大脑 · 让知识产生连接</p>
        </div>
        
        <!-- 统计栏 -->
        <div class="stats-bar" id="stats-bar">
            <div class="stat-card">
                <div class="stat-value" id="stat-papers">0</div>
                <div class="stat-label">📚 论文</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="stat-experiments">0</div>
                <div class="stat-label">🧪 实验</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="stat-relations">0</div>
                <div class="stat-label">🔗 关联</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="stat-keywords">0</div>
                <div class="stat-label">🔑 关键词</div>
            </div>
        </div>
        
        <div class="main-grid">
            <!-- 左侧：知识图谱 -->
            <div class="panel">
                <h2>🌳 知识图谱</h2>
                <div class="tabs">
                    <div class="tab active" onclick="showKgView('tree')">树状视图</div>
                    <div class="tab" onclick="showKgView('network')">网络视图</div>
                </div>
                <button class="btn" onclick="loadKnowledgeGraph()">🔄 刷新图谱</button>
                <div class="kg-viz" id="kg-viz">
                    <div class="loading">点击"刷新图谱"加载知识地图</div>
                </div>
            </div>
            
            <!-- 右侧：智能录入 -->
            <div class="panel">
                <h2>✏️ 智能录入</h2>
                <div class="tabs">
                    <div class="tab active" onclick="showInputType('paper')">📄 论文</div>
                    <div class="tab" onclick="showInputType('experiment')">🧪 实验</div>
                </div>
                
                <!-- 论文录入 -->
                <div id="input-paper">
                    <div class="form-group">
                        <label>论文标题：</label>
                        <input type="text" id="paper-title" placeholder="例如：Deep Residual Learning for Image Recognition">
                    </div>
                    <div class="form-group">
                        <label>研究问题：</label>
                        <input type="text" id="paper-question" placeholder="例如：深层网络训练退化问题">
                    </div>
                    <div class="form-group">
                        <label>方法：</label>
                        <input type="text" id="paper-method" placeholder="例如：残差连接">
                    </div>
                    <div class="form-group">
                        <label>关键词（逗号分隔）：</label>
                        <input type="text" id="paper-keywords" placeholder="例如：深度学习，残差学习，图像识别">
                    </div>
                    <button class="btn" onclick="addPaper()">➕ 添加论文</button>
                </div>
                
                <!-- 实验录入 -->
                <div id="input-experiment" style="display:none;">
                    <div class="form-group">
                        <label>实验目的：</label>
                        <input type="text" id="exp-purpose" placeholder="例如：改进 ResNet 残差块">
                    </div>
                    <div class="form-group">
                        <label>实验方法：</label>
                        <input type="text" id="exp-method" placeholder="例如：引入注意力机制">
                    </div>
                    <div class="form-group">
                        <label>实验结果：</label>
                        <textarea id="exp-result" placeholder="例如：准确率从 87% 提升到 89%"></textarea>
                    </div>
                    <button class="btn" onclick="addExperiment()">➕ 添加实验</button>
                </div>
                
                <div id="add-result" class="result-box" style="display:none;"></div>
            </div>
        </div>
        
        <!-- 智能推荐 -->
        <div class="panel" style="margin-top: 30px;">
            <h2>💡 智能推荐</h2>
            <div class="form-group">
                <label>输入实验描述，自动推荐相关论文：</label>
                <textarea id="rec-input" placeholder="例如：使用 ResNet-50 进行图像分类，引入注意力机制，准确率提升 2%"></textarea>
            </div>
            <button class="btn" onclick="getRecommendations()">🔍 获取推荐</button>
            <div id="rec-result" class="result-box" style="display:none;"></div>
        </div>
        
        <!-- 快速工具 -->
        <div class="main-grid" style="margin-top: 30px;">
            <div class="panel">
                <h2>⚡ 文献摘要</h2>
                <div class="form-group">
                    <input type="text" id="sum-input" placeholder="输入论文标题，如 ResNet">
                </div>
                <button class="btn" onclick="runSummarize()">生成摘要</button>
                <div id="sum-result" class="result-box" style="display:none;"></div>
            </div>
            
            <div class="panel">
                <h2>⚡ 实验日志</h2>
                <div class="form-group">
                    <textarea id="log-input" placeholder="输入实验数据，如：温度 60/70/80 度，收率 45%/62%/38%"></textarea>
                </div>
                <button class="btn" onclick="runLabLog()">生成报告</button>
                <div id="log-result" class="result-box" style="display:none;"></div>
            </div>
        </div>
    </div>
    
    <script>
        let currentKgData = null;
        
        function showInputType(type) {
            document.querySelectorAll('#input-paper, #input-experiment').forEach(el => el.style.display = 'none');
            document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
            
            document.getElementById('input-' + type).style.display = 'block';
            event.target.classList.add('active');
        }
        
        function showKgView(view) {
            document.querySelectorAll('.panel .tab').forEach(el => el.classList.remove('active'));
            event.target.classList.add('active');
            if (currentKgData) renderKg(currentKgData, view);
        }
        
        async function loadKnowledgeGraph() {
            document.getElementById('kg-viz').innerHTML = '<div class="loading"><div class="spinner"></div>加载中...</div>';
            
            const response = await fetch('/api/kg');
            const data = await response.json();
            currentKgData = data;
            
            // 更新统计
            document.getElementById('stat-papers').textContent = data.stats.papers;
            document.getElementById('stat-experiments').textContent = data.stats.experiments;
            document.getElementById('stat-relations').textContent = data.stats.edges;
            document.getElementById('stat-keywords').textContent = data.stats.keywords.length;
            
            renderKg(data, 'tree');
        }
        
        function renderKg(data, view) {
            const viz = document.getElementById('kg-viz');
            
            if (view === 'tree') {
                let html = '<div style="font-family: monospace; white-space: pre-wrap; line-height: 1.8;">';
                
                for (const [question, qdata] of Object.entries(data.knowledge_tree)) {
                    html += `\\n📌 ${question}\\n`;
                    for (const [method, papers] of Object.entries(qdata.methods)) {
                        html += `  └─ 🔧 ${method}\\n`;
                        for (const p of papers) {
                            html += `      • 📄 ${p.title} (${p.year})\\n`;
                        }
                    }
                }
                
                html += '</div>';
                viz.innerHTML = html;
            } else {
                // 网络视图
                let html = '<div style="display: flex; flex-wrap: wrap; gap: 10px;">';
                
                for (const node of data.nodes) {
                    const type = node.type;
                    const title = node.data.title || node.data.purpose || '未知';
                    html += `<div class="kg-node ${type}" title="${title}">${title.substring(0, 20)}...</div>`;
                }
                
                html += '</div>';
                viz.innerHTML = html;
            }
        }
        
        async function addPaper() {
            const data = {
                title: document.getElementById('paper-title').value,
                question: document.getElementById('paper-question').value,
                method: document.getElementById('paper-method').value,
                keywords: document.getElementById('paper-keywords').value.split(',').map(k => k.trim())
            };
            
            const response = await fetch('/api/paper', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            document.getElementById('add-result').innerHTML = '✅ ' + result.message;
            document.getElementById('add-result').style.display = 'block';
            
            loadKnowledgeGraph();
        }
        
        async function addExperiment() {
            const data = {
                purpose: document.getElementById('exp-purpose').value,
                method: document.getElementById('exp-method').value,
                result: document.getElementById('exp-result').value
            };
            
            const response = await fetch('/api/experiment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            document.getElementById('add-result').innerHTML = '✅ ' + result.message;
            document.getElementById('add-result').style.display = 'block';
            
            loadKnowledgeGraph();
        }
        
        async function getRecommendations() {
            const input = document.getElementById('rec-input').value;
            if (!input) { alert('请输入实验描述'); return; }
            
            document.getElementById('rec-result').innerHTML = '<div class="loading"><div class="spinner"></div>分析中...</div>';
            document.getElementById('rec-result').style.display = 'block';
            
            const response = await fetch('/api/recommend', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: input })
            });
            
            const result = await response.json();
            
            if (!result.recommendations || result.recommendations.length === 0) {
                document.getElementById('rec-result').innerHTML = '<div class="result-box"><p>😕 未找到相关论文推荐</p><p style="color:#888;font-size:0.9em">建议：尝试使用更具体的关键词，如"ResNet"、"Transformer"、"注意力机制"、"图像分类"等</p></div>';
                return;
            }
            
            let html = '<h3>📚 推荐论文</h3>';
            let classicCount = 0;
            let recentCount = 0;
            
            for (const rec of result.recommendations) {
                const tag = rec.paper.tag || '';
                const tagClass = tag.includes('经典') ? 'rec-classic' : 'rec-recent';
                const tagEmoji = tag.includes('经典') ? '📜' : (tag.includes('最新') ? '🆕' : '📄');
                
                if (tag.includes('经典')) classicCount++;
                if (tag.includes('最新')) recentCount++;
                
                html += `<div class="rec-item ${tagClass}">
                    <div class="rec-tag">${tagEmoji} ${tag}</div>
                    <div class="rec-score">${rec.score.toFixed(0)}分 - ${rec.reason}</div>
                    <strong>${rec.paper.title}</strong><br>
                    <small>${rec.paper.authors?.join(', ') || 'Unknown'} (${rec.paper.year})</small><br>
                    <small>方法：${rec.paper.method || 'N/A'}</small>
                </div>`;
            }
            
            // 添加统计信息
            if (classicCount > 0 || recentCount > 0) {
                html = `<div style="margin-bottom:15px;padding:10px;background:rgba(0,0,0,0.2);border-radius:8px;">
                    <span style="margin-right:15px;">📜 经典论文：${classicCount}篇</span>
                    <span>🆕 最新研究：${recentCount}篇</span>
                </div>` + html;
            }
            
            document.getElementById('rec-result').innerHTML = html;
        }
        
        async function runSummarize() {
            const input = document.getElementById('sum-input').value;
            const result = await fetch('/api/summarize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: input })
            }).then(r => r.json());
            
            document.getElementById('sum-result').innerHTML = '<pre>' + result.summary + '</pre>';
            document.getElementById('sum-result').style.display = 'block';
        }
        
        async function runLabLog() {
            const input = document.getElementById('log-input').value;
            const result = await fetch('/api/lablog', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ data: input })
            }).then(r => r.json());
            
            document.getElementById('log-result').innerHTML = '<pre>' + result.report + '</pre>';
            document.getElementById('log-result').style.display = 'block';
        }
        
        // 页面加载时刷新图谱
        loadKnowledgeGraph();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/kg')
def api_kg():
    """获取知识图谱数据"""
    stats = kg.get_statistics()
    knowledge_map = kg.get_knowledge_map()
    
    return jsonify({
        'stats': stats,
        'knowledge_tree': knowledge_map['knowledge_tree'],
        'nodes': kg.graph['nodes'],
        'edges': kg.graph['edges']
    })

@app.route('/api/paper', methods=['POST'])
def api_add_paper():
    """添加论文"""
    data = request.json
    
    paper = {
        'id': f"paper_{len(kg.graph['nodes']) + 1}",
        'title': data.get('title', '未知标题'),
        'authors': ['Unknown'],
        'year': datetime.now().year,
        'research_question': data.get('question', ''),
        'method': data.get('method', ''),
        'conclusion': '',
        'keywords': data.get('keywords', []),
        'category': '计算机视觉'
    }
    
    existing_id = kg.add_paper(paper)
    
    # 检查是否是重复添加
    if existing_id != paper['id']:
        return jsonify({
            'message': f'ℹ️ 该论文已存在：{paper["title"]}',
            'id': existing_id,
            'duplicate': True
        })
    
    return jsonify({
        'message': f'✅ 论文已添加：{paper["title"]}',
        'id': paper['id'],
        'duplicate': False
    })

@app.route('/api/experiment', methods=['POST'])
def api_add_experiment():
    """添加实验"""
    data = request.json
    
    experiment = {
        'id': f"exp_{len(kg.graph['nodes']) + 1}",
        'date': datetime.now().strftime('%Y-%m-%d'),
        'purpose': data.get('purpose', ''),
        'method': data.get('method', ''),
        'result': data.get('result', ''),
        'conclusion': '',
        'tags': []
    }
    
    existing_id = kg.add_experiment(experiment)
    
    # 检查是否是重复添加
    if existing_id != experiment['id']:
        return jsonify({
            'message': f'ℹ️ 该实验已存在：{experiment["purpose"]}',
            'id': existing_id,
            'duplicate': True
        })
    
    return jsonify({
        'message': f'✅ 实验已添加：{experiment["purpose"]}',
        'id': experiment['id'],
        'duplicate': False
    })

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    """获取推荐 - 直接使用内存中的知识图谱数据"""
    data = request.json
    text = data.get('text', '')
    
    # 从内存知识图谱中获取论文
    papers = []
    for node in kg.graph.get('nodes', []):
        if node['type'] == 'paper':
            papers.append(node['data'])
    
    # 提取实验关键词
    exp_keywords = extract_keywords_from_text(text)
    
    # 计算每篇论文的相关性
    recommendations = []
    for paper in papers:
        score, reason = calculate_paper_similarity(exp_keywords, paper)
        if score > 0:
            recommendations.append({
                'paper': paper,
                'score': score,
                'reason': reason
            })
    
    # 按分数排序
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    
    # 如果没有找到相关论文，返回模拟推荐（演示用）
    if not recommendations:
        recommendations = get_demo_recommendations(text)
    
    return jsonify({
        'recommendations': recommendations[:5]
    })


def extract_keywords_from_text(text: str) -> list:
    """从文本提取关键词"""
    research_terms = [
        'ResNet', 'Transformer', 'BERT', 'CNN', 'RNN', 'LSTM', 'ViT',
        '注意力机制', '残差连接', '迁移学习', '数据增强', '图像分类',
        '准确率', '损失函数', '训练', '测试', '验证', '自注意力',
        '温度', '压力', '浓度', '时间', '收率', '效率', 'Vision'
    ]
    keywords = []
    for term in research_terms:
        if term in text:
            keywords.append(term)
    return keywords


def calculate_paper_similarity(keywords: list, paper: dict) -> tuple:
    """计算论文与实验的相似度"""
    score = 0.0
    reasons = []
    
    paper_keywords = paper.get('keywords', [])
    paper_method = paper.get('method', '')
    paper_question = paper.get('research_question', '')
    
    # 关键词匹配（最高 60 分）
    keyword_matches = set(keywords) & set(paper_keywords)
    if keyword_matches:
        score += min(60, len(keyword_matches) * 20)
        reasons.append(f"关键词匹配：{', '.join(keyword_matches)}")
    
    # 方法匹配（最高 25 分）
    for kw in keywords:
        if kw.lower() in paper_method.lower():
            score += 25
            reasons.append(f"方法相关：{kw}")
            break
    
    # 问题匹配（最高 15 分）
    for kw in keywords:
        if kw.lower() in paper_question.lower():
            score += 15
            reasons.append(f"研究问题相关")
            break
    
    return min(score, 100), '；'.join(reasons) if reasons else '弱相关'


def get_demo_recommendations(text: str) -> list:
    """
    返回演示推荐（当没有本地数据或匹配分数低时）
    
    推荐策略：经典奠基性论文 + 最新研究进展
    所有论文信息均基于真实发表的学术论文，年份为 arXiv 预印本或会议首次发表时间。
    """
    demo_papers = []
    text_lower = text.lower()
    
    # ========== Transformer / 注意力机制 ==========
    if 'transformer' in text_lower or 'attention' in text_lower or '注意力' in text or '自注意力' in text:
        # 📜 经典奠基性论文
        demo_papers.append({
            'paper': {
                'title': 'Attention Is All You Need',
                'authors': ['Vaswani A', 'Shazeer N', 'Parmar N', 'Uszkoreit J', 'Jones L', 'Gomez A N', 'Kaiser L', 'Polosukhin I'],
                'year': 2017,
                'method': 'Transformer 架构，自注意力机制',
                'research_question': '序列建模中的并行化问题',
                'tag': '📜 经典奠基'
            },
            'score': 98,
            'reason': 'Transformer 开山之作，注意力机制革命'
        })
        
        # 📜 经典：ResNet (CVPR 2016)
        demo_papers.append({
            'paper': {
                'title': 'Deep Residual Learning for Image Recognition',
                'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
                'year': 2016,
                'method': '残差连接',
                'research_question': '深层网络训练退化问题',
                'tag': '📜 经典奠基'
            },
            'score': 95,
            'reason': '深度学习里程碑，残差学习开创者'
        })
        
        # 🆕 最新研究：Swin Transformer (ICCV 2021)
        demo_papers.append({
            'paper': {
                'title': 'Swin Transformer: Hierarchical Vision Transformer using Shifted Windows',
                'authors': ['Liu Z', 'Lin Y', 'Cao Y', 'Hu H', 'Wei Y', 'Zhang Z', 'Lin S', 'Guo B'],
                'year': 2021,
                'method': '层次化 Transformer，移位窗口注意力',
                'research_question': '视觉 Transformer 的多尺度建模',
                'tag': '🆕 最新进展'
            },
            'score': 92,
            'reason': '视觉 SOTA，层次化 Transformer 架构'
        })
        
        # 🆕 最新研究：MAE (CVPR 2022)
        demo_papers.append({
            'paper': {
                'title': 'Masked Autoencoders Are Scalable Vision Learners',
                'authors': ['He K', 'Chen X', 'Xie S', 'Li Y', 'Dollár P', 'Girshick R'],
                'year': 2022,
                'method': '掩码自编码器，自监督学习',
                'research_question': 'Vision Transformer 的自监督预训练',
                'tag': '🆕 最新进展'
            },
            'score': 90,
            'reason': '自监督学习新范式，MAE 开创者'
        })
        
        # 🆕 最新研究：ViT (ICLR 2021)
        demo_papers.append({
            'paper': {
                'title': 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)',
                'authors': ['Dosovitskiy A', 'Beyer L', 'Kolesnikov A', 'Weissenborn D', 'Zhai X', 'Unterthiner T', 'Dehghani M', 'Minderer M', 'Heigold G', 'Gelly S', 'Uszkoreit J', 'Houlsby N'],
                'year': 2020,
                'method': '将 Transformer 应用于图像分类',
                'research_question': '图像分类中的 Transformer 应用',
                'tag': '🆕 最新进展'
            },
            'score': 88,
            'reason': 'Vision Transformer 开创性工作'
        })
    
    # ========== ResNet / 残差网络 ==========
    if 'resnet' in text_lower or 'residual' in text_lower or '残差' in text:
        # 📜 经典：ResNet
        demo_papers.append({
            'paper': {
                'title': 'Deep Residual Learning for Image Recognition',
                'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
                'year': 2016,
                'method': '残差连接',
                'research_question': '深层网络训练退化问题',
                'tag': '📜 经典奠基'
            },
            'score': 98,
            'reason': 'ResNet 开山之作，152 层网络训练突破'
        })
        
        # 📜 经典：Identity Mappings (ECCV 2016)
        demo_papers.append({
            'paper': {
                'title': 'Identity Mappings in Deep Residual Networks',
                'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
                'year': 2016,
                'method': '改进的残差连接（pre-activation）',
                'research_question': '深层网络训练退化问题',
                'tag': '📜 经典奠基'
            },
            'score': 92,
            'reason': 'ResNet 改进版，pre-activation 设计'
        })
        
        # 🆕 最新：Wide ResNet (BMVC 2016)
        demo_papers.append({
            'paper': {
                'title': 'Wide Residual Networks',
                'authors': ['Zagoruyko S', 'Komodakis N'],
                'year': 2016,
                'method': '宽残差网络',
                'research_question': '网络宽度 vs 深度的权衡',
                'tag': '🆕 最新进展'
            },
            'score': 88,
            'reason': '宽网络设计，性能超越深网络'
        })
        
        # 🆕 最新：ResNeXt (CVPR 2017)
        demo_papers.append({
            'paper': {
                'title': 'Aggregated Residual Transformations for Deep Neural Networks (ResNeXt)',
                'authors': ['Xie S', 'Girshick R', 'Dollár P', 'Tu Z', 'He K'],
                'year': 2017,
                'method': '分组卷积，基数（cardinality）',
                'research_question': 'ResNet 架构的扩展与改进',
                'tag': '🆕 最新进展'
            },
            'score': 86,
            'reason': 'ResNeXt 架构，分组残差块'
        })
    
    # ========== CNN / 卷积神经网络 / 图像分类 ==========
    if 'cnn' in text_lower or '卷积' in text_lower or '图像分类' in text or '图像识别' in text or '深度学习' in text:
        # 📜 经典：AlexNet (NIPS 2012)
        demo_papers.append({
            'paper': {
                'title': 'ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)',
                'authors': ['Krizhevsky A', 'Sutskever I', 'Hinton G E'],
                'year': 2012,
                'method': '卷积神经网络，ReLU，Dropout，数据增强',
                'research_question': 'ImageNet 大规模图像分类',
                'tag': '📜 经典奠基'
            },
            'score': 98,
            'reason': '深度学习革命开端，ImageNet 突破'
        })
        
        # 📜 经典：VGG (ICLR 2015)
        demo_papers.append({
            'paper': {
                'title': 'Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG)',
                'authors': ['Simonyan K', 'Zisserman A'],
                'year': 2015,
                'method': '深层卷积神经网络（16-19 层）',
                'research_question': '图像分类与目标检测',
                'tag': '📜 经典奠基'
            },
            'score': 95,
            'reason': 'VGG 架构，小卷积核深层网络'
        })
        
        # 📜 经典：ResNet (CVPR 2016)
        demo_papers.append({
            'paper': {
                'title': 'Deep Residual Learning for Image Recognition',
                'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
                'year': 2016,
                'method': '深度卷积神经网络，残差连接',
                'research_question': '深层网络训练退化问题',
                'tag': '📜 经典奠基'
            },
            'score': 92,
            'reason': 'ResNet，152 层网络训练突破'
        })
        
        # 🆕 最新：EfficientNet (ICML 2019)
        demo_papers.append({
            'paper': {
                'title': 'EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks',
                'authors': ['Tan M', 'Le Q V'],
                'year': 2019,
                'method': '复合缩放方法（深度/宽度/分辨率）',
                'research_question': 'CNN 模型的高效缩放策略',
                'tag': '🆕 最新进展'
            },
            'score': 90,
            'reason': 'EfficientNet，SOTA 效率与精度平衡'
        })
        
        # 🆕 最新：ConvNeXt (CVPR 2022)
        demo_papers.append({
            'paper': {
                'title': 'A ConvNet for the 2020s (ConvNeXt)',
                'authors': ['Liu Z', 'Mao H', 'Wu C Y', 'Feichtenhofer C', 'Darrell T', 'Xie S'],
                'year': 2022,
                'method': '现代化 CNN 架构设计',
                'research_question': 'CNN 与 Transformer 的架构对比',
                'tag': '🆕 最新进展'
            },
            'score': 88,
            'reason': 'ConvNeXt，现代化 CNN 设计'
        })
    
    # ========== 注意力机制（SENet 等） ==========
    if 'attention' in text_lower or '注意力' in text or '通道' in text:
        # 📜 经典：SENet (CVPR 2018)
        demo_papers.append({
            'paper': {
                'title': 'Squeeze-and-Excitation Networks (SENet)',
                'authors': ['Hu J', 'Shen L', 'Sun G'],
                'year': 2018,
                'method': '通道注意力机制',
                'research_question': '特征通道的自适应加权',
                'tag': '📜 经典奠基'
            },
            'score': 95,
            'reason': '通道注意力开创者，ImageNet 2017 冠军'
        })
        
        # 📜 经典：Attention Is All You Need (NeurIPS 2017)
        demo_papers.append({
            'paper': {
                'title': 'Attention Is All You Need',
                'authors': ['Vaswani A', 'Shazeer N', 'Parmar N', 'Uszkoreit J', 'Jones L', 'Gomez A N', 'Kaiser L', 'Polosukhin I'],
                'year': 2017,
                'method': 'Transformer 架构，自注意力机制',
                'research_question': '序列建模中的并行化问题',
                'tag': '📜 经典奠基'
            },
            'score': 92,
            'reason': '自注意力机制革命性论文'
        })
        
        # 🆕 最新：CBAM (ECCV 2018)
        demo_papers.append({
            'paper': {
                'title': 'CBAM: Convolutional Block Attention Module',
                'authors': ['Woo S', 'Park J', 'Lee J Y', 'Kweon I S'],
                'year': 2018,
                'method': '通道 + 空间双重注意力',
                'research_question': 'CNN 特征的多维度注意力增强',
                'tag': '🆕 最新进展'
            },
            'score': 88,
            'reason': 'CBAM，通道与空间注意力结合'
        })
        
        # 🆕 最新：Non-local (CVPR 2018)
        demo_papers.append({
            'paper': {
                'title': 'Non-local Neural Networks',
                'authors': ['Wang X', 'Girshick R', 'Gupta A', 'He K'],
                'year': 2018,
                'method': '非局部注意力，长距离依赖建模',
                'research_question': '视频与图像中的长距离依赖关系',
                'tag': '🆕 最新进展'
            },
            'score': 85,
            'reason': 'Non-local 注意力，长距离建模'
        })
    
    # ========== BERT / NLP ==========
    if 'bert' in text_lower or 'nlp' in text_lower or '语言模型' in text or '文本' in text:
        # 📜 经典：BERT (NAACL 2019)
        demo_papers.append({
            'paper': {
                'title': 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding',
                'authors': ['Devlin J', 'Chang M W', 'Lee K', 'Toutanova K'],
                'year': 2019,
                'method': '双向 Transformer 编码器，Masked LM',
                'research_question': '语言模型的预训练方法',
                'tag': '📜 经典奠基'
            },
            'score': 98,
            'reason': 'BERT 开创者，11 项 NLP 任务 SOTA'
        })
        
        # 📜 经典：Attention Is All You Need (NeurIPS 2017)
        demo_papers.append({
            'paper': {
                'title': 'Attention Is All You Need',
                'authors': ['Vaswani A', 'Shazeer N', 'Parmar N', 'Uszkoreit J', 'Jones L', 'Gomez A N', 'Kaiser L', 'Polosukhin I'],
                'year': 2017,
                'method': 'Transformer 架构，自注意力机制',
                'research_question': '序列建模中的并行化问题',
                'tag': '📜 经典奠基'
            },
            'score': 95,
            'reason': 'Transformer 开山之作，NLP 革命'
        })
        
        # 🆕 最新：RoBERTa (2019)
        demo_papers.append({
            'paper': {
                'title': 'RoBERTa: A Robustly Optimized BERT Pretraining Approach',
                'authors': ['Liu Y', 'Ott M', 'Goyal N', 'Du J', 'Joshi M', 'Chen D', 'Levy O', 'Lewis M', 'Zettlemoyer L', 'Stoyanov V'],
                'year': 2019,
                'method': '优化的 BERT 预训练策略',
                'research_question': 'BERT 预训练的改进与优化',
                'tag': '🆕 最新进展'
            },
            'score': 92,
            'reason': 'RoBERTa，BERT 优化版'
        })
        
        # 🆕 最新：GPT-3 (NeurIPS 2020)
        demo_papers.append({
            'paper': {
                'title': 'Language Models are Few-Shot Learners (GPT-3)',
                'authors': ['Brown T', 'Mann B', 'Ryder N', 'Subbiah M', 'Kaplan J', 'Dhariwal P', 'Neelakantan A', 'Shyam P', 'Sastry G', 'Askell A', 'Agarwal S', 'Herbert-Voss A', 'Krueger G', 'Henighan T', 'Child R', 'Ramesh A', 'Ziegler D', 'Wu J', 'Winter C', 'Hesse C', 'Chen M', 'Sigler E', 'Litwin M', 'Gray S', 'Chess B', 'Clark J', 'Berner C', 'McCandlish S', 'Radford A', 'Sutskever I', 'Amodei D'],
                'year': 2020,
                'method': '大规模语言模型，少样本学习',
                'research_question': '语言模型的少样本学习能力',
                'tag': '🆕 最新进展'
            },
            'score': 90,
            'reason': 'GPT-3，1750 亿参数语言模型'
        })
        
        # 🆕 最新：LLaMA (2023)
        demo_papers.append({
            'paper': {
                'title': 'LLaMA: Open and Efficient Foundation Language Models',
                'authors': ['Touvron H', 'Lavril T', 'Izacard G', 'Martinet X', 'Lachaux M A', 'Lacroix T', 'Rozière B', 'Goyal N', 'Hambro E', 'Azhar F', 'Rodriguez A', 'Joulin A', 'Grave E', 'Lample G'],
                'year': 2023,
                'method': '开源大语言模型',
                'research_question': '高效开源语言模型训练',
                'tag': '🆕 最新进展'
            },
            'score': 88,
            'reason': 'LLaMA，开源大模型代表'
        })
    
    # ========== 如果没有任何匹配，返回通用推荐 ==========
    if not demo_papers:
        # 📜 经典教材
        demo_papers.append({
            'paper': {
                'title': 'Deep Learning (MIT Press 专著)',
                'authors': ['Goodfellow I', 'Bengio Y', 'Courville A'],
                'year': 2016,
                'method': '深度学习基础理论（反向传播、CNN、RNN、优化方法）',
                'research_question': '深度学习系统性理论与方法',
                'tag': '📜 经典教材'
            },
            'score': 85,
            'reason': '深度学习圣经，Ian Goodfellow 经典教材'
        })
        # 🆕 现代教材
        demo_papers.append({
            'paper': {
                'title': 'Understanding Deep Learning',
                'authors': ['Prince S J D'],
                'year': 2023,
                'method': '深度学习现代方法（注意力机制、Transformer、生成模型）',
                'research_question': '深度学习全面教程与现代进展',
                'tag': '🆕 现代教材'
            },
            'score': 80,
            'reason': '现代深度学习教材，涵盖最新进展'
        })
        # 📜 经典：AlexNet
        demo_papers.append({
            'paper': {
                'title': 'ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)',
                'authors': ['Krizhevsky A', 'Sutskever I', 'Hinton G E'],
                'year': 2012,
                'method': '卷积神经网络，ReLU，Dropout',
                'research_question': 'ImageNet 大规模图像分类',
                'tag': '📜 经典奠基'
            },
            'score': 78,
            'reason': '深度学习革命开端'
        })
        # 📜 经典：ResNet
        demo_papers.append({
            'paper': {
                'title': 'Deep Residual Learning for Image Recognition',
                'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
                'year': 2016,
                'method': '残差连接',
                'research_question': '深层网络训练退化问题',
                'tag': '📜 经典奠基'
            },
            'score': 75,
            'reason': 'ResNet 开创性工作'
        })
    
    return demo_papers

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    """文献摘要"""
    data = request.json
    summary_dict = summarizer.generate_summary(data.get('text', ''))
    
    summary_text = f"""【研究问题】{summary_dict.get('research_question', 'N/A')}
【研究方法】{summary_dict.get('method', 'N/A')}
【核心结论】{summary_dict.get('conclusion', 'N/A')}
【创新点】{summary_dict.get('innovation', 'N/A')}
【关键词】{', '.join(summary_dict.get('keywords', []))}"""
    
    return jsonify({'summary': summary_text})

@app.route('/api/lablog', methods=['POST'])
def api_lablog():
    """实验日志"""
    data = request.json
    report = lab_log.generate_report(data.get('data', ''))
    return jsonify({'report': report})

if __name__ == '__main__':
    print("\n🦞 学术龙虾 v2 - 科研知识大脑\n")
    print("=" * 60)
    print("访问地址：http://localhost:5001")
    print("=" * 60)
    print("\n核心功能：")
    print("  🌳 知识图谱 - 构建科研知识网络")
    print("  💡 智能推荐 - 实验 - 文献自动关联")
    print("  ⚡ 快速工具 - 摘要、日志生成")
    print("\n按 Ctrl+C 停止服务\n")
    
    app.run(host='0.0.0.0', port=5001, debug=False)
