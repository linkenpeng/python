'''

Tornado是一个Python web框架和异步网络库，它使用非阻塞网络I/O来支持数以万计的连接，
这使得它非常适合于长轮询、WebSockets和其他需要高并发的应用。

pip install tornado
'''

import tornado.ioloop
import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 在这里处理GET请求
        data = 'Hello, Tornado!'
        response = {"code":200, "message":"success", "data":data}
        time.sleep(0.1)
        self.write(response)

# 定义应用程序的路由
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    app = make_app()
    # 创建 HTTPServer 实例并传入 Tornado 应用
    http_server = tornado.httpserver.HTTPServer(app)
    # 监听 8888 端口
    http_server.listen(8888)
    # http_server.bind(8888, '0.0.0.0', backlog=2048)
    # http_server.start(3) # only on linux
    print("Server is running on http://localhost:8888")
    # 启动 IOLoop
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()