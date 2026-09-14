import functools
import http.server

DIRECTORY = "/Users/yeesh/Desktop/Web F4F"
PORT = 5173

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY} on port {PORT}")
    httpd.serve_forever()
