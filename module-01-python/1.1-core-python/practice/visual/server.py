import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

class GradeRequestHandler(SimpleHTTPRequestHandler):
    
    # 1. Handle CORS Preflight OPTIONS requests
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self._set_cors_headers()
        self.end_headers()

    # Helper method to add CORS headers
    def _set_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_POST(self):
        if self.path == '/api/grade':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            score = int(data.get('score', 0))
            


            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"

            # 2. Send response back with CORS headers included
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self._set_cors_headers()  # <--- Essential CORS header added here
            self.end_headers()
            
            response = {"grade": grade}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, GradeRequestHandler)
    print("Server running at http://localhost:8000/")
    httpd.serve_forever()

if __name__ == '__main__':
    run()