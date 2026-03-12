#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术龙虾 Web 界面
Web Application - 基于 Flask 的浏览器界面
"""

import sys
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, render_template_string, request, jsonify
from summarizer import PaperSummarizer
from lab_log import LabLogAssistant
from ppt_outline import PPTOutliner
from reference_formatter import ReferenceFormatter

app = Flask(__name__)

# 初始化模块
summarizer = PaperSummarizer()
lab_log = LabLogAssistant()
ppt_outliner = PPTOutliner()
ref_formatter = ReferenceFormatter()

# HTML 模板
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🦞 学术龙虾 - 科研全流程 AI 助手</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { font-size: 1.2em; opacity: 0.9; }
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .tab-btn {
            flex: 1;
            min-width: 150px;
            padding: 15px 20px;
            border: none;
            background: rgba(255,255,255,0.2);
            color: white;
            font-size: 1em;
            cursor: pointer;
            border-radius: 10px 10px 0 0;
            transition: background 0.3s;
        }
        .tab-btn:hover { background: rgba(255,255,255,0.3); }
        .tab-btn.active { background: white; color: #667eea; }
        .tab-content {
            background: white;
            padding: 30px;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        .tab-pane { display: none; }
        .tab-pane.active { display: block; }
        .form-group { margin-bottom: 20px; }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }
        textarea, input[type="text"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            font-family: inherit;
        }
        textarea { min-height: 150px; resize: vertical; }
        button.action-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 1em;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button.action-btn:hover { transform: translateY(-2px); }
        .result {
            margin-top: 20px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        .result h3 { margin-bottom: 10px; color: #667eea; }
        .result pre {
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: inherit;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        .loading.active { display: block; }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .feature-icon { font-size: 2em; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🦞 学术龙虾 Academic Lobster</h1>
            <p>让每一位研究者，都拥有平等的科研智能支持</p>
        </div>
        
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('summarizer')">📚 文献摘要</button>
            <button class="tab-btn" onclick="switchTab('lablog')">📝 实验日志</button>
            <button class="tab-btn" onclick="switchTab('ppt')">📄 PPT 大纲</button>
            <button class="tab-btn" onclick="switchTab('reference')">📖 参考文献</button>
        </div>
        
        <div class="tab-content">
            <!-- 文献摘要 -->
            <div id="summarizer" class="tab-pane active">
                <h2>📚 文献智能摘要</h2>
                <p style="color: #666; margin-bottom: 20px;">上传论文 PDF，30 秒生成结构化摘要</p>
                <div class="form-group">
                    <label>论文标题或内容描述：</label>
                    <input type="text" id="summarizer-input" placeholder="例如：ResNet、Transformer、BERT...">
                </div>
                <button class="action-btn" onclick="runSummarizer()">生成摘要</button>
                <div class="loading" id="summarizer-loading">
                    <div class="spinner"></div>
                    <p>正在生成摘要...</p>
                </div>
                <div class="result" id="summarizer-result" style="display: none;"></div>
            </div>
            
            <!-- 实验日志 -->
            <div id="lablog" class="tab-pane">
                <h2>📝 实验日志助手</h2>
                <p style="color: #666; margin-bottom: 20px;">输入实验数据，自动生成规范报告</p>
                <div class="form-group">
                    <label>实验数据：</label>
                    <textarea id="lablog-input" placeholder="例如：温度 60°C/70°C/80°C，反应时间 2h，产物收率 45%/62%/38%"></textarea>
                </div>
                <button class="action-btn" onclick="runLabLog()">生成实验日报</button>
                <div class="loading" id="lablog-loading">
                    <div class="spinner"></div>
                    <p>正在生成报告...</p>
                </div>
                <div class="result" id="lablog-result" style="display: none;"></div>
            </div>
            
            <!-- PPT 大纲 -->
            <div id="ppt" class="tab-pane">
                <h2>📄 组会 PPT 大纲</h2>
                <p style="color: #666; margin-bottom: 20px;">输入研究进展，生成汇报结构</p>
                <div class="form-group">
                    <label>本周研究进展：</label>
                    <textarea id="ppt-input" placeholder="例如：本周完成了 ResNet-50 在自定义数据集上的迁移学习，准确率 87%，遇到小样本过拟合问题"></textarea>
                </div>
                <button class="action-btn" onclick="runPPT()">生成 PPT 大纲</button>
                <div class="loading" id="ppt-loading">
                    <div class="spinner"></div>
                    <p>正在生成大纲...</p>
                </div>
                <div class="result" id="ppt-result" style="display: none;"></div>
            </div>
            
            <!-- 参考文献 -->
            <div id="reference" class="tab-pane">
                <h2>📖 参考文献格式化</h2>
                <p style="color: #666; margin-bottom: 20px;">一键转换多种参考文献格式</p>
                <div class="form-group">
                    <label>参考文献：</label>
                    <textarea id="reference-input" placeholder="例如：He K, Zhang X, Ren S, Sun J. Deep Residual Learning for Image Recognition. CVPR 2016."></textarea>
                </div>
                <button class="action-btn" onclick="runReference()">格式化</button>
                <div class="loading" id="reference-loading">
                    <div class="spinner"></div>
                    <p>正在格式化...</p>
                </div>
                <div class="result" id="reference-result" style="display: none;"></div>
            </div>
        </div>
        
        <div class="feature-grid" style="margin-top: 30px;">
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>高效</h3>
                <p>文献摘要 30 秒完成</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3>安全</h3>
                <p>数据本地处理</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>精准</h3>
                <p>专业科研场景优化</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💰</div>
                <h3>免费</h3>
                <p>开源普惠科研</p>
            </div>
        </div>
    </div>
    
    <script>
        function switchTab(tabId) {
            // 隐藏所有标签页
            document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            
            // 显示选中的标签页
            document.getElementById(tabId).classList.add('active');
            event.target.classList.add('active');
        }
        
        async function apiCall(endpoint, data) {
            const response = await fetch('/api/' + endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        }
        
        function showResult(elementId, loadingId, content) {
            document.getElementById(loadingId).classList.remove('active');
            const resultEl = document.getElementById(elementId);
            resultEl.innerHTML = '<h3>结果</h3><pre>' + content + '</pre>';
            resultEl.style.display = 'block';
        }
        
        async function runSummarizer() {
            const input = document.getElementById('summarizer-input').value;
            if (!input) { alert('请输入论文标题或内容描述'); return; }
            
            document.getElementById('summarizer-loading').classList.add('active');
            const result = await apiCall('summarize', { text: input });
            showResult('summarizer-result', 'summarizer-loading', result.summary);
        }
        
        async function runLabLog() {
            const input = document.getElementById('lablog-input').value;
            if (!input) { alert('请输入实验数据'); return; }
            
            document.getElementById('lablog-loading').classList.add('active');
            const result = await apiCall('lablog', { data: input });
            showResult('lablog-result', 'lablog-loading', result.report);
        }
        
        async function runPPT() {
            const input = document.getElementById('ppt-input').value;
            if (!input) { alert('请输入研究进展'); return; }
            
            document.getElementById('ppt-loading').classList.add('active');
            const result = await apiCall('ppt', { progress: input });
            showResult('ppt-result', 'ppt-loading', result.outline);
        }
        
        async function runReference() {
            const input = document.getElementById('reference-input').value;
            if (!input) { alert('请输入参考文献'); return; }
            
            document.getElementById('reference-loading').classList.add('active');
            const result = await apiCall('reference', { reference: input });
            showResult('reference-result', 'reference-loading', result.formatted);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    data = request.json
    text = data.get('text', '')
    
    # 根据输入生成摘要
    summary_dict = summarizer.generate_summary(text)
    summary_text = f"""【研究问题】{summary_dict.get('research_question', 'N/A')}
