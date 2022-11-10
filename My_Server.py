
import json
import io
from http.server import BaseHTTPRequestHandler, HTTPServer

server_Port = 8080

class My_Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title> Oshri Server :) </title></head>", "utf-8"))
        self.wfile.write(bytes("<p> Hello </p>", "utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        post_body = self.rfile.read(int(self.headers.get('Content-Length')))
        fix_bytes_value = post_body.replace(b"'", b'"')
        my_json = json.load(io.BytesIO(fix_bytes_value))
        name = "hello " + my_json.get('name')

        self.wfile.write(bytes(f'{name}', "utf-8"))
        print(name)