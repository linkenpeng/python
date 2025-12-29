'''
pip install fake_useragent
pip install fastapi
pip install uvicorn

Jemeter: avarage:56ms TPS: 1640 

stop: 
lsof -i :8000 | awk 'NR>1 {print $2}' |xargs kill -9

'''

from fake_useragent import UserAgent
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn

app = FastAPI()

# 允许前端跨域调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_headers():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }
    return headers

# 定义路由（使用装饰器将函数绑定到特定的路径和HTTP方法）
@app.get("/")
async def root():
    data = 'Hello, FastAPI!'
    response = {"code":200, "message":"success", "data":data}
    return response

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost')
