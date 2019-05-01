import socket
import http.server
import socketserver

# tasklist
# /IM py37.exe /F
# 
hostname = socket.gethostname()

IP = socket.gethostbyname(hostname)
print('serving on:', IP)
print ('IP Address of server: ', socket.gethostbyaddr(IP))

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', 5000), Handler) as httpd:
    httpd.serve_forever()
