import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = int(os.environ.get("PORT", 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"Serving on port {port}")
HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler).serve_forever()
