from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", "⚽ Nuovo alert GoalProfit!")

    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        requests.post(TELEGRAM_URL, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        })
        return "Message sent", 200
    else:
        return "Missing config", 500

@app.route("/", methods=["GET"])
def ping():
    return "🟢 Bot attivo", 200

if __name__ == "__main__":
    app.run(debug=True)
