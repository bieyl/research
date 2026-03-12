#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 Web 界面 v3
- 集成 arXiv 实时论文抓取
- 高端学术风格 UI
- 经典 + 前沿 + 实时 三轨推荐
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
from arxiv_fetcher import ArxivFetcher, translate_keywords

app = Flask(__name__)

# 初始化模块
kg = KnowledgeGraph()
recommender = SmartRecommender()
summarizer = PaperSummarizer()
lab_log = LabLogAssistant()
ppt_outliner = PPTOutliner()
ref_formatter = ReferenceFormatter()
arxiv_fetcher = ArxivFetcher(max_results=5)

# 内存缓存
cache = {}

# ========== 高端学术风格 HTML 模板 ==========
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🦞 学术龙虾 v3 - 科研知识大脑</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --secondary: #8b5cf6;
            --accent: #06b6d4;
            --classic: #f59e0b;
            --recent: #10b981;
            --realtime: #ec4899;
            --bg-dark: #0f172a;
            --bg-card: #1e293b;
            --bg-hover: #334155;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --border: #334155;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.15);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.2);
            --radius: 12px;
            --radius-sm: 8px;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: linear-gradient(135deg, var(--bg-dark) 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
        }
        
        /* 背景装饰 */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
            position: relative;
            z-index: 1;
        }
        
        /* Header */
        .header {
            text-align: center;
            margin-bottom: 50px;
            padding: 40px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            border: 1px solid var(--border);
            border-radius: var(--radius);
            backdrop-filter: blur(10px);
            box-shadow: var(--shadow-lg);
        }
        
        .header h1 {
            font-size: 3em;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
            letter-spacing: -0.02em;
        }
        
        .header p {
            font-size: 1.2em;
            color: var(--text-secondary);
            font-weight: 300;
        }
        
        .header .version {
            display: inline-block;
            margin-top: 15px;
            padding: 6px 16px;
            background: rgba(99, 102, 241, 0.2);
            border: 1px solid var(--primary);
            border-radius: 20px;
            font-size: 0.85em;
            color: var(--primary);
            font-weight: 500;
        }
        
        /* Stats Bar */
        .stats-bar {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .stat-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 25px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
        }
        
        .stat-card:hover {
            transform: translateY(-4px);
            border-color: var(--primary);
            box-shadow: var(--shadow-lg);
        }
        
        .stat-value {
            font-size: 2.5em;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 5px;
        }
        
        .stat-label {
            color: var(--text-secondary);
            font-size: 0.95em;
            font-weight: 500;
        }
        
        /* Main Grid */
        .main-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        /* Card */
        .card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 30px;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
        }
        
        .card:hover {
            border-color: var(--border);
            box-shadow: var(--shadow-lg);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--border);
        }
        
        .card-icon {
            font-size: 1.8em;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.2));
            border-radius: var(--radius-sm);
        }
        
        .card-title {
            font-size: 1.4em;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .card-subtitle {
            font-size: 0.9em;
            color: var(--text-muted);
            margin-top: 4px;
        }
        
        /* Form Elements */
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
            color: var(--text-secondary);
            font-weight: 500;
            font-size: 0.95em;
        }
        
        textarea, input[type="text"] {
            width: 100%;
            padding: 14px 18px;
            background: var(--bg-dark);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            font-size: 1em;
            font-family: inherit;
            transition: all 0.3s ease;
        }
        
        textarea:focus, input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }
        
        textarea::placeholder, input::placeholder {
            color: var(--text-muted);
        }
        
        /* Buttons */
        .btn {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            font-size: 1em;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: var(--shadow);
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--border);
        }
        
        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.15);
        }
        
        .btn-group {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        
        /* Tabs */
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            background: var(--bg-dark);
            padding: 6px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
        }
        
        .tab {
            flex: 1;
            padding: 10px 20px;
            background: transparent;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            color: var(--text-secondary);
            font-weight: 500;
            transition: all 0.3s ease;
            font-size: 0.95em;
        }
        
        .tab:hover {
            background: rgba(255, 255, 255, 0.05);
        }
        
        .tab.active {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
        }
        
        /* Paper Cards */
        .paper-list {
            margin-top: 20px;
        }
        
        .paper-card {
            background: var(--bg-dark);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 20px;
            margin-bottom: 15px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .paper-card::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
        }
        
        .paper-card.classic::before {
            background: linear-gradient(180deg, var(--classic), #fbbf24);
        }
        
        .paper-card.recent::before {
            background: linear-gradient(180deg, var(--recent), #34d399);
        }
        
        .paper-card.realtime::before {
            background: linear-gradient(180deg, var(--realtime), #f472b6);
        }
        
        .paper-card:hover {
            border-color: var(--border);
            background: var(--bg-hover);
            transform: translateX(4px);
        }
        
        .paper-tag {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.8em;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .paper-tag.classic {
            background: rgba(245, 158, 11, 0.15);
            color: var(--classic);
        }
        
        .paper-tag.recent {
            background: rgba(16, 185, 129, 0.15);
            color: var(--recent);
        }
        
        .paper-tag.realtime {
            background: rgba(236, 72, 153, 0.15);
            color: var(--realtime);
        }
        
        .paper-title {
            font-size: 1.1em;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 10px;
            line-height: 1.5;
        }
        
        .paper-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            font-size: 0.9em;
            color: var(--text-secondary);
            margin-bottom: 10px;
        }
        
        .paper-meta span {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .paper-abstract {
            font-size: 0.9em;
            color: var(--text-muted);
            line-height: 1.7;
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid var(--border);
        }
        
        .paper-links {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        
        .paper-link {
            padding: 6px 14px;
            background: rgba(99, 102, 241, 0.15);
            color: var(--primary);
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.85em;
            font-weight: 500;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        
        .paper-link:hover {
            background: rgba(99, 102, 241, 0.25);
            color: var(--text-primary);
        }
        
        /* Stats Summary */
        .rec-summary {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 15px 20px;
            margin-bottom: 20px;
            display: flex;
            gap: 25px;
            flex-wrap: wrap;
        }
        
        .rec-summary-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.95em;
            color: var(--text-secondary);
        }
        
        .rec-summary-item strong {
            color: var(--text-primary);
        }
        
        /* Loading */
        .loading {
            text-align: center;
            padding: 40px;
            color: var(--text-muted);
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid rgba(99, 102, 241, 0.2);
            border-top-color: var(--primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        /* Knowledge Graph Viz */
        .kg-viz {
            margin-top: 20px;
            padding: 25px;
            background: var(--bg-dark);
            border-radius: var(--radius-sm);
            min-height: 350px;
            border: 1px solid var(--border);
        }
        
        .kg-tree {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9em;
            line-height: 2;
            color: var(--text-secondary);
        }
        
        .kg-tree .node {
            padding: 4px 12px;
            border-radius: 6px;
            display: inline-block;
            margin: 3px;
        }
        
        .kg-tree .paper-node {
            background: rgba(99, 102, 241, 0.15);
            color: var(--primary);
            border: 1px solid rgba(99, 102, 241, 0.3);
        }
        
        .kg-tree .exp-node {
            background: rgba(139, 92, 246, 0.15);
            color: var(--secondary);
            border: 1px solid rgba(139, 92, 246, 0.3);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header h1 { font-size: 2em; }
            .main-grid { grid-template-columns: 1fr; }
            .stats-bar { grid-template-columns: repeat(2, 1fr); }
            .rec-summary { flex-direction: column; gap: 10px; }
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.5s ease forwards;
        }
        
        /* Mode Toggle */
        .mode-toggle {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
            padding: 10px 15px;
            background: var(--bg-dark);
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
        }
        
        .mode-toggle label {
            margin: 0;
            font-size: 0.9em;
        }
        
        .mode-toggle select {
            padding: 8px 14px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 6px;
            color: var(--text-primary);
            font-size: 0.9em;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>🦞 学术龙虾 v3</h1>
            <p>科研知识大脑 · 让知识产生连接</p>
            <span class="version">✨ 实时论文抓取 · 高端学术风格</span>
        </div>
        
        <!-- Stats Bar -->
        <div class="stats-bar" id="stats-bar">
            <div class="stat-card">
                <div class="stat-value" id="stat-papers">0</div>
                <div class="stat-label">📚 本地论文</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="stat-experiments">0</div>
                <div class="stat-label">🧪 实验</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="stat-connections">0</div>
                <div class="stat-label">🔗 关联</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="stat-keywords">0</div>
                <div class="stat-label">🔑 关键词</div>
            </div>
        </div>
        
        <!-- Main Grid -->
        <div class="main-grid">
            <!-- Knowledge Graph -->
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">🌳</div>
                    <div>
                        <div class="card-title">知识图谱</div>
                        <div class="card-subtitle">构建科研知识网络</div>
                    </div>
                </div>
                
                <div class="tabs">
                    <button class="tab active" onclick="switchKgView('tree')">树状视图</button>
                    <button class="tab" onclick="switchKgView('network')">网络视图</button>
                </div>
                
                <div class="btn-group">
                    <button class="btn" onclick="refreshKG()">🔄 刷新图谱</button>
                    <button class="btn btn-secondary" onclick="clearKG()">🗑️ 清空</button>
                </div>
                
                <div class="kg-viz" id="kg-viz">
                    <div class="loading">暂无数据，请添加论文或实验</div>
                </div>
                
                <div class="btn-group" style="margin-top: 20px;">
                    <button class="btn btn-secondary" onclick="showAddPaperForm()">📄 添加论文</button>
                    <button class="btn btn-secondary" onclick="showAddExpForm()">🧪 添加实验</button>
                </div>
                
                <div id="add-form" style="margin-top: 20px; display: none;">
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
            </div>
            
            <!-- Smart Recommendation -->
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">💡</div>
                    <div>
                        <div class="card-title">智能推荐</div>
                        <div class="card-subtitle">实验 - 文献自动关联</div>
                    </div>
                </div>
                
                <div class="mode-toggle">
                    <label>推荐模式：</label>
                    <select id="rec-mode" onchange="updateRecMode()">
                        <option value="hybrid">🎯 混合模式（本地 + 实时）</option>
                        <option value="local">📚 仅本地演示</option>
                        <option value="realtime">🌐 仅 arXiv 实时</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>输入实验描述，自动推荐相关论文：</label>
                    <textarea id="rec-input" rows="3" placeholder="例如：使用 ResNet-50 进行图像分类，引入注意力机制，准确率提升 2%"></textarea>
                </div>
                
                <button class="btn" onclick="getRecommendations()">🔍 获取推荐</button>
                
                <div id="rec-result" class="paper-list"></div>
            </div>
            
            <!-- Literature Summary -->
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">⚡</div>
                    <div>
                        <div class="card-title">文献摘要</div>
                        <div class="card-subtitle">快速提取核心信息</div>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>输入论文标题或内容：</label>
                    <textarea id="sum-input" rows="3" placeholder="输入论文标题，如 ResNet，或粘贴论文内容"></textarea>
                </div>
                
                <button class="btn" onclick="runSummarize()">📝 生成摘要</button>
                
                <div id="sum-result" class="loading" style="display: none;"></div>
            </div>
            
            <!-- Lab Log -->
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">📊</div>
                    <div>
                        <div class="card-title">实验日志</div>
                        <div class="card-subtitle">自动生成实验报告</div>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>输入实验数据：</label>
                    <textarea id="log-input" rows="3" placeholder="例如：温度 60/70/80 度，收率 45%/62%/38%"></textarea>
                </div>
                
                <button class="btn" onclick="runLabLog()">📈 生成报告</button>
                
                <div id="log-result" class="loading" style="display: none;"></div>
            </div>
        </div>
    </div>
    
    <script>
        let currentKgView = 'tree';
        let recMode = 'hybrid';
        
        // 初始化
        document.addEventListener('DOMContentLoaded', function() {
            refreshKG();
            updateStats();
        });
        
        // 更新统计
        async function updateStats() {
            const stats = await fetch('/api/stats').then(r => r.json());
            document.getElementById('stat-papers').textContent = stats.papers || 0;
            document.getElementById('stat-experiments').textContent = stats.experiments || 0;
            document.getElementById('stat-connections').textContent = stats.connections || 0;
            document.getElementById('stat-keywords').textContent = stats.keywords || 0;
        }
        
        // 切换 KG 视图
        function switchKgView(view) {
            currentKgView = view;
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
            refreshKG();
        }
        
        // 刷新 KG
        async function refreshKG() {
            const data = await fetch('/api/kg').then(r => r.json());
            const viz = document.getElementById('kg-viz');
            
            if (!data.papers || data.papers.length === 0) {
                viz.innerHTML = '<div class="loading">暂无数据，请添加论文或实验</div>';
                return;
            }
            
            if (currentKgView === 'tree') {
                viz.innerHTML = renderTree(data);
            } else {
                viz.innerHTML = renderNetwork(data);
            }
        }
        
        // 渲染树状视图
        function renderTree(data) {
            let html = '<div class="kg-tree">';
            
            if (data.papers && data.papers.length > 0) {
                html += '<div>📚 <strong>论文库</strong></div>';
                data.papers.forEach((p, i) => {
                    html += `<div style="padding-left: 20px;">├─ <span class="node paper-node">${p.title?.substring(0, 40) || 'Unknown'} (${p.year || '?'})</span></div>`;
                });
            }
            
            if (data.experiments && data.experiments.length > 0) {
                html += '<div style="margin-top: 15px;">🧪 <strong>实验库</strong></div>';
                data.experiments.forEach((e, i) => {
                    html += `<div style="padding-left: 20px;">├─ <span class="node exp-node">${e.purpose?.substring(0, 40) || 'Unknown'}</span></div>`;
                });
            }
            
            html += '</div>';
            return html;
        }
        
        // 渲染网络视图（简化版）
        function renderNetwork(data) {
            let html = '<div class="kg-tree" style="text-align: center;">';
            html += '<div style="color: var(--text-muted); padding: 50px 0;">';
            html += '🕸️ 网络视图开发中...<br><br>';
            html += '<small>将展示论文与实验之间的关联关系</small>';
            html += '</div></div>';
            return html;
        }
        
        // 显示添加论文表单
        function showAddPaperForm() {
            document.getElementById('add-form').style.display = 'block';
        }
        
        // 显示添加实验表单
        function showAddExpForm() {
            alert('实验添加功能开发中...');
        }
        
        // 添加论文
        async function addPaper() {
            const title = document.getElementById('paper-title').value;
            const question = document.getElementById('paper-question').value;
            const method = document.getElementById('paper-method').value;
            const keywords = document.getElementById('paper-keywords').value;
            
            if (!title) { alert('请输入论文标题'); return; }
            
            await fetch('/api/kg/paper', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title, research_question: question, method, keywords: keywords.split(',').map(k => k.trim()) })
            });
            
            alert('✅ 论文已添加');
            document.getElementById('add-form').style.display = 'none';
            refreshKG();
            updateStats();
        }
        
        // 清空 KG
        function clearKG() {
            if (confirm('确定要清空所有数据吗？')) {
                localStorage.clear();
                refreshKG();
                updateStats();
            }
        }
        
        // 更新推荐模式
        function updateRecMode() {
            recMode = document.getElementById('rec-mode').value;
        }
        
        // 获取推荐
        async function getRecommendations() {
            const input = document.getElementById('rec-input').value;
            if (!input) { alert('请输入实验描述'); return; }
            
            document.getElementById('rec-result').innerHTML = '<div class="loading"><div class="spinner"></div>正在分析并搜索论文...</div>';
            
            const response = await fetch('/api/recommend', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: input, mode: recMode })
            });
            
            const result = await response.json();
            
            if (!result.recommendations || result.recommendations.length === 0) {
                document.getElementById('rec-result').innerHTML = '<div class="paper-card"><p>😕 未找到相关论文推荐</p><p style="color:var(--text-muted);font-size:0.9em">建议：尝试使用更具体的关键词，如"ResNet"、"Transformer"、"注意力机制"、"图像分类"等</p></div>';
                return;
            }
            
            // 统计
            let classicCount = result.recommendations.filter(r => r.paper.tag_type === 'classic').length;
            let recentCount = result.recommendations.filter(r => r.paper.tag_type === 'recent').length;
            let realtimeCount = result.recommendations.filter(r => r.paper.source === 'arXiv 实时抓取').length;
            
            let html = '<div class="rec-summary">';
            if (classicCount > 0) html += `<div class="rec-summary-item">📜 经典论文：<strong>${classicCount}篇</strong></div>`;
            if (recentCount > 0) html += `<div class="rec-summary-item">🆕 最新研究：<strong>${recentCount}篇</strong></div>`;
            if (realtimeCount > 0) html += `<div class="rec-summary-item">🌐 实时抓取：<strong>${realtimeCount}篇</strong></div>`;
            html += '</div>';
            
            // 渲染论文卡片
            for (const rec of result.recommendations) {
                const tagType = rec.paper.tag_type || 'recent';
                const tag = rec.paper.tag || '📄 论文';
                const isRealtime = rec.paper.source === 'arXiv 实时抓取';
                
                html += `<div class="paper-card ${tagType} fade-in">
                    <span class="paper-tag ${tagType}">${tag}${isRealtime ? ' · arXiv' : ''}</span>
                    <div class="paper-score" style="float: right; color: var(--primary); font-weight: 600;">${rec.score?.toFixed(0) || 0}分</div>
                    <div class="paper-title">${rec.paper.title}</div>
                    <div class="paper-meta">
                        <span>👥 ${rec.paper.authors?.slice(0, 3).join(', ') || 'Unknown'}${rec.paper.authors?.length > 3 ? '...' : ''}</span>
                        <span>📅 ${rec.paper.year || 'N/A'}${rec.paper.published ? ' · ' + rec.paper.published : ''}</span>
                        ${rec.paper.arxiv_id ? `<span>📄 arXiv:${rec.paper.arxiv_id}</span>` : ''}
                    </div>
                    ${rec.paper.method ? `<div style="margin-top: 8px; font-size: 0.9em; color: var(--text-secondary);">🔧 方法：${rec.paper.method}</div>` : ''}
                    ${rec.paper.abstract ? `<div class="paper-abstract">${rec.paper.abstract}</div>` : ''}
                    <div class="paper-links">
                        ${rec.paper.pdf_url ? `<a href="${rec.paper.pdf_url}" target="_blank" class="paper-link">📄 PDF</a>` : ''}
                        ${rec.paper.arxiv_url ? `<a href="${rec.paper.arxiv_url}" target="_blank" class="paper-link">🔗 arXiv</a>` : ''}
                        ${rec.reason ? `<span class="paper-link" style="cursor: default;">💡 ${rec.reason}</span>` : ''}
                    </div>
                </div>`;
            }
            
            document.getElementById('rec-result').innerHTML = html;
        }
        
        // 生成摘要
        async function runSummarize() {
            const input = document.getElementById('sum-input').value;
            if (!input) { alert('请输入内容'); return; }
            
            document.getElementById('sum-result').style.display = 'block';
            document.getElementById('sum-result').innerHTML = '<div class="loading"><div class="spinner"></div>生成中...</div>';
            
            const result = await fetch('/api/summarize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: input })
            }).then(r => r.json());
            
            document.getElementById('sum-result').innerHTML = '<div class="paper-card"><pre style="white-space: pre-wrap; font-family: inherit; line-height: 1.8;">' + result.summary + '</pre></div>';
        }
        
        // 生成实验日志
        async function runLabLog() {
            const input = document.getElementById('log-input').value;
            if (!input) { alert('请输入实验数据'); return; }
            
            document.getElementById('log-result').style.display = 'block';
            document.getElementById('log-result').innerHTML = '<div class="loading"><div class="spinner"></div>生成中...</div>';
            
            const result = await fetch('/api/lablog', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: input })
            }).then(r => r.json());
            
            document.getElementById('log-result').innerHTML = '<div class="paper-card"><pre style="white-space: pre-wrap; font-family: inherit; line-height: 1.8;">' + result.report + '</pre></div>';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """主页"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/stats')
def api_stats():
    """获取统计信息"""
    stats = kg.get_statistics()
    return jsonify({
        'papers': stats.get('total_papers', 0),
        'experiments': stats.get('total_experiments', 0),
        'connections': stats.get('total_connections', 0),
        'keywords': stats.get('total_keywords', 0)
    })

@app.route('/api/kg')
def api_kg():
    """获取知识图谱数据"""
    km = kg.get_knowledge_map()
    return jsonify({
        'papers': km.get('papers', []),
        'experiments': km.get('experiments', []),
        'connections': km.get('connections', [])
    })

@app.route('/api/kg/paper', methods=['POST'])
def api_add_paper():
    """添加论文"""
    data = request.json
    paper_id = kg.add_paper(
        title=data.get('title', ''),
        year=data.get('year'),
        authors=data.get('authors', []),
        method=data.get('method', ''),
        research_question=data.get('research_question', ''),
        keywords=data.get('keywords', [])
    )
    return jsonify({'paper_id': paper_id, 'success': True})

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    """
    智能推荐 API
    
    支持三种模式：
    - hybrid: 混合模式（本地演示 + arXiv 实时）
    - local: 仅本地演示
    - realtime: 仅 arXiv 实时
    """
    data = request.json
    text = data.get('text', '')
    mode = data.get('mode', 'hybrid')
    
    if not text:
        return jsonify({'error': '请输入实验描述'}), 400
    
    recommendations = []
    
    # 模式 1: 混合模式
    if mode == 'hybrid':
        # 获取本地推荐
        local_recs = recommender.recommend_papers_for_experiment(text, top_n=3)
        for rec in local_recs:
            # 转换格式
            paper_data = rec.get('paper', {})
            if not paper_data and 'title' in rec:
                paper_data = rec
            paper_data['tag_type'] = 'classic' if paper_data.get('year', 2023) < 2020 else 'recent'
            recommendations.append({
                'paper': paper_data,
                'score': rec.get('score', 85),
                'reason': rec.get('reason', '本地推荐')
            })
        
        # 获取 arXiv 实时推荐
        try:
            arxiv_keywords = translate_keywords(text)
            classic_papers = arxiv_fetcher.get_classic_papers(arxiv_keywords, max_results=2)
            recent_papers = arxiv_fetcher.get_recent_papers(arxiv_keywords, max_results=3)
            
            for paper in classic_papers:
                recommendations.append({
                    'paper': paper,
                    'score': 90,
                    'reason': 'arXiv 经典高引论文'
                })
            
            for paper in recent_papers:
                recommendations.append({
                    'paper': paper,
                    'score': 85,
                    'reason': 'arXiv 最新研究'
                })
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"arXiv 抓取失败：{e}")
    
    # 模式 2: 仅本地
    elif mode == 'local':
        local_recs = recommender.recommend_papers_for_experiment(text, top_n=5)
        for rec in local_recs:
            paper_data = rec.get('paper', {})
            if not paper_data and 'title' in rec:
                paper_data = rec
            paper_data['tag_type'] = 'classic' if paper_data.get('year', 2023) < 2020 else 'recent'
            recommendations.append({
                'paper': paper_data,
                'score': rec.get('score', 85),
                'reason': rec.get('reason', '本地推荐')
            })
    
    # 模式 3: 仅实时
    elif mode == 'realtime':
        try:
            arxiv_keywords = translate_keywords(text)
            classic_papers = arxiv_fetcher.get_classic_papers(arxiv_keywords, max_results=3)
            recent_papers = arxiv_fetcher.get_recent_papers(arxiv_keywords, max_results=5)
            
            for paper in classic_papers:
                recommendations.append({
                    'paper': paper,
                    'score': 90,
                    'reason': 'arXiv 经典高引论文'
                })
            
            for paper in recent_papers:
                recommendations.append({
                    'paper': paper,
                    'score': 85,
                    'reason': 'arXiv 最新研究'
                })
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"arXiv 抓取失败：{e}")
            return jsonify({'error': 'arXiv API 调用失败，请稍后重试'}), 500
    
    # 去重（按标题）
    seen_titles = set()
    unique_recs = []
    for rec in recommendations:
        title = rec['paper'].get('title', '')
        if title not in seen_titles:
            seen_titles.add(title)
            unique_recs.append(rec)
    
    # 按分数排序
    unique_recs.sort(key=lambda x: x['score'], reverse=True)
    
    return jsonify({'recommendations': unique_recs[:10]})

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
    report_dict = lab_log.generate_log(data.get('text', ''))
    
    report_text = f"""【实验目的】{report_dict.get('purpose', 'N/A')}
【实验条件】{report_dict.get('conditions', 'N/A')}
【实验结果】
{report_dict.get('results_table', 'N/A')}
【结果分析】{report_dict.get('analysis', 'N/A')}
【后续建议】{report_dict.get('recommendations', 'N/A')}"""
    
    return jsonify({'report': report_text})

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   🦞 学术龙虾 v3 - 科研知识大脑                           ║
║                                                           ║
║   ✨ 实时论文抓取 · 高端学术风格                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

访问地址：http://localhost:5001
访问地址：http://10.0.0.52:5001

核心功能:
  🌳 知识图谱 - 构建科研知识网络
  💡 智能推荐 - 本地 + arXiv 实时混合推荐
  ⚡ 快速工具 - 摘要、日志生成

按 Ctrl+C 停止服务
""")
    
    app.run(host='0.0.0.0', port=5001, debug=False)
