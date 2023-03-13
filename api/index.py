from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from ..TurtleBackend.Parser import Parser

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        s = self.path
        print(s)
        # Content-Type: application/json
        # {"text": "fd 100"}
        text = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        textJson = json.dumps(text)
        print(text)
        text = json.loads(text)
        print(text)
        textInput = text["text"]
        print(textInput)
        print(text)
        parser = Parser()
        parser.parse(textInput)
        parser.execute()
        parser.save("temp.svg")
        response = 200
        self.send_response(response)
        # res the svg file
        self.send_header('Content-type','image/svg+xml')
        self.end_headers()
        with open("temp.svg", "r") as f:
            svg = f.read()
        self.wfile.write(bytes(svg, "utf8"))
        return
    

# if __name__ == '__main__':
#     from http.server import HTTPServer
#     server = HTTPServer(('localhost', 8080), handler)
#     print('Starting server, use <Ctrl-C> to stop')
#     server.serve_forever()

