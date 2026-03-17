# 快速开始指南

5 分钟内上手学术龙虾 v2！

---

## 📋 目录

- [系统要求](#系统要求)
- [安装步骤](#安装步骤)
- [快速体验](#快速体验)
- [核心功能演示](#核心功能演示)
- [常见问题](#常见问题)
- [下一步](#下一步)

---

## 系统要求

### 最低要求

| 组件 | 要求 |
|------|------|
| **操作系统** | Windows 10 / macOS 10.15 / Linux (Ubuntu 20.04+) |
| **Python** | 3.9 或更高版本 |
| **内存** | 4 GB RAM |
| **存储** | 1 GB 可用空间 |
| **网络** | 可选（离线模式可用） |

### 推荐配置

| 组件 | 要求 |
|------|------|
| **操作系统** | Windows 11 / macOS 12+ / Linux (Ubuntu 22.04+) |
| **Python** | 3.10 或更高版本 |
| **内存** | 8 GB RAM |
| **存储** | 5 GB 可用空间 |
| **网络** | 宽带（用于联网搜索） |

---

## 安装步骤

### 步骤 1：检查 Python 版本

```bash
python3 --version
```

需要 Python 3.9 或更高版本。如未安装，请前往 [python.org](https://www.python.org/) 下载。

### 步骤 2：克隆仓库

```bash
git clone https://github.com/bieyl/research.git
cd research
```

### 步骤 3：创建虚拟环境（推荐）

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 步骤 4：安装依赖

```bash
pip install -r requirements.txt
```

安装过程约需 2-5 分钟，取决于网络速度。

### 步骤 5：验证安装

```bash
python3 -c "import flask, jieba, networkx; print('✅ 所有依赖安装成功')"
```

---

## 快速体验

### 方式 1：Web 界面（推荐）

```bash
python3 src/web_app_v2.py
```

然后在浏览器中打开：**http://localhost:5001**

你会看到：
```
🦞 学术龙虾 v2 - 科研知识大脑

[添加论文] [添加实验] [智能推荐] [生成 PPT]
```

### 方式 2：命令行演示

```bash
python3 src/demo_v2.py
```

选择演示模式：
```
请选择演示模式:
1) 手动演示（逐步操作）
2) 自动演示（3 分钟完整流程）
```

推荐选择 **2) 自动演示**，快速了解全部功能。

### 方式 3：Docker 部署（可选）

```bash
# 构建镜像
docker build -t academic-lobster .

# 运行容器
docker run -d -p 5001:5001 -v ./data:/app/data academic-lobster
```

然后在浏览器中打开：**http://localhost:5001**

---

## 核心功能演示

### 功能 1：添加论文

**步骤：**

1. 点击"添加论文"按钮
2. 输入或粘贴论文信息：
   ```
   标题：Deep Residual Learning for Image Recognition
   作者：Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
   年份：2016
   会议：CVPR
   研究问题：深层网络训练退化问题
   方法：残差连接（Residual Connection）
   结论：残差网络可以显著提升深度网络的训练效果
   ```
3. 点击"保存"

**输出：**
```
✅ 论文添加成功！
📄 ResNet (He et al., 2016)
   ID: paper_001
   标签：深度学习、残差网络、CVPR
```

### 功能 2：添加实验

**步骤：**

1. 点击"添加实验"按钮
2. 输入实验信息：
   ```
   标题：ResNet-50 迁移学习实验
   日期：2026-03-16
   研究问题：图像分类任务中的迁移学习效果
   方法：基于 ResNet-50 的迁移学习
   结果：在自定义数据集上达到 87% 准确率
   ```
3. 点击"保存"

**输出：**
```
✅ 实验添加成功！
🧪 ResNet-50 迁移学习实验 (2026-03-16)
   ID: exp_001
```

### 功能 3：查看知识图谱

**步骤：**

1. 点击"知识图谱"按钮
2. 选择"树状视图"

**输出：**
```
🌳 科研知识图谱

【研究问题】深层网络训练退化问题
├─【方法】残差连接
│  ├─📄 ResNet (He et al., 2016)
│  └─📄 Identity Mappings (He et al., 2016)
└─【方法】改进的残差块
   └─🧪 ResNet-50 迁移学习实验 (2026-03-16)
```

### 功能 4：智能推荐

**步骤：**

1. 点击"智能推荐"按钮
2. 输入查询：
   ```
   残差网络在图像分类中的应用
   ```
3. 选择模式：
   - 🔵 基础模式（仅本地）
   - 🟢 进阶模式（本地 + 联网）

**输出（基础模式）：**
```
💡 智能推荐

📚 关联文献（按相关性排序）：

1. ResNet 原始论文 (He et al., 2016)
   相关性：★★★★★ (95/100)
   匹配理由：你的实验基于该论文的残差结构
   来源：本地知识库
```

**输出（进阶模式）：**
```
💡 智能推荐

📚 关联文献（按相关性排序）：

1. ResNet 原始论文 (He et al., 2016)
   相关性：★★★★★ (95/100)
   来源：本地知识库

🌐 公开学术平台补充推荐：

2. ECA-Net (Wang et al., CVPR 2020)
   来源：arXiv (公开摘要)
   相关性：★★★☆☆ (78/100)
   链接：https://arxiv.org/abs/1910.03151
   ⚠️ 声明：仅获取公开摘要，未存储全文
```

### 功能 5：生成 PPT 大纲

**步骤：**

1. 点击"生成 PPT"按钮
2. 选择要汇报的实验
3. 点击"生成"

**输出：**
```markdown
# 组会汇报 - 2026-03-16

## 第 1 页：封面
- 标题：本周研究进展
- 汇报人：[姓名]
- 日期：2026-03-16

## 第 2 页：研究背景
- 研究问题：深层网络训练退化问题
- 相关工作：ResNet (He et al., 2016)

## 第 3 页：本周实验
- 实验名称：ResNet-50 迁移学习实验
- 方法：基于 ResNet-50 的迁移学习
- 结果：准确率 87%

## 第 4 页：问题分析
- 遇到的问题：小样本过拟合
- 解决方案：数据增强、正则化

## 第 5 页：下周计划
- 尝试不同的预训练模型
- 调整超参数

## 第 6 页：参考文献
1. He K, et al. Deep Residual Learning for Image Recognition. CVPR 2016.
```

---

## 常见问题

### Q1: 安装失败怎么办？

**A:** 尝试以下步骤：

```bash
# 1. 升级 pip
pip install --upgrade pip

# 2. 清除缓存
pip cache purge

# 3. 重新安装
pip install -r requirements.txt --no-cache-dir
```

如仍有问题，检查 Python 版本是否为 3.9+。

### Q2: Web 界面无法访问？

**A:** 检查以下步骤：

```bash
# 1. 确认服务已启动
# 应该看到：* Running on http://127.0.0.1:5001

# 2. 检查端口是否被占用
lsof -i :5001  # Linux/macOS
netstat -ano | findstr 5001  # Windows

# 3. 尝试其他端口
python3 src/web_app_v2.py --port 5002
```

### Q3: 联网搜索失败？

**A:** 检查网络连接：

```bash
# 测试 arXiv API 是否可访问
curl -I https://export.arxiv.org/api/query?search_query=deep+learning

# 如无法访问，检查防火墙设置
```

如网络问题无法解决，可继续使用本地模式。

### Q4: 中文分词不准确？

**A:** 尝试添加自定义词典：

```python
# 在 src/config.py 中添加
import jieba
jieba.add_word("残差网络")
jieba.add_word("迁移学习")
```

### Q5: 数据如何备份？

**A:** 定期备份数据目录：

```bash
# Linux/macOS
tar -czf backup-$(date +%Y%m%d).tar.gz ~/.academic-lobster/

# Windows (PowerShell)
Compress-Archive -Path $env:APPDATA\academic-lobster -DestinationPath backup-$(Get-Date -Format yyyyMMdd).zip
```

---

## 下一步

恭喜你完成快速开始！接下来可以：

### 📚 深入学习

- [用户手册](docs/user-guide.md) — 详细功能说明
- [架构文档](docs/architecture.md) — 技术架构详解
- [安全合规](docs/security.md) — 安全设计说明

### 🔧 高级用法

- 配置自定义推荐算法
- 添加新的学术平台支持
- 自定义 PPT 模板

### 🤝 参与贡献

- [贡献指南](CONTRIBUTING.md) — 如何贡献代码
- [GitHub 仓库](https://github.com/bieyl/research) — 提交 Issue 和 PR

### 📞 获取帮助

- [GitHub Issues](https://github.com/bieyl/research/issues) — 报告问题
- 邮件列表（待设置）— 讨论和交流

---

## 附录：命令行参数

### Web 界面参数

```bash
python3 src/web_app_v2.py [选项]

选项:
  --port PORT         Web 服务器端口 (默认：5001)
  --host HOST         监听地址 (默认：127.0.0.1)
  --debug             启用调试模式
  --data-dir DIR      数据目录 (默认：~/.academic-lobster)
  --offline           离线模式（禁用网络）
  --help              显示帮助信息
```

### 演示脚本参数

```bash
python3 src/demo_v2.py [选项]

选项:
  --mode MODE         演示模式 (1=手动，2=自动)
  --speed SPEED       演示速度 (1=慢，2=正常，3=快)
  --output FILE       输出文件 (可选)
  --help              显示帮助信息
```

---

**文档版本：** 2.0

**最后更新：** 2026-03-16

🦞 **学术龙虾 v2，为每一位认真做研究的人服务。**
