"""Dev server: python -m app.main (PORT, default 8000)."""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from app import index


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = index.ROUTES.get(self.path.split("?")[0])
        if self.path == "/health":
            body = {"ok": True, "service": "search-service"}
        elif route:
            body = route()
        else:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"search-service listening on :{port}")
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()
