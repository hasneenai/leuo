<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحة إنشاء حساب</title>
    <link rel="stylesheet" href="style.css">
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
    <script src="script.js"></script>
</body>
</html>
