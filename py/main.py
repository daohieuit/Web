from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os  # Import thư viện os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
DATABASE = '../database/database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exams')
def exams():
    return render_template('exams.html')

@app.route('/document')
def document():
    return render_template('document.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    fullname = request.form['fullname']
    phone = request.form['phone']
    gender = request.form['gender']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        error = 'Mật khẩu và xác nhận mật khẩu không khớp.'
        return render_template('signup.html', error=error)

    conn = get_db()
    db = conn.cursor()
    error = None
    if not fullname:
        error = 'Vui lòng nhập họ tên.'
    elif not phone:
        error = 'Vui lòng nhập số điện thoại.'
    elif not username:
        error = 'Vui lòng nhập tên đăng nhập.'
    elif not email:
        error = 'Vui lòng nhập địa chỉ email.'
    elif not password:
        error = 'Vui lòng nhập mật khẩu.'
    elif db.execute(
        'SELECT id FROM users WHERE username = ?', (username,)
    ).fetchone() is not None:
        error = f'Tên đăng nhập "{username}" đã tồn tại.'
    elif db.execute(
        'SELECT id FROM users WHERE email = ?', (email,)
    ).fetchone() is not None:
        error = f'Địa chỉ email "{email}" đã được sử dụng.'

    if error is None:
        db.execute(
            'INSERT INTO users (fullname, phone, gender, username, email, password) VALUES (?, ?, ?, ?, ?, ?)',
            (fullname, phone, gender, username, email, password)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    else:
        conn.close()
        return render_template('signup.html', error=error)

if __name__ == '__main__':
    print("Chuẩn bị chạy ứng dụng Flask ở chế độ debug...")
    app.run(debug=True)