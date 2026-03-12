# 🦞 学术龙虾安装指南

---

## 1. 系统要求

| 项目 | 最低要求 | 推荐配置 |
|------|----------|----------|
| 操作系统 | Windows 10 / macOS 10.15 / Ubuntu 20.04 | Windows 11 / macOS 12 / Ubuntu 22.04 |
| Python 版本 | 3.9 | 3.10+ |
| 内存 | 4GB | 8GB+ |
| 存储 | 500MB | 1GB+ |
| 网络 | 可选（支持离线） | - |

---

## 2. 快速安装

### 2.1 方法一：源码安装（推荐开发者）

```bash
# 1. 克隆仓库
git clone https://github.com/your-repo/academic-lobster.git
cd academic-lobster

# 2. 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行程序
python src/main.py
```

### 2.2 方法二：pip 安装（推荐用户）

```bash
# 安装稳定版
pip install academic-lobster

# 运行程序
academic-lobster
```

### 2.3 方法三：桌面应用（推荐非技术用户）

**Windows:**
1. 下载 `academic-lobster-setup.exe`
2. 双击运行安装程序
3. 按提示完成安装
4. 桌面快捷方式启动

**macOS:**
1. 下载 `academic-lobster.dmg`
2. 拖拽到应用程序文件夹
3. 启动台启动

**Linux:**
1. 下载 `academic-lobster.AppImage`
2. 赋予执行权限：`chmod +x academic-lobster.AppImage`
3. 运行：`./academic-lobster.AppImage`

---

## 3. 依赖说明

### 3.1 核心依赖

```txt
# PDF 处理
PyMuPDF>=1.21.0
pdfplumber>=0.9.0

# NLP 处理
nltk>=3.8
spacy>=3.5
transformers>=4.30.0

# 语音处理
SpeechRecognition>=3.10.0
vosk>=0.3.45  # 离线语音识别
pyttsx3>=2.90  # 语音合成

# 数据存储
sqlite3  # Python 内置
SQLCipher  # 加密数据库
keyring>=24.0.0  # 密钥管理

# 图形界面
PyQt6>=6.5.0  # 或 Tkinter（Python 内置）

# 其他
jinja2>=3.1.0  # 模板引擎
cryptography>=41.0.0  # 加密库
```

### 3.2 可选依赖

```txt
# 云端 AI 推理
openai>=0.27.0
anthropic>=0.5.0

# 智能音箱接入
flask>=2.3.0  # API 服务

# 测试
pytest>=7.4.0
pytest-cov>=4.1.0
```

---

## 4. 首次配置

### 4.1 启动程序

```bash
python src/main.py
```

首次启动将自动创建配置文件和数据库。

### 4.2 配置向导

启动后将看到配置向导：

**步骤 1：选择数据目录**
```
请选择数据存储位置：
[默认] /home/user/.academic_lobster
[自定义] /path/to/your/data
```

**步骤 2：选择 AI 模式**
```
请选择 AI 推理模式：
[本地] 完全离线，精度适中
[云端] 需要网络，精度更高
```

**步骤 3：设置数据库密码**
```
请设置数据库加密密码：
建议：至少 12 位，包含大小写字母、数字、符号
```

**步骤 4：完成配置**
```
配置完成！
数据目录：/home/user/.academic_lobster
AI 模式：本地
数据库：已加密
```

---

## 5. 离线模式配置

### 5.1 下载离线模型

```bash
# 下载中文 NLP 模型
python -m spacy download zh_core_web_sm

# 下载离线语音识别模型（Vosk）
wget https://alphacephei.com/vosk/models/vosk-model-cn-0.22.tar.gz
tar -xzf vosk-model-cn-0.22.tar.gz
mv vosk-model-cn-0.22 ~/.academic_lobster/models/vosk-cn
```

### 5.2 配置离线模式

编辑配置文件 `~/.academic_lobster/config.json`：

```json
{
  "ai_mode": "local",
  "offline_models": {
    "nlp": "zh_core_web_sm",
    "speech": "vosk-cn"
  },
  "network": {
    "enabled": false
  }
}
```

---

## 6. 语音交互配置

### 6.1 桌面端语音

**Windows:**
```python
# 使用系统自带语音识别
import speech_recognition as sr
recognizer = sr.Recognizer()
# 自动使用 Windows Speech API
```

**macOS:**
```python
# 使用系统自带语音识别
import speech_recognition as sr
recognizer = sr.Recognizer()
# 自动使用 macOS Speech Framework
```

**Linux:**
```python
# 使用 Vosk 离线识别
from vosk import Model, KaldiRecognizer
model = Model("~/.academic_lobster/models/vosk-cn")
```

### 6.2 智能音箱接入

**小爱同学:**
1. 访问 https://miopen.mi.com/
2. 创建新技能
3. 配置回调 URL 指向学术龙虾 API
4. 发布技能

**天猫精灵:**
1. 访问 https://open.aligenie.com/
2. 创建新应用
3. 配置技能代码
4. 发布应用

---

## 7. 常见问题

### Q1: 安装时提示依赖冲突

**解决方案：**
```bash
# 创建新的虚拟环境
python -m venv venv
source venv/bin/activate

# 升级 pip
pip install --upgrade pip

# 重新安装
pip install -r requirements.txt
```

### Q2: 程序启动失败

**解决方案：**
```bash
# 查看详细错误日志
python src/main.py --verbose

# 重置配置
rm -rf ~/.academic_lobster
python src/main.py  # 重新配置
```

### Q3: 语音识别不工作

**解决方案：**
1. 检查麦克风权限
2. 测试麦克风：`arecord -l` (Linux) 或系统设置
3. 重新下载语音模型

### Q4: 数据库无法打开

**解决方案：**
```bash
# 检查数据库文件
ls -la ~/.academic_lobster/academic_lobster.db

# 重置数据库（会丢失数据）
rm ~/.academic_lobster/academic_lobster.db
python src/main.py  # 重新创建
```

---

## 8. 卸载

### 8.1 卸载程序

**pip 安装:**
```bash
pip uninstall academic-lobster
```

**桌面应用:**
- Windows: 控制面板 → 卸载程序
- macOS: 拖拽到废纸篓
- Linux: 删除 AppImage 文件

### 8.2 删除数据

```bash
# 删除所有数据（不可恢复！）
rm -rf ~/.academic_lobster
```

---

## 9. 更新

### 9.1 检查更新

```bash
academic-lobster --check-update
```

### 9.2 自动更新

```bash
# pip 安装
pip install --upgrade academic-lobster

# 源码安装
git pull
pip install -r requirements.txt
```

---

**安装指南版本：** v1.0

**最后更新：** 2026-03-12

**如有问题，请访问 GitHub Issues 或联系开发团队。**

🦞 学术龙虾，为每一位认真做研究的人服务。
