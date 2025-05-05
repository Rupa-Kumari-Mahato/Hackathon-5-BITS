import sqlite3

def init_db():
    try:
        # Connect to SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect('data/learning_system.db')
        c = conn.cursor()

        # Users table
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT
            )
        ''')

        # Scores table
        c.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                topic TEXT,
                score INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')

        # Quiz history table
        c.execute('''
            CREATE TABLE IF NOT EXISTS quiz_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                topic TEXT,
                question TEXT,
                user_answer TEXT,
                correct_answer TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')

        # Commit changes to the database
        conn.commit()

        print("Database initialized successfully!")

    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

    finally:
        # Close the connection regardless of success or failure
        conn.close()

# You can now call init_db() to initialize the database
