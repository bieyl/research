# 🚀 学术龙虾 v2 - 赛前优化建议

**评估时间：** 2026-03-12 23:10  
**优化目标：** 确保夺冠，提升用户体验和演示效果

---

## 一、高优先级优化（赛前必做）

### 1.1 演示视频录制 ⭐⭐⭐⭐⭐

**重要性：** 竞赛评分关键材料  
**时间：** 30 分钟

**录制脚本：**

```
0:00-0:30  开场介绍
           - 展示 Web 界面
           - 说明产品定位

0:30-1:30  功能 1：知识图谱
           - 添加 2 篇论文（ResNet、Transformer）
           - 添加 1 个实验
           - 展示树状视图

1:30-2:00  功能 2：智能推荐
           - 输入实验描述
           - 展示三轨制推荐结果
           - 说明经典/前沿/实时区别

2:00-2:30  功能 3：PPT 生成
           - 选择论文和实验
           - 一键生成 PPT 大纲
           - 展示讲稿

2:30-3:00  总结
           - 效率提升数据
           - GitHub 链接
           - 致谢
```

**录制工具：**
- OBS Studio（免费开源）
- 系统自带录屏（Win+G / Mac Shift+Cmd+5）

**上传平台：**
- Bilibili（推荐，国内访问快）
-  YouTube（备选）

---

### 1.2 项目海报制作 ⭐⭐⭐⭐⭐

**重要性：** 竞赛评分关键材料  
**时间：** 1 小时

**海报内容（基于 assets/poster.md）：**

```
主标题：🦞 学术龙虾 v2 - 科研知识大脑
副标题：课题组私有、本地优先、可落地的科研知识大脑

核心功能（6 个图标 + 文字）：
🌳 知识图谱 - 让知识产生连接
💡 智能推荐 - 三轨制推荐策略
⚡ 文献摘要 - 5 秒读懂论文
📊 实验日志 - 结构化记录
📊 PPT 大纲 - 一键生成
📝 参考文献 - 多格式支持

差异化优势（对比表格）：
功能 | 学术龙虾 | 竞品
知识图谱 | ✅ 独家 | ❌ 无
智能推荐 | ✅ 三轨制 | ❌ 单一
本地优先 | ✅ 安全 | ❌ 云端
中文优化 | ✅ GB/T 7714 | ⚠️ 插件

技术亮点：
- 12000+ 行代码
- 80%+ 测试覆盖
- Docker 一键部署
- arXiv 实时集成

参赛信息：
北纬·龙虾大赛（第一届）· 学术赛道
别云龙 · 北京中关村学院
GitHub: https://github.com/bieyl/research
```

**设计工具：**
- Canva（在线，模板多）
- 稿定设计（在线，中文友好）
- PowerPoint（简单快速）

**尺寸：** 1920x1080（16:9）或 A3

---

### 1.3 新手引导 ⭐⭐⭐⭐

**重要性：** 提升用户体验，降低演示门槛  
**时间：** 2 小时

**实现方案：**

```javascript
// 添加到 web_app_v3.py 的 HTML 模板中

// 首次访问时显示欢迎弹窗
function showWelcomeModal() {
    const html = `
        <div class="welcome-modal">
            <h2>🦞 欢迎使用学术龙虾 v2</h2>
            <p>您的科研知识大脑，让知识产生连接</p>
            
            <div class="feature-tour">
                <div class="step">
                    <h3>1️⃣ 添加论文</h3>
                    <p>输入论文标题、作者、研究问题等信息</p>
                </div>
                <div class="step">
                    <h3>2️⃣ 添加实验</h3>
                    <p>记录实验目的、方法、结果</p>
                </div>
                <div class="step">
                    <h3>3️⃣ 智能推荐</h3>
                    <p>获取经典 + 前沿 + 实时论文推荐</p>
                </div>
                <div class="step">
                    <h3>4️⃣ 生成 PPT</h3>
                    <p>一键生成组会汇报大纲</p>
                </div>
            </div>
            
            <button onclick="startDemo()">🎬 观看 3 分钟演示</button>
            <button onclick="closeModal()">我知道了</button>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', html);
}

// 检查是否首次访问
if (!localStorage.getItem('academic_lobster_welcome')) {
    showWelcomeModal();
    localStorage.setItem('academic_lobster_welcome', 'true');
}
```

---

## 二、中优先级优化（提升体验）

### 2.1 快捷键支持 ⭐⭐⭐

**重要性：** 提升高级用户效率  
**时间：** 1 小时

**快捷键列表：**

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Ctrl+N` | 新建论文 | 打开论文添加表单 |
| `Ctrl+E` | 新建实验 | 打开实验添加表单 |
| `Ctrl+R` | 智能推荐 | 打开推荐界面 |
| `Ctrl+P` | 生成 PPT | 打开 PPT 生成界面 |
| `Ctrl+K` | 搜索 | 全局搜索 |
| `Ctrl+H` | 帮助 | 显示快捷键列表 |
| `Esc` | 关闭 | 关闭弹窗/取消操作 |

