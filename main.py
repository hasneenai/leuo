import http.server
import socketserver
import sqlite3
from urllib.parse import parse_qs

PORT = 8080
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    username TEXT NOT NULL,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    password TEXT NOT NULL
)''')
conn.commit()
conn.close()

signup_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحة إنشاء حساب</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            background: linear-gradient(135deg, #74b9ff, #a29bfe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            margin: 0;
            position: relative;
        }

        .container {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }

        .form-container h1 {
            margin-bottom: 20px;
            color: #2d3436;
        }

        .input-group {
            margin-bottom: 15px;
            text-align: right;
        }

        .input-group label {
            display: block;
            margin-bottom: 5px;
            color: #636e72;
        }

        .input-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #dfe6e9;
            border-radius: 5px;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            padding: 10px;
            background: #0984e3;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #74b9ff;
        }

        .developer {
            margin-bottom: 20px;
            color: #2d3436;
        }

        .telegram-link {
            position: absolute;
            bottom: 10px;
            left: 10px;
            font-size: 32px;
        }

        .telegram-link a {
            color: #0984e3;
            text-decoration: none;
        }

        .telegram-link a:hover {
            color: #74b9ff;
        }

        .login-link {
            margin-top: 15px;
            display: block;
            color: #0984e3;
            text-decoration: none;
        }

        .login-link:hover {
            color: #74b9ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="developer">
            <h2>المطور حسو ال علي</h2>
        </div>
        <div class="form-container">
            <h1>إنشاء حساب</h1>
            <form id="signup-form" method="POST" action="/signup">
                <div class="input-group">
                    <label for="email">البريد الإلكتروني</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="input-group">
                    <label for="username">اسم المستخدم</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="input-group">
                    <label for="name">الاسم الكامل</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="input-group">
                    <label for="phone">رقم الهاتف</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                <div class="input-group">
                    <label for="password">كلمة السر</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <div class="input-group">
                    <label for="confirm-password">إعادة كتابة كلمة السر</label>
                    <input type="password" id="confirm-password" name="confirm-password" required>
                </div>
                <button type="submit">إنشاء حساب</button>
            </form>
            <a href="/login" class="login-link">تسجيل دخول</a>
        </div>
    </div>
    <div class="telegram-link">
        <a href="https://t.me/PY_50" target="_blank"><i class="fab fa-telegram"></i></a>
    </div>
    <script>
        document.getElementById('signup-form').addEventListener('submit', function(event) {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                event.preventDefault();
                alert('كلمات السر غير متطابقة. الرجاء المحاولة مرة أخرى.');
            }
        });
    </script>
</body>
</html>
"""

# محتوى صفحة تسجيل الدخول
login_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحة تسجيل دخول</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            background: linear-gradient(135deg, #74b9ff, #a29bfe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            margin: 0;
            position: relative;
        }

        .container {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }

        .form-container h1 {
            margin-bottom: 20px;
            color: #2d3436;
        }

        .input-group {
            margin-bottom: 15px;
            text-align: right;
        }

        .input-group label {
            display: block;
            margin-bottom: 5px;
            color: #636e72;
        }

        .input-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #dfe6e9;
            border-radius: 5px;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            padding: 10px;
            background: #0984e3;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #74b9ff;
        }

        .developer {
            margin-bottom: 20px;
            color: #2d3436;
        }

        .telegram-link {
            position: absolute;
            bottom: 10px;
            left: 10px;
            font-size: 32px;
        }

        .telegram-link a {
            color: #0984e3;
            text-decoration: none;
        }

        .telegram-link a:hover {
            color: #74b9ff;
        }

        .signup-link {
            margin-top: 15px;
            display: block;
            color: #0984e3;
            text-decoration: none;
        }

        .signup-link:hover {
            color: #74b9ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="developer">
            <h2>المطور حسو ال علي</h2>
        </div>
        <div class="form-container">
            <h1>تسجيل دخول</h1>
            <form id="login-form" method="POST" action="/login">
                <div class="input-group">
                    <label for="email">البريد الإلكتروني</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="input-group">
                    <label for="password">كلمة السر</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">تسجيل دخول</button>
            </form>
            <a href="/" class="signup-link">إنشاء حساب</a>
        </div>
    </div>
    <div class="telegram-link">
        <a href="https://t.me/PY_50" target="_blank"><i class="fab fa-telegram"></i></a>
    </div>
</body>
</html>
"""

# معالجة طلبات التسجيل وتسجيل الدخول
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(signup_page.encode('utf-8'))
        elif self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(login_page.encode('utf-8'))
        else:
            self.send_error(404, 'Page Not Found: %s' % self.path)
    
    def do_POST(self):
        if self.path == '/signup':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            fields = parse_qs(post_data.decode('utf-8'))

            email = fields.get('email', [''])[0]
            username = fields.get('username', [''])[0]
            name = fields.get('name', [''])[0]
            phone = fields.get('phone', [''])[0]
            password = fields.get('password', [''])[0]
            confirm_password = fields.get('confirm-password', [''])[0]

            if password != confirm_password:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Passwords do not match.')
                return

            try:
                conn = sqlite3.connect('users.db')
                c = conn.cursor()
                c.execute('INSERT INTO users (email, username, name, phone, password) VALUES (?, ?, ?, ?, ?)', 
                          (email, username, name, phone, password))
                conn.commit()
                conn.close()
                self.send_response(301)
                self.send_header('Location', '/login')
                self.end_headers()
            except sqlite3.IntegrityError:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Email already registered.')
        
        elif self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            fields = parse_qs(post_data.decode('utf-8'))

            email = fields.get('email', [''])[0]
            password = fields.get('password', [''])[0]

            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('SELECT password FROM users WHERE email=?', (email,))
            row = c.fetchone()
            conn.close()

            if row:
                db_password = row[0]
                if db_password == password:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    html_content = """
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
            background-color: #e9f0fb;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .image-container {
            margin-bottom: 20px;
        }
        .image-container img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .image-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .image-row img {
            width: 48%;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
            margin-bottom: 20px;
            font-size: 18px;
        }
        .header a {
            color: white;
            margin: 0 10px;
            text-decoration: none;
        }
        .header a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- القائمة العلوية -->
        <div class="header">
            <a href="#">Home</a>
            <a href="#">Terms of Service</a>
            <a href="#">Help</a>
            <a href="#">Support</a>
            <a href="#" onclick="logout()">Logout</a>
        </div>

        <!-- الاسم بالعربية -->
        <div class="header">
            حسو ال علي 
        </div>
        
        <h1>The site is dedicated to pictures of Messi</h1>
        <p>Here are some images displayed as per your request:</p>

        <!-- عرض الصورة الأولى -->
        <div class="image-container">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_26.jpg" alt="Image 1">
        </div>

        <!-- صف الصور الأول (صورتين بجانب بعض) -->
        <div class="image-row">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_31.jpg" alt="Image 2">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_31.jpg" alt="Image 3">
        </div>

        <!-- صف الصور الثاني (صورتين بجانب بعض) -->
        <div class="image-row">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_29.jpg" alt="Image 4">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_27.jpg" alt="Image 5">
        </div>

        <!-- صف الصور الثالث (صورتين بجانب بعض) -->
        <div class="image-row">
            <img src="https://api.telegram.org/file/bot6804250062:AAGm9Inu7FBDx3GI22xDejKNp9QaMIOZuSE/photos/file_9.jpg" alt="Image 6">
            <img src="https://api.telegram.org/file/bot6804250062:AAGm9Inu7FBDx3GI22xDejKNp9QaMIOZuSE/photos/file_8.jpg" alt="Image 7">
        </div>

        <!-- صف الصور الرابع (صورتين بجانب بعض) -->
        <div class="image-row">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_28.jpg" alt="Image 8">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_25.jpg" alt="Image 9">
        </div>

        <!-- عرض الصورة الأخيرة -->
        <div class="image-container">
            <img src="https://api.telegram.org/file/bot5295020674:AAFCr5qXMrOVamBRzvnqAlid1bUAxqOJL8Q/photos/file_26.jpg" alt="Image 10">
        </div>

        <!-- روابط التواصل الاجتماعي -->
        <div class="menu-container">
            <a href="https://t.me/PY_50" target="_blank">Telegram</a>
        </div>

    </div>

    <script>
        function logout() {
            alert('You have logged out.');
            window.location.href = "/login";
        }
    </script>
</body>
</html>
"""


                    self.wfile.write(html_content.encode('utf-8'))
                    response_text = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>Hasso Al Ali Website</title>
    <style>
        body {
            font-size: 20px; /* حجم الخط */
        }
        .bold {
            font-weight: bold; /* خط عريض */
        }
    </style>
</head>
<body>
    <span class="bold">\nWelcome to the new Hasso Al Ali website</span>
</body>
</html>
"""
                    self.end_headers()
                    self.wfile.write(response_text.encode('utf-8'))

                else:
                    self.send_response(401)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'Incorrect password.')
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Email not registered.')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
