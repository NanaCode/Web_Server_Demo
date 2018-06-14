# Bug list:
## Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/web_server/server.py", line 30, in <module>
    server = HTTPserver(server_address, RequestHandler)
NameError: name 'HTTPserver' is not defined
TO_DO: Opps, HTTPserver should be HTTPServer

## Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/web_server/server.py", line 31, in <module>
    server.server_forever()
AttributeError: 'HTTPServer' object has no attribute 'server_forever'
TO_DO: Opps, server_forever should be serve_forever()