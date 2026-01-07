import random
import sqlite3
import datetime

def generate_otp():
    return str(random.randint(100000, 999999))

def save_otp(conn, mobile, otp):
    expires = datetime.datetime.now() + datetime.timedelta(minutes=5)
    conn.execute(
        "INSERT INTO otps (mobile, otp, expires_at) VALUES (?, ?, ?)",
        (mobile, otp, expires)
    )
    conn.commit()

def verify_otp(conn, mobile, otp):
    cur = conn.cursor()
    cur.execute("""
        SELECT otp FROM otps 
        WHERE mobile=? AND otp=? AND expires_at > CURRENT_TIMESTAMP
    """, (mobile, otp))

    result = cur.fetchone()
    return result is not None
