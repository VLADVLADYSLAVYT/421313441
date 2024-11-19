from flask import Flask, render_template, request

app = Flask(__name__)

# Змінна для зберігання даних користувачів
users_data = []

# Головна сторінка, де користувач вводить свої дані
@app.route('/')
def index():
    return render_template('index.html')  # Форма реєстрації

# Маршрут для обробки форми
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')

    # Зберігаємо дані в список
    users_data.append({'email': email, 'password': password})

    # Показуємо адміну список всіх користувачів
    admin_page = "<h1>Дані користувачів:</h1>"
    for user in users_data:
        admin_page += f"<p>Електронна пошта: {user['email']} - Пароль: {user['password']}</p>"

    return admin_page

if __name__ == '__main__':
    app.run(debug=True)
