import json
import http.server
import logging

from client import client, send_msg, secret_key
from movie_recommend import get_recommended_movie
from emo_platform import EmoPlatformError


class Handler(http.server.BaseHTTPRequestHandler):
    def _send_status(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

    def do_POST(self):
        KEY_WORD = "おすすめの映画を教えて"

        if not secret_key == self.headers["X-Platform-Api-Secret"]:
            self._send_status(401)
            return

        content_len = int(self.headers['content-length'])
        request_body = json.loads(self.rfile.read(content_len).decode('utf-8'))

        try:
            cb_func, emo_webhook_body = client.get_cb_func(request_body)
        except EmoPlatformError:
            self._send_status(501)
            return

        cb_func(emo_webhook_body)
        self._send_status(200)
        
        if hasattr(emo_webhook_body.data, 'message') and emo_webhook_body.data.message.message.ja == KEY_WORD:
            send_msg(get_recommended_movie())

def run_server():
    with http.server.HTTPServer(('', 8000), Handler) as httpd:
        logging.info("Server running on port 8000...")
        httpd.serve_forever()
