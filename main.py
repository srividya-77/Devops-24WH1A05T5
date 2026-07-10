import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleRegistryHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Handles CORS browser handshakes automatically
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/v1/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            user_payload = json.loads(post_data.decode('utf-8'))
            
            # SAFE STORAGE: Saves data directly into a local text file
            with open("registrations_log.txt", "a") as file:
                file.write(json.dumps(user_payload) + "\n")
                
            print("Successfully Saved Entry to File:", user_payload['username'])
            
            # Response Header Setup
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {"status": "success", "message": "Saved to text log!"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

# Starts the native server on port 8000
if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8000), SimpleRegistryHandler)
    print("Zero-dependency server running at http://127.0.0.1:8000")
    server.serve_forever()
