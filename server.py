#!/usr/bin/env python3
"""
BAE Systems Strategic Analytics & Transformation Suite
Simple HTTP Local Web Server Launcher
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 70)
        print(f" BAE Systems Strategic Analytics Suite Running at:")
        print(f" {url}")
        print(" Press Ctrl+C to stop the server.")
        print("=" * 70)
        
        # Open browser automatically
        try:
            webbrowser.open(url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    run_server()
