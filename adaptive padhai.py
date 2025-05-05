# Adaptive Learning Engine for Underserved Students

class Student:
    def __init__(self, name):
        self.name = name
        self.performance = []  # List of quiz scores (0-100)

    def add_score(self, score):
        self.performance.append(score)

    def get_average_score(self):
        if not self.performance:
            return 0
        return sum(self.performance) / len(self.performance)

class AdaptiveEngine:
    def __init__(self):
        self.levels = {
            "basic": ["Addition", "Subtraction", "Basic Reading"],
            "intermediate": ["Multiplication", "Grammar", "Comprehension"],
            "advanced": ["Algebra", "Essay Writing", "Critical Thinking"]
        }

    def suggest_content(self, student): 
        avg_score = student.get_average_score()
        print(f"\nStudent: {student.name} | Avg. Score: {avg_score:.2f}")

        if avg_score < 50:
            level = "basic"
        elif 50 <= avg_score < 75:
            level = "intermediate"
        else:
            level = "advanced"

        content = self.levels[level]
        print(f"Suggested Learning Level: {level.upper()}")
        print("Recommended Topics:", content)

# === Example Usage ===
student1 = Student("Ravi (Underserved Background)")
student1.add_score(40)  # Initial low performance
student1.add_score(55)  # Slight improvement
student1.add_score(60)

engine = AdaptiveEngine()
engine.suggest_content(student1)
