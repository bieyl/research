# 安全与合规声明

学术龙虾 v2 严格遵守数据安全、隐私保护和知识产权规范。本文档详细说明我们的安全设计、合规措施和使用边界。

---

## 📋 目录

- [核心原则](#核心原则)
- [数据安全](#数据安全)
- [隐私保护](#隐私保护)
- [知识产权](#知识产权)
- [网络安全](#网络安全)
- [合规对照表](#合规对照表)
- [第三方审计](#第三方审计)
- [联系方式](#联系方式)

---

## 核心原则

### 1. 本地优先 (Local-First)

**承诺：** 所有用户数据默认存储在本地设备，不上传至任何云端服务器。

**实现：**
- SQLite 本地数据库
- 文件系统存储文献和实验数据
- 完全离线模式可用

**验证方式：**
- 代码开源可审计
- 网络监控工具可验证无上传行为
- 可配置防火墙规则阻止所有外联

### 2. 权限最小化 (Least Privilege)

**承诺：** 仅申请和运行必要的最小权限。

**实现：**
- 仅读取用户明确指定的文件
- 仅写入用户授权的数据目录
- 不申请系统级权限（管理员/root）
- 不访问通讯录、位置、相机等无关权限

**验证方式：**
- 权限申请清单公开
- 运行时权限监控

### 3. 透明可控 (Transparency)

**承诺：** 所有操作透明，用户完全可控。

**实现：**
- 完整的操作日志
- 数据导出功能
- 一键删除全部数据
- 网络请求日志

**验证方式：**
- 日志文件公开可读
- 数据导出格式标准化

### 4. 合规设计 (Compliance by Design)

**承诺：** 从设计源头考虑合规性。

**实现：**
- 隐私影响评估（PIA）
- 安全设计审查
- 定期合规审计
- 遵循相关法律法规

---

## 数据安全

### 存储安全

| 数据类型 | 存储位置 | 加密方式 | 访问控制 |
|---------|---------|---------|---------|
| 文献元数据 | 本地 SQLite | 可选 AES-256 | 文件系统权限 |
| 实验记录 | 本地 SQLite | 可选 AES-256 | 文件系统权限 |
| 用户配置 | 本地 YAML | 无 | 文件系统权限 |
| 操作日志 | 本地文件 | 无 | 文件系统权限 |
| 临时缓存 | 本地临时目录 | 无 | 自动清理 |

### 传输安全

| 场景 | 协议 | 加密 | 说明 |
|------|------|------|------|
| arXiv API 请求 | HTTPS | TLS 1.3 | 仅发送搜索关键词 |
| PubMed API 请求 | HTTPS | TLS 1.3 | 仅发送搜索关键词 |
| Web 界面访问 | HTTP (本地) | 无 | 仅限 localhost |

**重要说明：**
- 所有网络请求仅发送搜索关键词，不发送用户数据
- 本地 Web 界面仅监听 localhost，不暴露到外部网络
- 可选配置为完全离线模式

### 备份建议

**官方建议：**
```bash
# 定期备份数据目录
tar -czf academic-lobster-backup-$(date +%Y%m%d).tar.gz \
    ~/.academic-lobster/data/
    
# 建议备份频率：每周
# 建议存储位置：外部硬盘或加密云存储
```

---

## 隐私保护

### 不收集的数据

学术龙虾 v2 **不会**收集以下数据：

- ❌ 个人身份信息（姓名、邮箱、电话）
- ❌ 研究内容（论文全文、实验数据）
- ❌ 使用行为数据（点击、浏览记录）
- ❌ 设备信息（MAC 地址、IP 地址）
- ❌ 位置信息

### 可能收集的数据

学术龙虾 v2 **可能**收集以下数据（用户明确授权后）：

- ✅ 文献元数据（标题、作者、摘要）— 仅本地存储
- ✅ 实验记录 — 仅本地存储
- ✅ 搜索历史 — 仅本地存储，可选关闭
- ✅ 崩溃报告 — 可选发送，匿名

### 用户权利

根据 GDPR 和中国《个人信息保护法》，用户享有以下权利：

| 权利 | 说明 | 行使方式 |
|------|------|---------|
| 知情权 | 了解数据如何被使用 | 阅读本文档 |
| 访问权 | 访问个人数据 | 数据导出功能 |
| 更正权 | 更正错误数据 | 直接编辑 |
| 删除权 | 删除个人数据 | 一键删除功能 |
| 可携带权 | 导出个人数据 | 数据导出功能 |
| 撤回同意 | 撤回数据处理同意 | 关闭相关功能 |

---

## 知识产权

### 尊重版权

**承诺：** 学术龙虾 v2 尊重所有学术资源的知识产权。

**实现：**

| 资源类型 | 处理方式 | 说明 |
|---------|---------|------|
| arXiv 论文 | 仅获取公开摘要 | 不存储全文，提供官方链接 |
| PubMed 论文 | 仅获取公开摘要 | 不存储全文，提供官方链接 |
| CNKI 论文 | 仅获取公开摘要 | 不存储全文，提供官方链接 |
| 用户上传文献 | 本地存储 | 用户自行负责版权 |

### 合理使用

学术龙虾 v2 的文献处理符合"合理使用"原则：

- ✅ 仅处理公开、免费的学术摘要
- ✅ 不绕过付费墙或技术保护措施
- ✅ 不提供全文下载或分发
- ✅ 明确标注来源和版权信息
- ✅ 仅用于科研学习目的

### 开源许可证

学术龙虾 v2 采用 **MIT License** 开源：

```
MIT License

Copyright (c) 2026 学术龙虾

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 网络安全

### 网络请求清单

学术龙虾 v2 **仅**在以下场景发起网络请求：

| 场景 | 目标域名 | 目的 | 发送数据 | 接收数据 |
|------|---------|------|---------|---------|
| arXiv 搜索 | export.arxiv.org | 获取文献摘要 | 搜索关键词 | 公开摘要 |
| PubMed 搜索 | eutils.ncbi.nlm.nih.gov | 获取文献摘要 | 搜索关键词 | 公开摘要 |
| 版本检查 | api.github.com | 检查更新 | 无 | 版本信息 |

**可选配置为完全离线模式：**
```yaml
# config.yaml
network:
  enabled: false  # 完全禁用网络
```

### 防火墙规则

建议配置防火墙规则：

```bash
# 允许出站 HTTPS（仅 arXiv 和 PubMed）
iptables -A OUTPUT -p tcp -d export.arxiv.org --dport 443 -j ACCEPT
iptables -A OUTPUT -p tcp -d eutils.ncbi.nlm.nih.gov --dport 443 -j ACCEPT

# 阻止其他所有出站连接
iptables -A OUTPUT -p tcp --dport 443 -j DROP
```

### 安全更新

**更新策略：**
- 定期检查 GitHub  releases
- 通过官方渠道下载更新
- 验证更新文件完整性（SHA-256）
- 备份数据后更新

---

## 合规对照表

### 中国法律法规

| 法规 | 要求 | 学术龙虾实现 | 证明方式 |
|------|------|-------------|---------|
| 《网络安全法》 | 网络运营者安全保护义务 | 本地存储，不上传数据 | 代码审计 |
| 《数据安全法》 | 数据分类分级保护 | 数据本地加密存储 | 安全文档 |
| 《个人信息保护法》 | 个人信息保护 | 不收集个人信息 | 隐私政策 |
| 《著作权法》 | 著作权保护 | 仅处理公开摘要 | 功能设计 |

### 国际规范

| 规范 | 要求 | 学术龙虾实现 | 证明方式 |
|------|------|-------------|---------|
| GDPR | 个人数据保护 | 不收集个人数据 | 隐私政策 |
| FAIR 原则 | 数据可查找、可访问、可互操作、可重用 | 数据导出标准化 | 数据格式文档 |
| TOP 原则 | 科研透明度 | 开源代码 | GitHub 仓库 |

---

## 第三方审计

### 代码审计

学术龙虾 v2 欢迎第三方安全审计：

- **代码仓库：** https://github.com/bieyl/research
- **安全文档：** docs/security.md
- **架构文档：** docs/architecture.md

### 审计清单

审计者可重点关注：

- [ ] 数据是否真的本地存储
- [ ] 是否有隐藏的网络请求
- [ ] 是否有未声明的数据收集
- [ ] 权限申请是否最小化
- [ ] 加密实现是否正确
- [ ] 日志是否完整可追溯

### 联系方式

如发现安全问题，请联系：

- **邮箱：** security@academic-lobster.org（待设置）
- **GitHub Issue：** https://github.com/bieyl/research/issues
- **GPG Key：** （待发布）

**响应时间：** 48 小时内回复

---

## 合规承诺

学术龙虾 v2 承诺：

1. **不收集** 任何用户身份信息、研究内容或实验数据
2. **不上传** 任何用户数据到云端服务器
3. **不提供** 付费文献的全文下载或分发
4. **不绕过** 任何技术保护措施或付费墙
5. **遵守** 所有适用的法律法规和学术规范

### 违规处理

如发现学术龙虾 v2 违反上述承诺：

1. 我们将立即修复问题
2. 公开披露问题详情
3. 通知受影响的用户
4. 承担相应法律责任

---

## 版本历史

| 版本 | 日期 | 变更说明 |
|------|------|---------|
| 1.0 | 2026-03-12 | 初始版本 |
| 2.0 | 2026-03-16 | 全面更新，增加合规对照表 |

---

## 附录：隐私政策模板

```
学术龙虾 v2 隐私政策

生效日期：2026-03-16

1. 我们收集什么信息
   学术龙虾 v2 不收集任何个人身份信息。

2. 我们如何使用信息
   不适用。

3. 我们如何共享信息
   我们不与任何第三方共享信息。

4. 数据安全措施
   所有数据本地存储，可选加密。

5. 您的权利
   您有权访问、更正、删除您的数据。

6. 联系我们
   如有问题，请联系 security@academic-lobster.org。
```

---

**文档版本：** 2.0

**最后更新：** 2026-03-16

🦞 **学术龙虾 v2，为每一位认真做研究的人服务。**
