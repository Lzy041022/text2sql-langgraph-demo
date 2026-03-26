import streamlit as st
import sys
import os

# 将 src 目录添加到 Python 路径，以便正确导入 agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.text_to_sql_agent import agent

st.set_page_config(page_title="Text2SQL 智能体", page_icon="🤖")

st.title("🤖 Text2SQL 智能助手")
st.markdown("欢迎使用 Text2SQL 智能助手！输入你的问题，我将为你生成 SQL 并查询数据库。")

# 初始化聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入
if prompt := st.chat_input("问问你的数据库..."):
    # 显示用户输入
    st.chat_message("user").markdown(prompt)
    # 添加到历史
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 调用智能体并流式输出
        # 注意：这里 agent.stream 返回的是各步骤的结果，我们寻找最终回答
        try:
            with st.spinner("思考中..."):
                steps = agent.stream(
                    input={'messages': [{'role': 'user', 'content': prompt}]},
                    stream_mode="values"
                )
                
                # 获取最后一条消息
                last_step = None
                for step in steps:
                    last_step = step
                
                if last_step and 'messages' in last_step:
                    final_message = last_step['messages'][-1]
                    full_response = final_message.content
                    message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"发生错误: {e}")
            full_response = "抱歉，我无法处理这个请求。"
        
        # 添加到历史
        st.session_state.messages.append({"role": "assistant", "content": full_response})

st.sidebar.info("这是一个基于 LangGraph 和 SQL 智能体的 Text2SQL 应用示例。")
