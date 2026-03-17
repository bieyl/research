# Contributing to 学术龙虾 v2

首先，感谢你愿意为学术龙虾 v2 贡献代码！本指南将帮助你快速上手。

---

## 📋 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发环境搭建](#开发环境搭建)
- [代码风格](#代码风格)
- [Pull Request 流程](#pull-request-流程)
- [添加新功能](#添加新功能)
- [报告 Bug](#报告 -bug)
- [建议新功能](#建议新功能)

---

## 行为准则

本项目遵循 [Contributor Covenant](https://www.contributor-covenant.org/) 行为准则：

- 使用友好和包容的语言
- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

---

## 如何贡献

### 你可以贡献的内容

- 🐛 报告 Bug
- 💡 建议新功能
- 📝 改进文档
- 🎨 改进 UI/UX
- 🔧 提交代码修复
- 🧪 添加测试用例
- 🌍 翻译文档

### 贡献流程概览

```
1. Fork 仓库
2. Clone 到本地
3. 创建分支 (git checkout -b feature/AmazingFeature)
4. 提交更改 (git commit -m 'Add some AmazingFeature')
5. 推送到分支 (git push origin feature/AmazingFeature)
6. 开启 Pull Request
```

---

## 开发环境搭建

### 前置要求

- Python 3.9+
- Git
- pip 或 conda

### 步骤

```bash
# 1. Fork 仓库
# 在 GitHub 上点击 Fork 按钮

# 2. Clone 到本地
git clone https://github.com/YOUR_USERNAME/research.git
cd research

# 3. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate     # Windows

# 4. 安装依赖
pip install -r requirements.txt

# 5. 安装开发依赖
pip install -r requirements-dev.txt  # 如果有的话

# 6. 运行测试
python -m pytest tests/

# 7. 启动开发服务器
python3 src/web_app_v2.py
```

---

## 代码风格

### Python 代码规范

遵循 [PEP 8](https://pep8.org/) 规范：

```python
# ✅ 好的示例
def calculate_similarity(doc1, doc2):
    """计算两个文档的相似度分数"""
    if not doc1 or not doc2:
        return 0.0
    return cosine_similarity(doc1, doc2)

# ❌ 坏的示例
def calcSim(d1,d2):  # 命名不清晰
    if d1==None or d2==None:  # 应用 is None
        return 0
    return cosine_similarity(d1,d2)  # 缺少空格
```

### 代码检查工具

```bash
# 安装检查工具
pip install flake8 black isort mypy

# 格式化代码
black src/

# 排序 imports
isort src/

# 检查代码风格
flake8 src/

# 类型检查
mypy src/
```

### 提交信息规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```
feat: 添加新的知识图谱可视化功能
fix: 修复文献摘要生成的空指针错误
docs: 更新 README 安装指南
style: 格式化代码（不影响功能）
refactor: 重构推荐引擎（无功能变化）
test: 添加知识图谱单元测试
chore: 更新依赖版本
```

---

## Pull Request 流程

### PR 标题规范

```
<type>(<scope>): <subject>

示例：
feat(ui): 添加深色模式支持
fix(core): 修复中文分词错误
docs(readme): 更新快速开始指南
```

### PR 描述模板

```markdown
## 描述
简要说明这个 PR 做了什么

## 相关 Issue
Fixes #123

## 更改类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 文档更新
- [ ] 代码重构
- [ ] 测试添加

## 测试
- [ ] 已添加单元测试
- [ ] 已手动测试
- [ ] 不需要测试

## 截图（如适用）
[截图]

## 检查清单
- [ ] 代码遵循项目规范
- [ ] 已更新文档
- [ ] 无新的警告信息
- [ ] 通过了所有测试
```

### 审查流程

1. **自动检查**：GitHub Actions 运行测试和代码检查
2. **Maintainer 审查**：至少需要 1 个维护者批准
3. **解决问题**：根据审查意见修改代码
4. **合并**：审查通过后合并到 main 分支

---

## 添加新功能

### 步骤

1. **讨论**：先在 Issue 中讨论新功能的必要性
2. **设计**：说明功能设计和技术方案
3. **实现**：编写代码和测试
4. **文档**：更新相关文档
5. **提交**：创建 Pull Request

### 示例：添加新的推荐算法

```python
# src/new_recommender.py

class NewRecommender:
    """基于 XXX 的新型推荐算法"""
    
    def __init__(self, config):
        self.config = config
    
    def recommend(self, query, top_k=10):
        """
        生成推荐结果
        
        Args:
            query: 查询文本
            top_k: 返回数量
            
        Returns:
            List[Dict]: 推荐结果列表
        """
        # 实现代码
        pass
    
    def _validate_input(self, query):
        """验证输入格式"""
        # 验证逻辑
        pass
```

### 测试示例

```python
# tests/test_new_recommender.py

import pytest
from src.new_recommender import NewRecommender

def test_recommend_returns_list():
    recommender = NewRecommender(config={})
    result = recommender.recommend("test query")
    assert isinstance(result, list)

def test_recommend_respects_top_k():
    recommender = NewRecommender(config={})
    result = recommender.recommend("test query", top_k=5)
    assert len(result) <= 5
```

---

## 报告 Bug

### Bug 报告模板

```markdown
**描述问题**
清晰简洁地描述问题是什么

**复现步骤**
1. 执行步骤 1
2. 执行步骤 2
3. 看到错误

**期望行为**
清晰简洁地描述期望发生什么

**截图**
如适用，添加截图帮助说明

**环境信息**
- OS: [e.g. macOS 14.0]
- Python: [e.g. 3.9.18]
- Version: [e.g. 2.0.0]

**日志**
```
错误日志内容
```

**额外信息**
其他有助于解决问题的信息
```

### 提交 Bug

1. 在 [Issues](https://github.com/bieyl/research/issues) 中搜索是否已有相同问题
2. 如果没有，点击 "New Issue"
3. 选择 "Bug Report" 模板
4. 填写详细信息
5. 提交

---

## 建议新功能

### 功能建议模板

```markdown
**功能描述**
清晰简洁地描述你想要的功能

**动机**
为什么需要这个功能？解决什么问题？

**替代方案**
有没有其他方式可以实现？

**额外信息**
其他有助于理解的信息
```

### 提交建议

1. 在 [Issues](https://github.com/bieyl/research/issues) 中搜索是否已有相同建议
2. 如果没有，点击 "New Issue"
3. 选择 "Feature Request" 模板
4. 填写详细信息
5. 提交

---

## 文档规范

### Markdown 格式

- 使用 `#` 表示标题层级
- 使用 `-` 或 `*` 表示列表
- 使用 ` ```language ` 表示代码块
- 使用 `**粗体**` 强调重点

### 文档结构

```markdown
# 功能名称

简要描述（1-2 句话）

## 使用场景

什么情况下使用这个功能

## 使用方法

```python
# 代码示例
```

## 参数说明

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| param1 | str | 说明 | None |

## 示例输出

展示输出结果

## 注意事项

需要特别注意的地方
```

---

## 许可证

通过贡献代码，你同意你的贡献遵循本项目的 [MIT License](LICENSE)。

---

## 致谢

感谢所有为学术龙虾 v2 做出贡献的开发者！

🦞 **学术龙虾 v2，为每一位认真做研究的人服务。**
