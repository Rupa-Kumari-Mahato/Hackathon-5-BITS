from flask import Blueprint, render_template, session, redirect
import sqlite3

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_dashboard():
    if 'role' not in session or session['role'] != 'admin':
        return redirect('/')

    conn = sqlite3.connect('data/learning_system.db')
    cur = conn.cursor()

    cur.execute('''
        SELECT users.username, scores.topic, scores.score
        FROM scores
        JOIN users ON scores.user_id = users.id
    ''')
    report = cur.fetchall()
    conn.close()

    return render_template('admin_panel.html', report=report)
