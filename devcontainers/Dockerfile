FROM mcr.microsoft.com/devcontainers/python:3.10

# 设置工作目录
WORKDIR /workspaces/text2sql

# 安装系统依赖（如 MySQL 客户端）
RUN apt-get update && apt-get install -y \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口：Streamlit (8501) 和 FastAPI (8000)
EXPOSE 8501
EXPOSE 8000