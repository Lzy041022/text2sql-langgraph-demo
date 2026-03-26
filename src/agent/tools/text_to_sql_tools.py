from typing import Any
from typing import List, Optional,Annotated#这个地方注意一下
#from sqlalchemy.sql.annotation import Annotated
from langchain_core.tools import BaseTool, InjectedToolArg
from langgraph.prebuilt import ToolRuntime


from agent.utils.db_utils import MySQLDatabaseManager
from pydantic import create_model, Field, ConfigDict, BaseModel
from agent.utils.log_utils import log



class ListTablesTool(BaseTool):
    """
    列出数据库中的所有表及其描述信息
    """
    name:str = "sql_db_list_tables"
    description:str = "列出MySQL数据库中的所有表名及其描述信息。当需要了解数据库中有哪些表以及表的用途时使用。"

    #数据库管理实例
    db_manager:MySQLDatabaseManager

    def _run(self) -> str:
        try:
            tables_info = self.db_manager.get_tables_with_comments()

            result = f"数据库中共有{len(tables_info)}个表：\n\n"
            for i,tables_info in enumerate(tables_info):
                table_name = tables_info['table_name']
                table_comment = tables_info['table_comment']

                #处理空描述的情况
                if not table_comment or table_comment.isspace():
                    description_siaplay = "(暂无描述)"
                else:
                    description_siaplay = table_comment

                result += f"{i+1}.表名：{table_name}\n"
                result += f"   描述：{description_siaplay}\n"

            return result
        except Exception as e:
            log.exception(e)
            return f"列出表时出错：{str(e)}"

    async def _arun(self) -> str:
        """异步执行"""
        return self._run()


class TableSchemaToolArgs(BaseModel):
    """表模式工具参数"""
    table_names:Optional[str] = Field(None,description='逗号分隔的表名列表，例如：t_usermodel,t_rolemodel')
    runtime: Annotated[ToolRuntime,InjectedToolArg] = Field(...,description='运行时上下文')
    #添加配置允许任意类型
    model_config = ConfigDict(arbitrary_types_allowed=True)
class TableSchemaTool(BaseTool):
    """
    获取表的模式信息
    """
    name:str = "sql_db_schema"
    description:str = "列出MySQL数据库中的所有表名及其描述信息，包括列定义、主外键等。输入应为逗号分隔的表名列表，以获取使用表的信息。"

    #数据库管理实例
    db_manager:MySQLDatabaseManager

    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        # self.db_manager = db_manager
        #self.args_schema = create_model("TobleSchemaToolArgs",table_names=(Optional[str],Field(...,description = '逗号隔开的表名列表，例如：t_usermodel,t_rolemodel')))
        self.args_schema = TableSchemaToolArgs

    #参数注入的方式:得到一个运行时对象（Runtime）,在通过runtime得到state
    def _run(self,table_names:Optional[str]=None,runtime: Annotated[ToolRuntime,InjectedToolArg] = None) -> str:
        """
        返回表结构信息
        """
        try:
            print(f'当前运行的状态：{runtime.state}')
            print(f'当前静止的状态：{runtime.context}')

            table_list = None
            if table_names:
                table_list = [name.strip() for name in table_names.split(',')if name.strip()]

            schema_info = self.db_manager.get_table_schema(table_list)
            return schema_info if schema_info else  "未找到匹配的表"
        except Exception as e:
            log.exception(e)
            return f"获取表模式信息时出差错：{str(e)}"

    async def _arun(self,table_names:Optional[str]=None) -> str:
        return self._run(table_names)


class SQLQueryTool(BaseTool):
    name: str = "sql_db_query"
    description: str ="在MySQL数据库上执行安全的SELECT查询并返回结果。输入应为有效的SQL SELECT查询语句。"

    db_manager: MySQLDatabaseManager

    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        # self.db_manager = db_manager
        self.args_schema = create_model("SQLQueryToolArgs",query=(str,Field(...,description = '有效的SQL SELECT查询语句')))

    def _run(self,query: str) ->str:
        """
        执行工具逻辑
        """

        try:
            result = self.db_manager.excute_query(query)
            return result
        except Exception as e:
            return f"执行查询时出错：{str(e)}"

    async def _arun(self,query:str) -> str:
        return self._run(query)


class SQLQueryCheckerTool(BaseTool):
    """检查SQL查询语法"""

    name:str = "sql_db_query_checker"
    description:str = "检查SQL查询语句的语法是否正确，提供验证反馈。输入应为要检测的SQL查询。"
    db_manager: MySQLDatabaseManager

    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        # self.db_manager = db_manager
        self.args_schema = create_model("SQLQueryCheckerToolArgs",query=(str,Field(...,description = '需要继续检查的SQL语句')))


    def _run(self,query:str) ->str:
        """执行工具逻辑"""
        try:
            result = self.db_manager.validate_query(query)
            return result
        except Exception as e:
            return f"检查查询时出错：{str(e)}"
    async def _arun(self,query:str) -> str:
        return self._run(query)



if __name__ == '__main__':
    #配置数据库连接信息
    username = 'root'
    password = '123456'
    host = '127.0.0.1'
    port = 3306
    database = 'mysql'
    #构建连接字符串
    connection_string = f"mysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4"
    manager = MySQLDatabaseManager(connection_string)
    tool = ListTablesTool(db_manager=manager)#测试第一个工具
    print(tool.invoke({}))
    # tool = TableSchemaTool(db_manager=manager)#测试第二个工具
    # print(tool.invoke({'table_names':['albums','artists','customers']}))
    # tool = SQLQueryTool(db_manager=manager)#第三个
    # print(tool.invoke({'query': 'select * from employees'}))
    # tool = SQLQueryCheckerTool(db_manager=manager)#第四个
    # print(tool.invoke({'query': 'select count(*) from albums'}))











































