import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        update = json.loads(self.rfile.read(length))
        message = update.get("message", {})
        chat = message.get("chat", {})
        text = message.get("text", "")

        if chat and text:
            reply = "Привет! Я бот автоподбора 🚗 Скоро начну искать выгодные машины в Новосибирске!"
            data = json.dumps({
                "chat_id": chat["id"],
                "text": reply
            }).encode()

            token = os.environ["BOT_TOKEN"]
            request = urllib.request.Request(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data=data,
                headers={"Content-Type": "application/json"}
            )
            urllib.request.urlopen(request, timeout=10)

        self.send_response(200)
        self.end_headers()
