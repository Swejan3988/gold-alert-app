import sqlite3
from gold_price import get_gold_price

def send_sms(mobile, price):
    print(f"📲 SMS sent to {mobile}: Gold price reached ₹{price}")

def check_alerts():
    current_price = get_gold_price()
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("SELECT mobile, target_price FROM users")
    users = cur.fetchall()

    for mobile, target in users:
        if current_price <= target:
            send_sms(mobile, current_price)

    conn.close()
