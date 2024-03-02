
#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
pip install qianfan

# pip安装 fastapi 和 uvicorn
# 执行 "uvicorn qianfan:app --host=0.0.0.0 --port=8000 --reload" 启动服务端
'''
import os
import requests
from fake_useragent import UserAgent
import redis
import json
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

if(os.getenv('QIANFAN_ACCESS_KEY') == None): 
    os.environ["QIANFAN_ACCESS_KEY"] = ""
if(os.getenv('QIANFAN_SECRET_KEY') == None): 
    os.environ["QIANFAN_SECRET_KEY"] = ""
os.environ["REDIS_HOST"] = "localhost"
os.environ["REDIS_PORT"] = "6379"

print(os.environ)

ua = UserAgent()
headers = {
 "User-Agent": ua.random
}

app = FastAPI()

# 允许前端跨域调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_redis_client():
    client = redis.StrictRedis(host=os.environ["REDIS_HOST"] , port=os.environ["REDIS_PORT"])
    return client

def get_access_token_info():
    print(os)
    redis = get_redis_client()
    cache_key = 'test:qianfan:access_token'
    cache_value = redis.get(cache_key)
    #print(f"get from cache: {cache_value}")
    if(len(cache_value) > 0):
        access_token_info = json.loads(cache_value)
        #print(access_token_info['access_token'])
        return access_token_info

    access_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
    ACCESS_KEY = os.environ["QIANFAN_ACCESS_KEY"]
    SECRET_KEY = os.environ["QIANFAN_SECRET_KEY"]
    token_url = access_token_url % (ACCESS_KEY, SECRET_KEY)

    data = {}
    response = requests.post(token_url, data, headers=headers)
    print(response.content)
    if(response.content > 0):
        access_token_info = json.loads(response.content)
        redis.set(cache_key, response.content, ex=access_token_info['expires_in'])
        return access_token_info
    else:
        return {}
    
def get_access_token():
    access_info = get_access_token_info()
    return access_info["access_token"]

def get_stream_response(prompt):
    source = "&sourceVer=0.0.1&source=app_center&appName=streamDemo"
    # 大模型接口URL
    base_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant"
    url = base_url + "?access_token=" + get_access_token() + source
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    return requests.post(url, headers=headers, data=payload, stream=True)

def gen_stream(prompt):
    response = get_stream_response(prompt)
    for chunk in response.iter_lines():
        chunk = chunk.decode("utf8")
        if chunk[:5] == "data:":
            chunk = chunk[5:]
        yield chunk

@app.post("/eb_stream")    # 前端调用的path
async def eb_stream(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    return StreamingResponse(gen_stream(prompt))

if __name__ == '__main__':
    uvicorn.run(app='qianfan:app', host="127.0.0.1", port=8000, reload=True)