# 贡献指南
# Contributing to Academic Lobster v2

感谢你对学术龙虾 v2 的兴趣！本文档将指导你如何为项目做出贡献。

---

## 📋 目录

- [行为准则](#行为准则)
- [我能贡献什么](#我能贡献什么)
- [开发环境设置](#开发环境设置)
- [提交代码流程](#提交代码流程)
- [代码规范](#代码规范)
- [测试](#测试)
- [文档](#文档)
- [问题报告](#问题报告)
- [功能建议](#功能建议)

---

## 行为准则

本项目采用 [Contributor Covenant](https://www.contributor-covenant.org/) 行为准则。

**核心原则：**
- 友好包容
- 尊重多样性
- 建设性反馈
- 学术诚信

---

## 我能贡献什么

### 代码贡献
- 🐛 修复 Bug
- ✨ 新功能开发
- ⚡ 性能优化
- 🔒 安全改进

### 文档贡献
- 📝 完善文档
- 🌍 翻译（支持多语言）
- 📚 示例代码
- 🎓 使用教程

### 其他贡献
- 💡 功能建议
- 🐞 问题报告
- 📢 推广项目
- 🎨 UI/UX 改进

---

## 开发环境设置

### 1. Fork 项目

```bash
# 在 GitHub 上点击 Fork 按钮
```

### 2. 克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/research.git
cd research
```

### 3. 创建分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 运行测试

```bash
python tests/test_suite.py
```

---

## 提交代码流程

### 1. 修改代码

确保代码符合规范（见下方）。

### 2. 运行测试

```bash
python tests/test_suite.py
```

### 3. 提交更改

```bash
git add .
git commit -m "类型：简短描述"
```

**Commit 信息格式：**
```
类型：简短描述

详细描述（可选）

关联 Issue: #123
```

**类型说明：**
- `feat` - 新功能
- `fix` - Bug 修复
- `docs` - 文档更新
- `style` - 代码格式
- `refactor` - 重构
- `test` - 测试
- `chore` - 构建/工具

### 4. 推送代码

```bash
git push origin feature/your-feature-name
```

### 5. 创建 Pull Request

在 GitHub 上创建 PR，填写：
- 修改内容
- 修改原因
- 测试情况
- 关联 Issue

---

## 代码规范

### Python 代码

遵循 [PEP 8](https://pep8.org/) 规范。

**关键规则：**
- 缩进：4 个空格
- 行宽：≤ 100 字符
- 命名：
  - 变量/函数：`snake_case`
  - 类：`CamelCase`
  - 常量：`UPPER_CASE`

**示例：**
```python
def calculate_similarity(keywords_a, keywords_b):
    """计算关键词相似度"""
    if not keywords_a or not keywords_b:
        return 0.0
    
    intersection = set(keywords_a) & set(keywords_b)
    union = set(keywords_a) | set(keywords_b)
    
    return len(intersection) / len(union) if union else 0.0
```

### 文档规范

使用 Markdown 格式。

**标题层级：**
```markdown
# 一级标题
## 二级标题
### 三级标题
```

**代码块：**
````markdown
```python
# Python 代码
```
````

---

## 测试

### 单元测试

```bash
python tests/test_suite.py
```

### 覆盖率

```bash
pip install pytest-cov
pytest --cov=src tests/
```

### 测试规范

- 每个核心功能都要有测试
- 测试覆盖率目标：≥ 80%
- 测试命名：`test_功能_场景_预期结果`

---

## 文档

### 文档位置

- 用户文档：`docs/user-guide.md`
- API 文档：`docs/API.md`
- 架构文档：`docs/architecture.md`
- 贡献指南：`CONTRIBUTING.md`

### 文档更新

代码修改时，同步更新相关文档。

---

## 问题报告

### 创建 Issue

在 GitHub Issues 中创建问题，包含：

**Bug 报告：**
```markdown
### 问题描述
简要描述问题

### 复现步骤
1. 步骤 1
2. 步骤 2
3. 步骤 3

### 预期行为
应该发生什么

### 实际行为
实际发生了什么

### 环境信息
- OS: 
- Python 版本：
- 学术龙虾版本：

### 截图（可选）
```

**功能建议：**
```markdown
### 功能描述
简要描述功能

### 使用场景
谁会用这个功能，解决什么问题

### 实现建议（可选）
如何实现

### 替代方案（可选）
是否有其他解决方案
```

---

## 评审流程

1. **自动检查** - CI 运行测试
2. **代码评审** - 维护者审查代码
3. **修改反馈** - 根据评审意见修改
4. **合并** - 合并到主分支

---

## 致谢

所有贡献者都会被记录在 `CONTRIBUTORS.md` 中。

感谢你的贡献！🦞

---

## 联系方式

- GitHub Issues: https://github.com/bieyl/research/issues
- Email: bieyunlong1@163.com

---

**🦞 学术龙虾 v2 - 让知识产生连接**
