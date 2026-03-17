# 学术龙虾 v2 系统架构

本文档详细描述学术龙虾 v2 的系统架构设计、技术选型和核心模块。

---

## 📋 目录

- [系统概览](#系统概览)
- [架构设计原则](#架构设计原则)
- [技术栈](#技术栈)
- [核心模块](#核心模块)
- [数据流](#数据流)
- [安全设计](#安全设计)
- [部署架构](#部署架构)
- [扩展性设计](#扩展性设计)

---

## 系统概览

### 整体架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                        用户界面层 (Presentation Layer)           │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   Web UI        │   CLI Demo      │   Voice Interface           │
│   (Flask)       │   (Python)      │   (pygame + pyaudio)        │
└────────┬────────┴────────┬────────┴────────────┬────────────────┘
         │                 │                     │
         └─────────────────┼─────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                      业务逻辑层 (Business Logic Layer)           │
├─────────────────┬─────────────────┬─────────────────────────────┤
│  知识图谱引擎   │  智能推荐引擎   │   PPT 生成引擎               │
│  KnowledgeGraph │  Recommender    │   PPTGenerator              │
└────────┬────────┴────────┬────────┴────────────┬────────────────┘
         │                 │                     │
         └─────────────────┼─────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                        数据访问层 (Data Access Layer)            │
├─────────────────┬─────────────────┬─────────────────────────────┤
│  SQLite         │  File System    │   Web Crawler               │
│  (本地数据库)   │  (文献/实验)    │   (arXiv/PubMed/CNKI)       │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

---

## 架构设计原则

### 1. 本地优先 (Local-First)

**原则：** 所有用户数据默认存储在本地，不依赖云端服务。

**实现：**
- SQLite 本地数据库
- 文件系统存储文献和实验数据
- 可选的离线模式

**优势：**
- 数据隐私保护
- 无网络依赖
- 低延迟访问

### 2. 模块化设计 (Modular Design)

**原则：** 各功能模块独立，可单独测试和替换。

**实现：**
- 知识图谱、推荐、PPT 生成独立模块
- 清晰的接口定义
- 依赖注入

**优势：**
- 易于维护
- 便于扩展
- 降低耦合

### 3. 安全可控 (Security by Design)

**原则：** 从设计源头考虑安全性。

**实现：**
- 最小权限原则
- 数据加密存储
- 操作日志审计
- 网络请求白名单

**优势：**
- 防止数据泄露
- 可追溯审计
- 合规性保障

### 4. 可扩展性 (Extensibility)

**原则：** 支持未来功能扩展。

**实现：**
- 插件式架构
- 配置驱动
- API 接口标准化

**优势：**
- 易于添加新功能
- 支持第三方集成
- 适应不同场景

---

## 技术栈

### 核心技术

| 层级 | 技术 | 版本 | 用途 |
|------|------|------|------|
| **语言** | Python | 3.9+ | 主要编程语言 |
| **Web 框架** | Flask | 2.x | Web 界面服务器 |
| **数据库** | SQLite | 3.x | 本地数据存储 |
| **NLP** | jieba | 0.42+ | 中文分词 |
| **NLP** | textrank4zh | 0.3+ | 文本摘要和关键词提取 |
| **图算法** | NetworkX | 3.x | 知识图谱数据结构 |
| **UI** | HTML/CSS/JS | - | Web 界面 |
| **语音** | pygame | 2.x | 音频播放 |
| **语音** | pyaudio | 0.2+ | 音频录制 |

### 开发工具

| 工具 | 用途 |
|------|------|
| black | 代码格式化 |
| flake8 | 代码风格检查 |
| isort | import 排序 |
| mypy | 类型检查 |
| pytest | 单元测试 |
| coverage | 测试覆盖率 |

### 部署工具

| 工具 | 用途 |
|------|------|
| Docker | 容器化部署 |
| docker-compose | 多容器编排 |
| systemd | 服务管理 (Linux) |

---

## 核心模块

### 1. 知识图谱引擎 (Knowledge Graph Engine)

**文件：** `src/knowledge_graph.py`

**职责：**
- 构建"问题→方法→论文→实验"知识树
- 维护论文库和实验库的关联关系
- 提供查询和遍历接口

**核心类：**

```python
class KnowledgeGraph:
    """知识图谱核心类"""
    
    def __init__(self, db_path: str):
        self.db = SQLiteConnection(db_path)
        self.graph = nx.DiGraph()
    
    def add_paper(self, paper: Paper) -> str:
        """添加论文到知识库"""
        pass
    
    def add_experiment(self, exp: Experiment) -> str:
        """添加实验到知识库"""
        pass
    
    def link_paper_experiment(self, paper_id: str, exp_id: str, relation: str):
        """关联论文和实验"""
        pass
    
    def get_tree_view(self, root_id: str) -> str:
        """获取树状视图（文字版）"""
        pass
    
    def search_by_keyword(self, keyword: str) -> List[Node]:
        """按关键词搜索"""
        pass
```

**数据结构：**

```python
@dataclass
class Paper:
    title: str
    authors: List[str]
    year: int
    venue: str
    problem: str
    method: str
    conclusion: str
    tags: List[str]
    file_path: Optional[str]

@dataclass
class Experiment:
    title: str
    date: datetime
    problem: str
    method: str
    result: str
    related_papers: List[str]  # 关联的论文 ID
```

### 2. 智能推荐引擎 (Smart Recommendation Engine)

**文件：** `src/smart_recommend.py`

**职责：**
- 基于本地知识库的推荐（基础模式）
- 基于联网搜索的推荐（进阶模式）
- 相关性评分和排序

**核心算法：**

```python
class Recommender:
    """智能推荐引擎"""
    
    def __init__(self, kg: KnowledgeGraph, config: Config):
        self.kg = kg
        self.config = config
    
    def recommend_local(self, query: str, top_k: int = 10) -> List[Recommendation]:
        """本地推荐（基于关键词匹配）"""
        # 1. 提取查询关键词
        keywords = self._extract_keywords(query)
        
        # 2. 在知识库中搜索
        candidates = self.kg.search_by_keywords(keywords)
        
        # 3. 计算相关性分数
        scored = [(item, self._compute_score(query, item)) for item in candidates]
        
        # 4. 排序并返回 Top-K
        return sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]
    
    def recommend_web(self, query: str, top_k: int = 10) -> List[Recommendation]:
        """联网推荐（arXiv/PubMed/CNKI）"""
        # 1. 构建搜索查询
        search_query = self._build_search_query(query)
        
        # 2. 调用 API 获取结果
        results = self._fetch_from_arxiv(search_query)
        results += self._fetch_from_pubmed(search_query)
        
        # 3. 去重和过滤
        results = self._deduplicate(results)
        
        # 4. 计算相关性分数
        scored = [(item, self._compute_score(query, item)) for item in results]
        
        # 5. 排序并返回 Top-K
        return sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]
    
    def _extract_keywords(self, text: str) -> List[str]:
        """使用 textrank4zh 提取关键词"""
        pass
    
    def _compute_score(self, query: str, item: Any) -> float:
        """计算相关性分数（基于关键词重叠度和语义相似度）"""
        pass
```

**推荐模式对比：**

| 特性 | 基础模式（本地） | 进阶模式（联网） |
|------|-----------------|-----------------|
| 数据源 | 本地知识库 | arXiv/PubMed/CNKI |
| 网络依赖 | 无 | 有 |
| 响应速度 | 快 (<1s) | 较慢 (2-5s) |
| 数据隐私 | 完全本地 | 有网络请求 |
| 覆盖范围 | 仅本地文献 | 全球学术资源 |
| 适用场景 | 日常使用 | 深度调研 |

### 3. PPT 生成引擎 (PPT Generator Engine)

**文件：** `src/ppt_outline.py`

**职责：**
- 根据实验和文献生成 PPT 大纲
- 生成演讲备注
- 支持多种模板

**输出格式：**

```markdown
# 组会汇报 - [姓名] - [日期]

## 第 1 页：封面
- 标题：本周研究进展
- 副标题：[具体方向]
- 汇报人：[姓名]
- 日期：[日期]

## 第 2 页：研究背景
- 研究问题：[问题描述]
- 研究意义：[重要性]
- 相关工作：[2-3 篇关键文献]

**演讲备注：**
各位老师好，我今天汇报的主题是...

## 第 3 页：本周实验
- 实验目的：[目的]
- 实验方法：[方法]
- 实验结果：[数据/图表]

**演讲备注：**
本周我主要完成了以下实验...

## 第 4 页：问题分析
- 遇到的问题：[问题列表]
- 可能的原因：[分析]
- 解决方案：[计划]

## 第 5 页：下周计划
- 计划 1：[具体任务]
- 计划 2：[具体任务]
- 预期目标：[目标]

## 第 6 页：参考文献
1. [文献 1]
2. [文献 2]
3. [文献 3]
```

**核心方法：**

```python
class PPTGenerator:
    """PPT 大纲生成器"""
    
    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
    
    def generate_outline(self, experiment_ids: List[str]) -> PPTOutline:
        """生成 PPT 大纲"""
        # 1. 获取实验数据
        experiments = [self.kg.get_experiment(eid) for eid in experiment_ids]
        
        # 2. 获取关联文献
        related_papers = self._get_related_papers(experiments)
        
        # 3. 构建大纲结构
        outline = self._build_structure(experiments, related_papers)
        
        # 4. 生成演讲备注
        outline.speaker_notes = self._generate_speaker_notes(outline)
        
        return outline
```

### 4. 文献爬取器 (Web Crawler)

**文件：** `src/arxiv_fetcher.py`

**职责：**
- 合规爬取公开学术平台
- 解析和结构化数据
- 临时缓存管理

**支持的平台：**

| 平台 | API | 数据类型 | 限制 |
|------|-----|---------|------|
| arXiv | arXiv API | 标题、摘要、作者、分类 | 无限制 |
| PubMed | E-utilities | 标题、摘要、MeSH 词 | 3 次/秒 |
| CNKI | 公开页面 | 标题、摘要（需登录） | 有反爬 |

**合规设计：**

```python
class ArxivFetcher:
    """arXiv 文献获取器"""
    
    def __init__(self, cache_dir: str, max_cache_hours: int = 24):
        self.cache_dir = cache_dir
        self.max_cache_hours = max_cache_hours
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AcademicLobster/2.0 (Research Tool)'
        })
    
    def search(self, query: str, max_results: int = 10) -> List[Paper]:
        """搜索 arXiv 文献"""
        # 1. 检查缓存
        cached = self._check_cache(query)
        if cached:
            return cached
        
        # 2. 调用 API
        url = f"http://export.arxiv.org/api/query?search_query={query}&max_results={max_results}"
        response = self.session.get(url, timeout=30)
        
        # 3. 解析 XML
        papers = self._parse_response(response.text)
        
        # 4. 写入缓存
        self._write_cache(query, papers)
        
        return papers
    
    def _check_cache(self, query: str) -> Optional[List[Paper]]:
        """检查缓存是否有效"""
        cache_file = self._get_cache_file(query)
        if not os.path.exists(cache_file):
            return None
        
        # 检查缓存时间
        age = time.time() - os.path.getmtime(cache_file)
        if age > self.max_cache_hours * 3600:
            return None
        
        return self._read_cache(cache_file)
```

---

## 数据流

### 典型用户操作流程

```
用户输入研究问题
       │
       ▼
┌──────────────┐
│  文本预处理  │
│  (分词/清洗) │
└──────┬───────┘
       │
       ▼
┌──────────────┐     ┌──────────────┐
│  知识图谱    │────▶│  智能推荐    │
│  查询        │     │  引擎        │
└──────┬───────┘     └──────┬───────┘
       │                    │
       │                    ▼
       │            ┌──────────────┐
       │            │  本地推荐    │
       │            │  (关键词匹配)│
       │            └──────┬───────┘
       │                    │
       │            ┌───────▼───────┐
       │            │  联网推荐     │
       │            │  (arXiv API)  │
       │            └──────┬────────┘
       │                   │
       ▼                   ▼
┌──────────────────────────────────┐
│         结果聚合和排序           │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│         返回给用户               │
│  (推荐列表 + 相关性分数 + 来源)   │
└──────────────────────────────────┘
```

### 数据持久化流程

```
用户添加论文
       │
       ▼
┌──────────────┐
│  解析元数据  │
│  (标题/作者/│
│   摘要等)    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  提取关键词  │
│  (textrank)  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  写入 SQLite │
│  (papers 表) │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  更新知识图谱│
│  (NetworkX)  │
└──────────────┘
```

---

## 安全设计

### 数据安全

| 风险 | 防护措施 |
|------|---------|
| 数据泄露 | 本地存储，不上传云端 |
| 未授权访问 | 文件系统权限控制 |
| 数据丢失 | 定期备份建议 |
| 恶意注入 | 输入验证和参数化查询 |

### 网络安全

| 风险 | 防护措施 |
|------|---------|
| 中间人攻击 | HTTPS 请求（联网时） |
| DDoS | 请求频率限制 |
| 恶意网站 | URL 白名单 |
| 数据泄露 | 不发送用户数据 |

### 合规设计

```python
class ComplianceChecker:
    """合规检查器"""
    
    @staticmethod
    def check_copyright(paper: Paper) -> bool:
        """检查版权合规"""
        # 仅处理公开摘要，不涉及全文
        if paper.is_full_text:
            return False
        return True
    
    @staticmethod
    def check_data_usage(data: Dict) -> bool:
        """检查数据使用合规"""
        # 确保不存储用户身份信息
        if 'user_id' in data or 'email' in data:
            return False
        return True
```

---

## 部署架构

### 单机部署（推荐）

```
┌─────────────────────────────────────┐
│           用户电脑                   │
│  ┌───────────────────────────────┐  │
│  │   学术龙虾 v2                  │  │
│  │  ┌─────────┐  ┌─────────────┐ │  │
│  │  │  Flask  │  │   SQLite    │ │  │
│  │  │  Server │  │   Database  │ │  │
│  │  └─────────┘  └─────────────┘ │  │
│  │  ┌─────────┐  ┌─────────────┐ │  │
│  │  │  知识   │  │   推荐      │ │  │
│  │  │  图谱   │  │   引擎      │ │  │
│  │  └─────────┘  └─────────────┘ │  │
│  └───────────────────────────────┘  │
│                                     │
│  数据目录：~/.academic-lobster/     │
│  日志目录：~/.academic-lobster/logs/│
└─────────────────────────────────────┘
```

### Docker 部署

```yaml
# docker-compose.yml
version: '3.8'

services:
  academic-lobster:
    build: .
    ports:
      - "5001:5001"
    volumes:
      - ./data:/app/data
      - ./config:/app/config
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
```

---

## 扩展性设计

### 插件架构

```python
class PluginManager:
    """插件管理器"""
    
    def __init__(self):
        self.plugins = {}
    
    def register(self, name: str, plugin: Plugin):
        """注册插件"""
        self.plugins[name] = plugin
    
    def get_plugin(self, name: str) -> Optional[Plugin]:
        """获取插件"""
        return self.plugins.get(name)
    
    def list_plugins(self) -> List[str]:
        """列出所有插件"""
        return list(self.plugins.keys())
```

### 配置驱动

```yaml
# config.yaml
database:
  path: ~/.academic-lobster/data.db
  
crawler:
  enabled: true
  sources:
    - arxiv
    - pubmed
  cache_hours: 24
  
ui:
  theme: light
  language: zh-CN
  
security:
  encryption: true
  audit_log: true
```

---

## 性能优化

### 缓存策略

| 数据类型 | 缓存位置 | 过期时间 |
|---------|---------|---------|
| arXiv 搜索结果 | 本地文件 | 24 小时 |
| 知识图谱查询 | 内存 | 会话期间 |
| 文献摘要 | 本地文件 | 7 天 |
| 用户配置 | 内存 | 启动时加载 |

### 索引优化

```sql
-- 为常用查询创建索引
CREATE INDEX idx_paper_title ON papers(title);
CREATE INDEX idx_paper_year ON papers(year);
CREATE INDEX idx_paper_tags ON papers(tags);
CREATE INDEX idx_experiment_date ON experiments(date);
CREATE INDEX idx_relation_paper_id ON relations(paper_id);
CREATE INDEX idx_relation_exp_id ON relations(experiment_id);
```

---

## 监控与日志

### 日志级别

| 级别 | 用途 | 示例 |
|------|------|------|
| DEBUG | 调试信息 | 函数调用参数 |
| INFO | 正常操作 | 用户登录、数据添加 |
| WARNING | 警告 | 网络请求失败 |
| ERROR | 错误 | 数据库连接失败 |
| CRITICAL | 严重错误 | 系统崩溃 |

### 日志格式

```
[时间戳] [级别] [模块] 消息
[2026-03-16 20:30:15] [INFO] [knowledge_graph] 添加论文：ResNet (ID: 12345)
[2026-03-16 20:30:16] [ERROR] [arxiv_fetcher] API 请求失败：超时
```

---

## 未来规划

### 短期（3 个月）

- [ ] 添加更多学术平台支持（Google Scholar、Semantic Scholar）
- [ ] 改进推荐算法（引入语义相似度）
- [ ] 优化 UI/UX 设计

### 中期（6 个月）

- [ ] 支持多用户协作
- [ ] 添加移动端应用
- [ ] 集成更多 AI 模型

### 长期（1 年）

- [ ] 建立学术社区
- [ ] 支持多语言
- [ ] 企业级部署方案

---

**文档版本：** 2.0

**最后更新：** 2026-03-16

🦞 **学术龙虾 v2，为每一位认真做研究的人服务。**
