# Text2SQL 智能数据库查询助手

## 🚀 项目简介
Text2SQL 是一个基于大语言模型（LLM）和 LangGraph 构建的智能体（Agent）系统。它旨在消除自然语言与结构化查询语言（SQL）之间的鸿沟，允许非技术人员通过直接对话的方式，轻松查询、分析和获取数据库中的信息。

## ✨ 核心特性
- **自然语言交互**：直接使用中文提问，如“去年销售额最高的前三个客户是谁？”。
- **自主 Schema 探索**：Agent 会自动列出数据库表名并查看表结构，无需手动配置元数据。
- **SQL 自动修正**：内置 SQL 检查工具，当生成的 SQL 执行失败时，Agent 会根据错误信息自动重写并尝试修复。
- **多模型适配**：深度集成通义千问 (Qwen)、DeepSeek、智谱 AI 等主流大模型。
- **灵活的展示层**：
  - **Python 原生界面**：基于 Streamlit 快速构建。
  - **现代化 Web 界面**：基于 FastAPI 和 HTML5/Tailwind CSS。

## 🛠️ 技术栈
- **AI 框架**: [LangChain](https://github.com/langchain-ai/langchain) / [LangGraph](https://github.com/langchain-ai/langgraph)
- **大语言模型**: Qwen-3.5, DeepSeek-V3, 智谱 ChatGLM
- **数据库支持**: MySQL (核心支持), SQLite (Chinook 示例)
- **Web 服务**: FastAPI, Uvicorn
- **前端界面**: Streamlit, HTML5, Tailwind CSS

## 📂 目录结构说明
```text
text2sql/
├── src/
│   ├── agent/               # 智能体核心逻辑
│   │   ├── my_llm.py        # LLM 模型配置与初始化
│   │   ├── text_to_sql_agent.py # Agent 状态机定义
│   │   └── tools/           # 数据库操作工具集 (SQL执行、架构查询等)
│   ├── app/                 # 前端应用文件夹
│   │   ├── streamlit_app.py # Python Streamlit 聊天界面
│   │   ├── index.html       # HTML 静态页面
│   │   └── api_server.py    # FastAPI 后端接口
│   └── utils/               # 通用工具
│       ├── db_utils.py      # 数据库连接管理
│       └── log_utils.py     # 系统日志记录
├── chinook.db               # 示例 SQLite 数据库
└── README.md                # 项目说明文件
```

## 🚥 快速开始

### 1. 环境准备
确保您的 Python 版本 >= 3.9，并安装依赖：
```bash
pip install langchain langchain-openai langchain-deepseek fastapi uvicorn streamlit zhipuai pymysql
```

### 2. 配置 API 密钥
在 `src/agent/env_utils.py` 或环境变量中设置您的 LLM API Key（如 `DASHSCOPE_API_KEY`）。

### 3. 运行应用

#### 运行 Streamlit 界面 (推荐)
```bash
streamlit run src/app/streamlit_app.py
```

#### 运行 Web 服务 (FastAPI + HTML)
```bash
python src/app/api_server.py
```
启动后在浏览器访问：`http://localhost:8000`

## 🛡️ 安全提示
本项目目前处于原型开发阶段。请注意，Agent 具有执行 SQL 的权限。虽然代码中已明确禁止 DML 语句（INSERT/UPDATE/DELETE），但建议仅在受控环境下连接生产数据库。
