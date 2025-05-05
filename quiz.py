from flask import Blueprint, render_template, request, session, redirect
from utils.question_bank import get_questions
from utils.adaptive_engine import get_recommendations
from flask import Flask, render_template, request
import sqlite3

# Define the quiz blueprint with a unique name
quiz_bp = Blueprint('quiz_blueprint', __name__, url_prefix='/quiz')

# Route to select topic and take the quiz
@quiz_bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'user_id' not in session:
        return redirect('/')

    if request.method == 'POST':
        topic = request.form['topic']
        questions = get_questions(topic)
        if not questions:
            return render_template('error.html', message="No questions available for this topic.")
        return render_template('quiz.html', topic=topic, questions=questions)

    return render_template('select_topic.html')

# Route to handle quiz submission and calculate score
@quiz_bp.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if 'user_id' not in session:
        return redirect('/')

    user_id = session['user_id']
    topic = request.form['topic']
    total = 0
    correct = 0

    conn = sqlite3.connect('data/learning_system.db')
    cur = conn.cursor()

    # Fetch the questions for the quiz
    questions = get_questions(topic)

    # Check if questions exist for this topic
    if not questions:
        return render_template('error.html', message="No questions available for this quiz topic.")

    # Iterate over the questions and check answers
    for q in questions:
        qid = str(q['id'])
        user_answer = request.form.get(qid)
        
        # Skip question if no answer is provided (could be handled as an error, depending on the case)
        if not user_answer:
            continue

        correct_answer = q['answer']
        total += 1
        if user_answer == correct_answer:
            correct += 1

        # Save question-answer history into the database
        cur.execute('''INSERT INTO quiz_history (user_id, topic, question, user_answer, correct_answer)
                       VALUES (?, ?, ?, ?, ?)''', (user_id, topic, q['question'], user_answer, correct_answer))

    # Avoid division by zero by checking if there are questions
    if total > 0:
        score = int((correct / total) * 100)
    else:
        score = 0  # Default to 0 if there are no questions

    # Save the score into the database
    cur.execute('INSERT INTO scores (user_id, topic, score) VALUES (?, ?, ?)', (user_id, topic, score))
    conn.commit()
    conn.close()

    # Get recommendations based on the user's performance
    recommendations = get_recommendations(user_id)

    # Return the result page with score and recommendations
    return render_template('result.html', topic=topic, score=score, recommendations=recommendations)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/select_topic')
def select_topic():
    subjects = ['Maths', 'Science', 'History']
    return render_template('select_topic.html', subjects=subjects)

@app.route('/quiz/<subject>')
def quiz(subject):
    # You can later add logic here to load quiz questions by subject
    return f"Quiz for {subject} coming soon!"
