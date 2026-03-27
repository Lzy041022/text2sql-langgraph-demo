from zhipuai import ZhipuAI

from agent.env_utils import DEEPSEEK_API_KEY, DEEPSEEK_API_URL
# from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek  # 添加对ChatDeepSeek的导入
#千问模型
# qwen = ChatOpenAI(
#     api_key=DASHSCOPE_API_KEY,  # 从环境变量获取API密钥
#     base_url=DASHSCOPE_API_URL,  # API基础URL
#     model="qwen3.5-flash", # 模型名称qwen3-max"
#     temperature=0.7,  # 可选参数，控制生成文本的多样性
#     max_tokens=1000,  # 可选参数，控制生成文本的最大长度
# )
#
#
# #deepseek模型
# #deepseek-chat 对应deepseek-v3.2-exp的非思考模式
# #deepseek-reasoner 对应deepseek-v3.2-exp的思考模式
# chatdeepseek = ChatOpenAI(
#     api_key=DEEPSEEK_API_KEY,  # 从环境变量获取API密钥
#     base_url=DEEPSEEK_API_URL,  # API基础URL
#     model="deepseek-chat",  # 模型名称
#     temperature=0.7,  # 可选参数，控制生成文本的多样性
#     max_tokens=1000,  # 可选参数，控制生成文本的最大长度
# )

deepseek =  ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,  # 从环境变量获取API密钥
    api_base=DEEPSEEK_API_URL,  # API基础URL
    model="deepseek-chat",  # 模型名称
    temperature=0.7,  # 可选参数，控制生成文本的多样性
    max_tokens=1000,  # 可选参数，控制生成文本的最大长度
)

# zhipuai_client = ZhipuAI(api_key=ZHIPU_API_KEY)
#
#
# xiaomi = ChatOpenAI(
#     api_key=MIMOXIAOMI_API_KEY,  # 从环境变量获取API密钥
#     base_url=MIMOXIAOMI_API_URL,  # API基础URL
#     model="mimo-v2-flash",  # 模型名称
#     temperature=0.7,  # 可选参数，控制生成文本的多样性
#     max_tokens=1000,  # 可选参数，控制生成文本的最大长度
# )





# baseqwen = ChatOpenAI(
#     api_key='',  # 从环境变量获取API密钥
#     base_url=LOCAL_BASE_URL,  # API基础URL
#     model="Qwen3.5-9B",  # 模型名称
#     temperature=0.8,  # 可选参数，控制生成文本的多样性
#     extra_body={'chat_template_kwargs':{'enable_thinking':True}},
# )
#
# basedeepseek= ChatOpenAI(
#     api_key='',  # 从环境变量获取API密钥
#     base_url=LOCAL_BASE_URL,  # API基础URL
#     model="deepseek-qwen3-8b",  # 模型名称
#     temperature=0.8,  # 可选参数，控制生成文本的多样性
#     #extra_body={'chat_template_kwargs':{'enable_thinking':True}},
#     extra_body={'chat_template_kwargs':{'enable_thinking':False}},#True和False没区别
#
# )
