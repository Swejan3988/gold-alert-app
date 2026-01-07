from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# ✅ Azure-safe persistent DB path
BASE_DIR = os.environ.get("HOME", os.getcwd())
DB_PATH = os.path.join(BASE_DIR, "site", "wwwroot", "users.db")

def db_connection():
    return sqlite3.connect(DB_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mobile = request.form["mobile"]
        target_price = request.form["price"]

        conn = db_connection()
        cur = conn.cursor()

        # Create table if not exists
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mobile TEXT,
            target_price REAL
        )
        """)

        # Insert user data
        cur.execute(
            "INSERT INTO users (mobile, target_price) VALUES (?, ?)",
            (mobile, target_price)
        )

        conn.commit()
        conn.close()

        return "✅ Alert registered successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