【研究方法】{summary_dict.get('method', 'N/A')}
【核心结论】{summary_dict.get('conclusion', 'N/A')}
【创新点】{summary_dict.get('innovation', 'N/A')}
【关键词】{', '.join(summary_dict.get('keywords', []))}"""
    
    return jsonify({'summary': summary_text})

@app.route('/api/lablog', methods=['POST'])
def api_lablog():
    data = request.json
    raw_data = data.get('data', '')
    
    report = lab_log.generate_report(raw_data)
    return jsonify({'report': report})

@app.route('/api/ppt', methods=['POST'])
def api_ppt():
    data = request.json
    progress = data.get('progress', '')
    
    outline = ppt_outliner.generate(progress)
    outline_text = ""
    for slide in outline['slides']:
        outline_text += f"P{slide['page']} {slide['title']}\n"
        for point in slide['points']:
            outline_text += f"   • {point}\n"
        outline_text += "\n"
    
    return jsonify({'outline': outline_text})

@app.route('/api/reference', methods=['POST'])
def api_reference():
    data = request.json
    reference = data.get('reference', '')
    
    result = ref_formatter.format(reference)
    formatted = ""
    for fmt, text in result.items():
        formatted += f"【{fmt}】{text}\n\n"
    
    return jsonify({'formatted': formatted})

if __name__ == '__main__':
    print("\n🦞 学术龙虾 Web 界面启动中...\n")
    print("=" * 60)
    print("访问地址：http://localhost:5000")
    print("=" * 60)
    print("\n按 Ctrl+C 停止服务\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
