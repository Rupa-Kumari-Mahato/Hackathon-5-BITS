from flask import Blueprint, render_template, request, redirect, session
import sqlite3

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return render_template('login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        conn = sqlite3.connect('data/learning_system.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE username=? AND password=?', (uname, pwd))
        user = cur.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[3]
            return redirect('/dashboard')
        else:
            return "Invalid credentials"
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('data/learning_system.db')
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already exists."
        conn.close()
        return redirect('/')
    return render_template('signup.html')