**实现代码：**
```javascript
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey) {
        switch(e.key) {
            case 'n':
                e.preventDefault();
                showAddPaperModal();
                break;
            case 'e':
                e.preventDefault();
                showAddExperimentModal();
                break;
            case 'r':
                e.preventDefault();
                showRecommendModal();
                break;
            case 'p':
                e.preventDefault();
                showPPTModal();
                break;
        }
    }
});
```

---

### 2.2 数据导出功能 ⭐⭐⭐

**重要性：** 提升实用性，方便用户备份  
**时间：** 2 小时

**导出格式：**

1. **知识图谱导出（JSON）**
```json
{
  "export_date": "2026-03-12",
  "version": "2.0.0",
  "nodes": [...],
  "edges": [...]
}
```

2. **参考文献导出（BibTeX）**
```bibtex
@article{he2016deep,
  title={Deep Residual Learning for Image Recognition},
  author={He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian},
  journal={CVPR},
  year={2016}
}
```

3. **实验日志导出（PDF）**
- 使用 reportlab 库生成
- 包含实验报告完整内容

**API 端点：**
```python
@app.route('/api/export/graph', methods=['GET'])
def export_graph():
    data = kg.export_all()
    return jsonify(data)

@app.route('/api/export/references', methods=['POST'])
def export_references():
    papers = request.json['papers']
    format = request.json.get('format', 'bibtex')
    output = ref_formatter.export(papers, format)
    return output
```

---

### 2.3 示例数据一键加载 ⭐⭐⭐

**重要性：** 方便演示和新手体验  
**时间：** 1 小时

**实现方案：**
```python
@app.route('/api/demo/load', methods=['POST'])
def load_demo_data():
    """加载示例数据（10 篇经典论文 + 5 个实验）"""
    
    demo_papers = [
        {
            'title': 'Deep Residual Learning for Image Recognition',
            'authors': ['He K', 'Zhang X', 'Ren S', 'Sun J'],
            'year': 2016,
            'research_question': '深层网络训练退化问题',
            'method': '残差连接',
            'conclusion': '可训练 152 层网络',
            'keywords': ['深度学习', '残差学习', '图像分类']
        },
        # ... 更多论文
    ]
    
    demo_experiments = [
        {
            'title': 'ResNet-50 图像分类实验',
            'purpose': '验证残差连接有效性',
            'method': '使用 PyTorch 实现 ResNet-50',
            'results': 'Top-1 准确率 76.0%',
            'tags': ['ResNet', '图像分类']
        },
        # ... 更多实验
    ]
    
    # 添加到知识图谱
    for paper in demo_papers:
        kg.add_paper(paper)
    
    for exp in demo_experiments:
        kg.add_experiment(exp)
    
    return jsonify({'success': True, 'count': len(demo_papers) + len(demo_experiments)})
```

**前端按钮：**
```html
<button onclick="loadDemoData()">📦 加载示例数据</button>
```

---

## 三、代码优化建议

### 3.1 性能优化 ⭐⭐

**当前瓶颈：**
- 知识图谱查询：O(n) - 可接受（千级数据）
- 推荐算法：O(n²) - 可接受（千级数据）
- arXiv API：网络延迟 - 已加缓存

**优化建议：**

1. **添加数据库索引**
```python
# knowledge_graph.py
def _create_indexes(self):
    """创建索引加速查询"""
    # 按类型索引
    self.cursor.execute(
        'CREATE INDEX IF NOT EXISTS idx_type ON nodes(type)'
    )
    # 按标题索引
    self.cursor.execute(
        'CREATE INDEX IF NOT EXISTS idx_title ON nodes((data->>"title"))'
    )
```

2. **推荐结果缓存**
```python
# smart_recommend.py
from functools import lru_cache

@lru_cache(maxsize=100)
def recommend_papers_for_experiment(self, experiment_text, top_n=5):
    # 缓存推荐结果
    pass
```

---

### 3.2 错误处理优化 ⭐⭐

**当前状态：** 良好  
**改进建议：**

1. **统一错误响应格式**
```python
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        'success': False,
        'error': {
            'code': 'INTERNAL_ERROR',
            'message': str(e),
            'suggestion': '请重试或联系开发者'
        }
    }), 500
```

2. **arXiv API 降级**
```python
def fetch_with_fallback(keywords):
    try:
        return arxiv_fetcher.search(keywords)
    except Exception as e:
        logger.warning(f"arXiv API 失败：{e}")
        # 返回本地推荐
        return get_local_recommendations(keywords)
```

---

## 四、演示优化建议

### 4.1 路演脚本优化 ⭐⭐⭐⭐⭐

