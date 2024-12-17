from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Inisialisasi database
def init_db():
    conn = sqlite3.connect('database/users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       username TEXT, 
                       email TEXT, 
                       number TEXT, 
                       password TEXT)''')
    conn.commit()
    conn.close()

# Route untuk registrasi user
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        number = request.form['number']
        password = request.form['password']
        
        # Enkripsi password sebelum disimpan
        password_hash = generate_password_hash(password)
        
        # Simpan ke database
        conn = sqlite3.connect('database/users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, number, password) VALUES (?, ?, ?, ?)", 
                       (username, email, number, password_hash))
        conn.commit()
        conn.close()
        return redirect(url_for("success"))

    return render_template("register.html")

# Route sukses
@app.route("/success")
def success():
    return "Registration Successful! Thank you for signing up."

# Route untuk login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        # Cek apakah email ada di database
        conn = sqlite3.connect('database/users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[4], password):  # user[4] adalah kolom password
            return redirect(url_for("user_dashboard"))
        else:
            return "Invalid login credentials!"

    return render_template("login.html")

# Route untuk halaman dashboard user
@app.route('/user')
def user_dashboard():
    return render_template('user_dashboard.html')

# Route untuk halaman dashboard admin
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Route untuk halaman rekomendasi admin
@app.route('/admin/rekomendasi')
def admin_rekomendasi():
    return render_template('admin_rekomendasi.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
