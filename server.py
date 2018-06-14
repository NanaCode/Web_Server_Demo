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
    <table>
    <tr>  <td>Header</td>         <td>Value</td>          </tr>
    <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
    <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    </table>
    </body>
    </html>
    '''

    # 处理一个get请求
    def do_GET(self):
        page = self.create_page()
        self.send_content(page)

    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        page = self.Page.format(**values)
        return page

    def send_content(self, page):
        self.send_response(200)
        self.send_header("Content_Type","text/html")
        self.send_header("Content_Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))


if __name__ == '__main__':
    server_address = ('', 8080)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()

# visit http://127.0.0.1:8080/ in browser and you will get somethind as below shown' in the pages


# Header	Value
# Date and time	Thu, 14 Jun 2018 06:57:19 GMT
# Client host	127.0.0.1
# Client port	59020
# Command	GET
# Path	/

# server return:
# 127.0.0.1 - - [14/Jun/2018 14:20:06] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [14/Jun/2018 14:20:06] "GET /favicon.ico HTTP/1.1" 200 -

# visit http://127.0.0.1:8080/something.html


# Header	Value
# Date and time	Thu, 14 Jun 2018 07:52:47 GMT
# Client host	127.0.0.1
# Client port	61872
# Command	GET
# Path	/something.html