**30 秒开场（关键）：**

```
（痛点）
在座的评委老师可能都带过研究生。您有没有遇到过这种情况：
学生读了两年论文，但知识是碎片化的，
问他这个领域有哪些方法，他说不清楚。

（解决方案）
学术龙虾 v2 不是又一个文献管理工具，
而是科研知识的大脑。
它自动构建"问题→方法→论文→实验"知识树，
让实验和文献智能关联，一键生成组会 PPT 和讲稿。

（价值）
所有数据本地存储，安全可控；
联网爬取合规透明，尊重知识产权。
我们的愿景：让每一位研究者，都拥有平等的科研智能支持。
```

**5 分钟演示流程：**

| 时间 | 环节 | 操作 | 台词 |
|------|------|------|------|
| 0:00-0:30 | 开场 | 展示首页 | 痛点 + 定位 |
| 0:30-1:00 | 添加论文 | 输入 ResNet 论文 | "这是 2016 年的经典论文" |
| 1:00-1:30 | 添加实验 | 输入 ResNet 实验 | "基于这篇论文做实验" |
| 1:30-2:00 | 知识图谱 | 展示树状图 | "自动构建知识关联" |
| 2:00-2:30 | 智能推荐 | 输入新实验 | "推荐相关论文" |
| 2:30-3:00 | 三轨制 | 展示经典/前沿/实时 | "覆盖全领域" |
| 3:00-3:30 | PPT 生成 | 一键生成 | "10 分钟完成组会准备" |
| 3:30-4:00 | 参考文献 | 选择格式 | "支持 GB/T 7714" |
| 4:00-4:30 | 效率对比 | 展示数据 | "效率提升 10-15 倍" |
| 4:30-5:00 | 总结 | 展示 GitHub | "开源免费，欢迎使用" |

---

### 4.2 Q&A 准备 ⭐⭐⭐⭐

**预期问题：**

1. **Q: 和 Zotero/EndNote 有什么区别？**
   ```
   A: 核心区别有三点：
   1. 我们不是文献管理工具，而是知识大脑
   2. 独家知识树图谱，让知识产生连接
   3. 本地优先架构，数据不出实验室
   ```

2. **Q: arXiv 抓取是否合规？**
   ```
   A: 完全合规：
   1. 仅获取公开摘要，不爬取付费全文
   2. 明确标注来源，尊重知识产权
   3. 爬取内容仅用于临时推荐，用完即清理
   ```

3. **Q: 如何保证数据安全？**
   ```
   A: 三重保障：
   1. 本地存储，不上传云端
   2. 开源代码，可审计
   3. MIT 许可，透明使用
   ```

4. **Q: 技术壁垒是什么？**
   ```
   A: 三个独家：
   1. 知识树图谱（市面无同类）
   2. 三轨制推荐策略
   3. 实验 - 文献双向关联
   ```

---

## 五、优化优先级总结

| 优化项 | 优先级 | 时间 | 影响 |
|--------|--------|------|------|
| 演示视频 | ⭐⭐⭐⭐⭐ | 30 分钟 | 高 |
| 项目海报 | ⭐⭐⭐⭐⭐ | 1 小时 | 高 |
| 路演脚本 | ⭐⭐⭐⭐⭐ | 30 分钟 | 高 |
| Q&A 准备 | ⭐⭐⭐⭐ | 30 分钟 | 中 |
| 新手引导 | ⭐⭐⭐⭐ | 2 小时 | 中 |
| 示例数据 | ⭐⭐⭐ | 1 小时 | 中 |
| 快捷键 | ⭐⭐⭐ | 1 小时 | 低 |
| 数据导出 | ⭐⭐⭐ | 2 小时 | 低 |
| 性能优化 | ⭐⭐ | 2 小时 | 低 |

**建议顺序：**
1. 演示视频（必做）
2. 项目海报（必做）
3. 路演脚本（必做）
4. Q&A 准备（推荐）
5. 其他（可选）

---

## 六、最终检查清单

### 赛前检查（提交前）

- [ ] 演示视频已录制并上传
- [ ] 项目海报已制作并上传
- [ ] GitHub 仓库链接可访问
- [ ] 所有文档链接可访问
- [ ] 注册表单填写完整
- [ ] 参赛协议已勾选

### 演示准备（比赛当天）

- [ ] 离线演示环境准备（本地数据）
- [ ] 在线演示环境准备（arXiv API）
- [ ] 备用电脑/网络
- [ ] 路演脚本熟练
- [ ] Q&A 准备充分

### 技术保障

- [ ] Web 服务正常运行
- [ ] 所有功能测试通过
- [ ] 性能测试通过（千级数据）
- [ ] 错误处理完善

---

**🦞 学术龙虾 v2 - 夺冠准备就绪！**

**目标：中关村北纬龙虾大赛・学术赛道冠军！** 🏆
