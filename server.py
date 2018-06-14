# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/6/14 14:01'

from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模版
    Page = '''\
    <html>
    <body>
    <p>Hello, web!</p>
    </body>
    </html>
    '''

    # 处理一个get请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content_Type","text/html")
        self.send_header("Content_Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()

# visit http://127.0.0.1:8080/ in browser and you will get 'Hello, web!' in the pages

# server return:
# 127.0.0.1 - - [14/Jun/2018 14:20:06] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [14/Jun/2018 14:20:06] "GET /favicon.ico HTTP/1.1" 200 -

