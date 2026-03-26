from typing import Any, Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, create_model

from agent.my_llm import zhipuai_client


#工具参数
class SearchArgs(BaseModel):
    query:str = Field(...,description='需要进行联网查询的信息')

class MyWebSearchTool(BaseTool):
    name:str="web_search2"
    description:str ="使用这个工具可以进行网络搜索"
    #下面的工具参数有两种写法
    #第一种，用上面的类
    # args_schema: Type[BaseModel] =SearchArgs
    #第二种，自定义一个类，继承一个父类的方式
    def __init__(self):
        super().__init__()
        self.args_schema = create_model(model_name:="SearchInput",query=(str,Field(...,description='需要进行联网查询的信息')))


    #_run表示私有化函数只能在当前类里调用，外部不可以调用
    def _run(self,query:str) -> Any:
        try:
            resp = zhipuai_client.web_search.web_search(
                search_engine='search_std',
                search_query=query,
            )

            if resp.search_result:
                return "\n\n".join([d.content for d in resp.search_result])
            return "没有搜索到任何结果"
        except Exception as e:
            print(e)
            return f"Error:{e}"


    #异步工具，配合异步agent使用
    async def _run(self,query:str) -> Any:
        return self.run(query=query)


