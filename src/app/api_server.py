from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sys
import os

# 将 src 目录添加到 Python 路径，以便正确导入 agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.text_to_sql_agent import agent

app = FastAPI()

class QueryRequest(BaseModel):
    prompt: str

@app.post("/query")
async def query_agent(request: QueryRequest):
    try:
        # 调用智能体
        steps = agent.stream(
            input={'messages': [{'role': 'user', 'content': request.prompt}]},
            stream_mode="values"
        )
        
        # 获取最后一条消息
        last_step = None
        for step in steps:
            last_step = step
        
        if last_step and 'messages' in last_step:
            final_message = last_step['messages'][-1]
            return {"response": final_message.content}
        else:
            raise HTTPException(status_code=500, detail="没有返回结果")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open(os.path.join(os.path.dirname(__file__), "index.html"), "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
