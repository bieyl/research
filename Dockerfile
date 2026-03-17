# Academic Lobster v2 - Docker 部署配置
# 用于快速部署学术龙虾 v2 到服务器或本地环境

FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production
ENV FLASK_PORT=5001

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY src/ ./src/
COPY docs/ ./docs/
COPY assets/ ./assets/

# 创建数据目录
RUN mkdir -p /root/.academic_lobster

# 暴露端口
EXPOSE 5001

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5001/health')" || exit 1

# 启动应用
CMD ["python", "src/web_app_v3.py", "--host", "0.0.0.0", "--port", "5001"]
