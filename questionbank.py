import random

# for the creation of questions
question_bank = {
    'easy': [
        {'question': '2 + 2 = ?', 'options': ['3', '4', '5'], 'answer': '4'},
        {'question': 'Capital of India?', 'options': ['Delhi', 'Mumbai', 'Kolkata'], 'answer': 'Delhi'}
    ],
    'medium': [
        {'question': '12 x 12 = ?', 'options': ['144', '121', '132'], 'answer': '144'},
        {'question': 'H2O is the chemical formula for?', 'options': ['Oxygen', 'Water', 'Hydrogen'], 'answer': 'Water'}
    ],
    'hard': [
        {'question': 'What is the derivative of sin(x)?', 'options': ['cos(x)', '-cos(x)', 'sin(x)'], 'answer': 'cos(x)'},
        {'question': 'Who developed the theory of relativity?', 'options': ['Newton', 'Einstein', 'Tesla'], 'answer': 'Einstein'}
    ]
}

# To showcase the performance of students
student_performance = {'correct': 0, 'total': 0}

def get_next_question():
    accuracy = student_performance['correct'] / student_performance['total'] if student_performance['total'] > 0 else 0
    if accuracy < 0.5:
        difficulty = 'easy'
    elif accuracy < 0.8:
        difficulty = 'medium'
    else:
        difficulty = 'hard'
    return random.choice(question_bank[difficulty])

# main loop
for _ in range(5):  # For 5 questions
    q = get_next_question()
    print(f"\n{q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"{idx}. {option}")
    try:
        answer = int(input("your answer (1/2/3): "))
        if q['options'][answer - 1] == q['answer']:
            print("✅ correct answer!")
            student_performance['correct'] += 1
        else:
            print(f"❌ wrong answer! correct answer is: {q['answer']}")
    except (ValueError, IndexError):
        print("❌ please choose the valid option।")
    student_performance['total'] += 1

print(f"\nYour accuracy: {student_performance['correct']}/{student_performance['total']}")