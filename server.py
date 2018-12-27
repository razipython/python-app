import http.server
import socketserver
import cgi
import cgitb

cgitb.enable()


Handler = http.server.SimpleHTTPRequestHandler
CGIHandler = http.server.CGIHTTPRequestHandler


class MyRequestHandler(CGIHandler):
    def do_GET(self):
        pass


PORT = 8000


with socketserver.TCPServer(("http://127.0.0.1", PORT), CGIHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

