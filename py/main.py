from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

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

if __name__ == '__main__':
    print("Chuẩn bị chạy ứng dụng Flask ở chế độ debug...")
    app.run(debug=True)