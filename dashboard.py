from flask import Blueprint, render_template, session, redirect
import sqlite3

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']
    conn = sqlite3.connect('data/learning_system.db')
    cur = conn.cursor()
    cur.execute('SELECT topic, score FROM scores WHERE user_id=?', (user_id,))
    scores = cur.fetchall()
    conn.close()

    return render_template('dashboard.html', scores=scores)
