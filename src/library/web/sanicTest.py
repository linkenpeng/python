'''
https://blog.csdn.net/qq_44000141/article/details/138255465
一、Sanic 简介及特性
说到 Python Web 框架， 你可能会想到 Flask、Django、Tornado、FastAPI这些；而本文将向大家介绍另一个 Python Web 框架 —— Sanic。
它是一个 Python 3.8+ Web 服务器和 Web 框架，旨在快速运行。它允许使用 Python 3.5 中添加的 async/await 语法，这使您的代码非阻塞且快速。

应用场景
如果你希望快速搭建一个小型的 API 项目，又对速度有非常大的需求，那 Sanic 无疑是你的天选框架！

Sanic 特性
直接支持生产环境部署
高度可扩展
内置快速网络服务器
具有异步支持
使用 Redoc、Swagger 的 OpenAPI 文档
CORS 保护等

pip install sanic

Jemeter: avarage:55ms TPS: 1700 

stop: 
lsof -i :8000 | awk 'NR>1 {print $2}' |xargs kill -9
'''
from sanic import Sanic
from sanic.response import json
from datetime import datetime
import multiprocessing

app = Sanic("SanicAPP")
HOST = "localhost"
PORT = 7777

app.config.FALLBACK_ERROR_FORMAT = 'json'
app.config.ACCESS_LOG = True

async def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/getdatetime')
async def getdatetime(request):
    return json({"now": await get_datetime(), 'server_name': request.server_name, 'path': request.path})

@app.route('/')
def hello(request):
    data = 'Hello, Sanic!'
    response = {"code":200, "message":"success", "data":data}
    return json(response)


async def request_parse(request):
    platform, chain, address = 'platform', 'chain', 'address'
    if request.method == 'POST':
        parameters = request.json
        platform, chain, address = parameters['platform'], parameters['chain'], parameters['address']
    elif request.method == 'GET':
        parameters = request.args
        platform, chain, address = parameters['platform'][0], parameters['chain'][0], parameters['address'][0]
    print(f'请求参数为{platform}, {chain}, {address}')
    return platform, chain, address


if __name__ == "__main__":
    app_workers = multiprocessing.cpu_count() // 5
    print('app_workers:', app_workers)
    app.run(host=HOST, debug=False, auto_reload=True, workers=app_workers)


