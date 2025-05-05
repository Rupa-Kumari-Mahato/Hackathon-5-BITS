# This is the main file for the API Creation using Flask

from flask import Flask
from routes.auth import auth_bp
from routes.quiz import quiz_bp
from routes.dashboard import dashboard_bp
from routes.admin import admin_bp
from routes.lesson import lesson_bp  # Import lesson blueprint
from routes.language import language_bp
from models.database import init_db
from flask import Flask, render_template
from utils.translator import Translator
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, session, redirect, url_for
import pandas as pd
from flask import send_file, session, redirect
import sqlite3
from io import BytesIO
from flask import Flask, session, redirect, url_for
from flask import render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key' # Required for freshing message

# Dummy data for validation (replace with your database or other storage)
valid_credentials = {
    'username': 'admin',  # Example username
    'password': 'password123'  # Example password
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        

        # Check if the credentials are valid
        if username == valid_credentials['username'] and password == valid_credentials['password']:
            session['username'] = username  # Set session
            session['user_id'] = 1 # hardcoded ID or fetch from DB
            return redirect(url_for('dashboard'))  # Redirect to the dashboard on success
        else:
            flash('Invalid credentials. Please try again.', 'error')  # Flash error message

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

    # Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(lesson_bp)  # Register lesson blueprint
app.register_blueprint(language_bp)
@app.route('/translated')
def translated():
    translator = Translator(src_lang='en', target_lang='hi')
    translated_text = translator.translate("Welcome to the AI learning platform.")
    return render_template('lesson.html', content=translated_text)

@app.route('/')
def index():
    return render_template('dashboard.html')

# Language setting route
@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in LANGUAGES:
        session['lang'] = lang
    return redirect(url_for('index'))


@app.route('/export_excel', methods=['GET'])
def export_excel():
    # Check if the user id is loggged in
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect('/')  # Redirect to login page if user is not logged in

    # Get the user_id from the session
    user_id = session['user_id']

    # Connect to the database to fetch the user's scores
    conn = sqlite3.connect('data/learning_system.db')
    cursor = conn.cursor()
# Fetch the scores for the current user
    cursor.execute('SELECT topic, score FROM scores WHERE user_id = ?', (user_id,))
    scores = cursor.fetchall()

    # Create a DataFrame from the scores
    df = pd.DataFrame(scores, columns=['Topic', 'Score (%)'])

    # Save the DataFrame to a BytesIO object as an Excel file
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Scores')
    output.seek(0)  # Rewind the file pointer to the beginning

    # Send the file as a downloadable response
    return send_file(output, as_attachment=True, download_name="quiz_scores.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# Initialize database
init_db()
if __name__ == "__main__":
    app.run(debug=True)
