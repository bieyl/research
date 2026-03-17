# GitHub 推送指南

由于需要 GitHub 认证，请使用以下任一方式推送更改：

## 方式 1：使用 Personal Access Token（推荐）

```bash
# 1. 生成 Token
# 访问 https://github.com/settings/tokens
# 创建新的 token，勾选 repo 权限

# 2. 推送代码
cd /home/admin/openclaw/workspace/research
git remote set-url origin https://<YOUR_TOKEN>@github.com/bieyl/research.git
git push origin main
```

## 方式 2：使用 SSH

```bash
# 1. 生成 SSH key（如果没有）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 添加 SSH key 到 GitHub
# 访问 https://github.com/settings/keys
# 复制 ~/.ssh/id_ed25519.pub 的内容

# 3. 切换 remote 为 SSH
cd /home/admin/openclaw/workspace/research
git remote set-url origin git@github.com:bieyl/research.git
git push origin main
```

## 方式 3：使用 GitHub Desktop

1. 下载 GitHub Desktop: https://desktop.github.com/
2. 登录 GitHub 账号
3. 克隆仓库到本地
4. 将更改的文件复制到克隆的目录
5. 在 GitHub Desktop 中 commit 并 push

---

## 本次更新内容

✅ **README.md** - 重写为专业版本（参考 MatClaw 风格）
✅ **README_zh.md** - 新增中文版本
✅ **系统架构图** - ASCII art 架构图
✅ **技术栈表格** - 清晰的技术说明
✅ **BibTeX 引用** - 学术引用格式
✅ **文档导航** - 完整的文档链接

## 组委会链接修复

回复组委会时，使用以下正确链接：

| 材料类型 | 正确链接 |
|---------|---------|
| 项目说明书 | https://github.com/bieyl/research |
| 代码仓库 | https://github.com/bieyl/research |
| 项目海报 | https://github.com/bieyl/research/blob/main/assets/poster.md |
| 演示视频 | （需要上传 B 站后提供链接） |

---

**推送后请验证：**
1. 访问 https://github.com/bieyl/research 确认 README 已更新
2. 确认 README_zh.md 可见
3. 检查所有文档链接是否正确
