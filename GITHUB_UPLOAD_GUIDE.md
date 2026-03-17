# 📤 GitHub 上传指南 - 学术龙虾 v2

## 快速上传步骤（5 分钟）

### 方法 1：GitHub 网页上传（推荐）

#### 步骤 1：打开仓库
访问：https://github.com/bieyl/research

#### 步骤 2：创建项目文件夹
1. 点击 **"Add file"** 按钮
2. 选择 **"Create new file"**
3. 在文件名输入框输入：`academic-lobster-v2/README.md`
4. 粘贴 `GITHUB_UPLOAD_README.md` 文件内容
5. 滚动到页面底部，点击 **"Commit changes"**

#### 步骤 3：上传源代码
1. 再次点击 **"Add file"**
2. 选择 **"Upload files"**
3. 将以下文件夹拖拽到上传区域：
   - `src/` (整个文件夹)
   - `docs/` (整个文件夹)
   - `assets/` (整个文件夹)
   - `requirements.txt`
   - `competition-project-statement.md`
4. 等待上传完成
5. 点击 **"Commit changes"**

---

### 方法 2：Git 命令行（如果你已配置 SSH）

```bash
# 1. 克隆仓库
git clone git@github.com:bieyl/research.git
cd research

# 2. 复制项目文件
cp -r /home/admin/openclaw/workspace/academic-lobster/* ./academic-lobster-v2/

# 3. 提交并推送
git add academic-lobster-v2/
git commit -m "🦞 添加学术龙虾 v2 参赛作品"
git push origin main
```

---

## 上传后的链接

上传完成后，你将获得以下链接：

### 项目说明书
```
https://github.com/bieyl/research/blob/main/academic-lobster-v2/competition-project-statement.md
```

### GitHub 仓库
```
https://github.com/bieyl/research
```

### 项目 README
```
https://github.com/bieyl/research/blob/main/academic-lobster-v2/README.md
```

---

## 项目海报和演示视频

### 海报（2 选 1）

**方案 A：使用 UI 截图**
1. 打开已保存的截图：`/home/admin/.openclaw/media/browser/07eef111-b351-4e10-b34e-100edfa7f990.png`
2. 上传到图床（如 https://sm.ms/）
3. 复制图片链接

**方案 B：简单文字海报**
使用 `assets/poster-text.txt` 内容，创建为图片

### 演示视频（3 选 1）

**方案 A：屏幕录制**
- 使用 OBS 或系统自带录屏
- 录制 2-3 分钟演示（知识图谱、智能推荐、文献摘要）
- 上传到 B 站

**方案 B：截图 + 配音**
- 用多张 UI 截图
- 添加配音解说
- 用剪映合成

**方案 C：暂时使用占位符**
- 先提交，后续补充
- 填写："演示视频准备中，稍后更新"

---

## 填写注册表格

获得所有链接后，打开注册页面：
https://claw.lab.bza.edu.cn/participant/register

填写内容：

| 字段 | 填写内容 |
|------|---------|
| **项目说明书** | `https://github.com/bieyl/research/blob/main/academic-lobster-v2/competition-project-statement.md` |
| **项目海报** | [图床链接] |
| **演示视频** | [B 站链接] 或 "稍后更新" |
| **GitHub 仓库** | `https://github.com/bieyl/research` |

---

## 检查清单

- [ ] GitHub 仓库已创建/打开
- [ ] 项目文件已上传
- [ ] 可以正常访问 README
- [ ] 项目说明书链接可用
- [ ] 海报图片已上传（如有）
- [ ] 演示视频已上传（如有）
- [ ] 注册页面链接已填写
- [ ] 勾选同意参赛协议
- [ ] 点击提交

---

## 当前本地文件位置

```
/home/admin/openclaw/workspace/academic-lobster/
├── GITHUB_UPLOAD_README.md       # GitHub README（已准备）
├── competition-project-statement.md # 项目说明书（已准备）
├── src/                          # 源代码
├── docs/                         # 文档
├── assets/                       # 资源文件
└── requirements.txt              # 依赖
```

---

**上传完成后，告诉我链接，我帮你填写注册页面！** 🦞
