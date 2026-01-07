from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
from auth import start_login, confirm_otp

app = Flask(__name__)
app.secret_key = "replace_this_later"

BASE_DIR = os.environ.get("HOME", os.getcwd())
DB_PATH = os.path.join(BASE_DIR, "site", "wwwroot", "users.db")

def db():
    return sqlite3.connect(DB_PATH)

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mobile = request.form["mobile"]
        conn = db()
        start_login(conn, mobile)
        session["mobile"] = mobile
        return redirect("/verify-otp")
    return render_template("login.html")

@app.route("/verify-otp", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        otp = request.form["otp"]
        conn = db()
        if confirm_otp(conn, session["mobile"], otp):
            session["logged_in"] = True
            return redirect("/dashboard")
    return render_template("verify_otp.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
