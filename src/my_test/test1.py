# from langchain_openai import ChatOpenAI
#
# from agent.env_utils import LOCAL_BASE_URL
# from agent.my_llm import baseqwen,basedeepseek
#
#
# # basedeepseek = ChatOpenAI(
# #     api_key='',  # 从环境变量获取API密钥
# #     base_url=LOCAL_BASE_URL,  # API基础URL
# #     model="Qwen3.5-9B",  # 模型名称
# #     temperature=0.8,  # 可选参数，控制生成文本的多样性
# #     extra_body={'chat_template_kwargs':{'enable_thinking':True}},
# # )
# response = basedeepseek.invoke("请介绍一下什么是深度学习")
# print(response)


import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",  # Local subprocess communication
                "command": "python",
                # Absolute path to your math_server.py file
                "args": ["/path/to/math_server.py"],
            },
            "weather": {
                "transport": "http",  # HTTP-based remote server
                # Ensure you start your weather server on port 8000
                "url": "http://localhost:8000/mcp",
            }
        }
    )

    tools = await client.get_tools()
    agent = create_agent(
        "claude-sonnet-4-6",
        tools
    )
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "计算(3 + 5) x 12?"}]}
    )
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "郑州天气怎么样?"}]}
    )
    print(math_response)
    print(weather_response)

if __name__ == "__main__":
    asyncio.run(main())
