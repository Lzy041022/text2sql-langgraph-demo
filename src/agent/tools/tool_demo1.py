# from langchain_core.tools import tool
# from pydantic import BaseModel,Field

# from agent.my_llm import zhipuai_client


# #工具定义，两种方法（第二种在tool_demo2.py文件）
# ##一、使用装饰器@tool定义工具有一下两种方法（简单工具使用这种方法）
# ###方法一
# @tool('my_web_search')#parse_docstring=True解析下面的注释,这一段可能要移除
# def web_search(query:str)-> str:

#     """联网搜索工具，可以搜索所有公开信息

#     Args:
#         query:需要进行联网查询的信息。
#     Returns:
#         返回搜索的结果信息，该信息是一个文本字符串

#     """
#     #上面这部分必须写，用于工具的描述
#     #Returns部分也可以写在装饰器中，写在装饰器名字后面加description='     ',把parse_docstring=True去掉
#     try:
#         resp=zhipuai_client.web_search.web_search(
#             search_engine='search_std',
#             search_query=query,
#         )

#         if resp.search_result:
#             return "\n\n".join([d.content for d in resp.search_result])
#         return "没有搜索到任何结果"
#     except Exception as e:
#         print(e)
#         return f"Error:{e}"

# ###方法二
# # class SearchArgs(BaseModel):
# #     query:str = Field(...,description='需要进行联网查询的信息')
# #
# #
# # @tool('my_web_search',args_schema=SearchArgs,description='联网搜索工具，可以搜索所有公开信息')
# # def web_search2(query:str)-> str:
# #
# #     pass





# if __name__ == '__main__':
#     print(web_search.name)  #工具名字
#     print(web_search.description)  #工具描述
#     print(web_search.args)  #工具参数
#     print(web_search.args_schema.model_json_schema())  #工具的参数的json sxhema(描述jaon字符串)


#     result = web_search.invoke({'query':'如何使用langchain?'})
#     print(result)






