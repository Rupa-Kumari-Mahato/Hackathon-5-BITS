from flask import Blueprint, render_template, session, redirect, url_for
import sqlite3

# Create blueprint for lesson
lesson_bp = Blueprint('lesson', __name__)

# Define different learning modules with some dummy content
modules = {
    'math': {
        'title': 'Basic Math: Addition and Subtraction',
        'content': 'In this lesson, we will learn how to add and subtract numbers.',
        'quiz_link': '/quiz/math'
    },
    'science': {
        'title': 'Science: Introduction to Physics',
        'content': 'In this lesson, we will explore the basics of physics, including forces and motion.',
        'quiz_link': '/quiz/science'
    },
    'history': {
        'title': 'History: Ancient Civilizations',
        'content': 'In this lesson, we will dive into the ancient civilizations, like Egypt and Mesopotamia.',
        'quiz_link': '/quiz/history'
    }
}

# Route for general lesson overview
@lesson_bp.route('/start')
def start_learning():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))  # Redirect to login if not logged in

    user_id = session['user_id']
    lang = session.get('language', 'en')  # Default language to English

    lessons = {
        'en': {
            'math': "Welcome to today's lesson on Basic Math: Addition and Subtraction.",
            'science': "Welcome to the Science lesson: Introduction to Physics.",
            'history': "Welcome to History: Ancient Civilizations."
        },
        'hi': {
            'math': "आज के पाठ में आपका स्वागत है: जोड़ और घटाव।",
            'science': "भौतिकी के बारे में परिचय: बल और गति।",
            'history': "इतिहास में आपका स्वागत है: प्राचीन सभ्यताएँ।"
        }
    }

    content = lessons.get(lang, lessons['en'])
    return render_template('lesson.html', modules=modules, content=content)

# ✅ New route to handle individual topic
@lesson_bp.route('/start/<topic>', endpoint='start_learning_topic')
def start_learning_topic(topic):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if topic not in modules:
        return "Topic not found", 404

    lang = session.get('language', 'en')

    lessons = {
        'en': {
            'math': "Welcome to today's lesson on Basic Math: Addition and Subtraction.",
            'science': "Welcome to the Science lesson: Introduction to Physics.",
            'history': "Welcome to History: Ancient Civilizations."
        },
        'hi': {
            'math': "आज के पाठ में आपका स्वागत है: जोड़ और घटाव।",
            'science': "भौतिकी के बारे में परिचय: बल और गति।",
            'history': "इतिहास में आपका स्वागत है: प्राचीन सभ्यताएँ।"
        }
    }

    topic_content = modules[topic]
    greeting = lessons.get(lang, lessons['en']).get(topic, "")
    return render_template('lesson_topic.html', title=topic_content['title'], content=topic_content['content'], greeting=greeting)
