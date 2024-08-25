'''

Tornado是一个Python web框架和异步网络库，它使用非阻塞网络I/O来支持数以万计的连接，
这使得它非常适合于长轮询、WebSockets和其他需要高并发的应用。

pip install tornado
'''

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 在这里处理GET请求
        self.write("Hello, Tornado!")

# 定义应用程序的路由
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8088)  # 监听8088端口
    print("Server is running on http://localhost:8088")
    tornado.ioloop.IOLoop.current().start()  # 启动IOLoop
