from flask import Flask, redirect, render_template, request, session, url_for, flash
import mysql.connector
from views.views_ingrediente import views_ingrediente
from views.views_categoria_ing import views_categoria_ing

app = Flask(__name__)
app.register_blueprint(views_ingrediente)
app.register_blueprint(views_categoria_ing)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='miyh2'
)
cursor = db.connect()

app.secret_key = 'My clave'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT id, user_name, password FROM users where user_name = %s", (username))
        user = cursor.fetchone()

    return render_template('login.html')

@app.route('/index', methods=['POST'])
def index():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "admin1234": 
        
        return render_template('index.html')
    
    else:
        print('Usuario Incorrecto')

        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)