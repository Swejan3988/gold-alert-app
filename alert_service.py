import sqlite3
import os
from gold_price import get_gold_price

# ✅ Same Azure-safe DB path
BASE_DIR = os.environ.get("HOME", os.getcwd())
DB_PATH = os.path.join(BASE_DIR, "site", "wwwroot", "users.db")

def send_sms(mobile, price):
    # TODO: Replace with real SMS provider (Fast2SMS / Twilio)
    print(f"📲 SMS sent to {mobile}: Gold price reached ₹{price}")

def check_alerts():
    current_price = get_gold_price()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT mobile, target_price FROM users")
    users = cur.fetchall()

    for mobile, target in users:
        if current_price <= target:
            send_sms(mobile, current_price)

    conn.close()
