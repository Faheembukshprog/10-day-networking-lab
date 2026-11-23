import html
import json
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8090


class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        name = params.get("name", ["guest"])[0]

        if parsed.path == "/":
            body = """
            <h2>Day 9 Local Security Training Lab</h2>
            <p>Compare endpoints on <code>127.0.0.1:8090</code>:</p>
            <ul>
              <li><a href="/reflect-unsafe?name=Alice">/reflect-unsafe?name=Alice</a> (unencoded reflection + verbose banner)</li>
              <li><a href="/reflect-safe?name=Alice">/reflect-safe?name=Alice</a> (HTML-escaped output + security headers)</li>
              <li><a href="/debug-info">/debug-info</a> (simulated sensitive internal config exposure)</li>
            </ul>
            """.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

        elif parsed.path == "/reflect-unsafe":
            # Intentionally unescaped output for training observation only
            body = f"<p>Welcome, {name}</p>".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("X-Powered-By", "Day9-Insecure-Demo/0.1")
            self.end_headers()
            self.wfile.write(body)

        elif parsed.path == "/reflect-safe":
            safe_name = html.escape(name, quote=True)
            body = f"<p>Welcome, {safe_name}</p>".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Content-Security-Policy", "default-src 'self'")
            self.end_headers()
            self.wfile.write(body)

        elif parsed.path == "/debug-info":
            # Simulates accidental exposure of internal lab details
            payload = {
                "lab": "Day 9 Vulnerable Environment Evaluation",
                "bound_interface": HOST,
                "port": PORT,
                "simulated_note": "Never expose debug/config endpoints in production.",
            }
            body = json.dumps(payload, indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not found")

    def log_message(self, format, *args):
        print(f"[LAB] {self.address_string()} - {format % args}")


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), LabHandler)
    print(f"Serving Day 9 training lab on http://{HOST}:{PORT} (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped Day 9 lab server.")
        server.server_close()
