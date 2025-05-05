import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(BASE_DIR, 'database.db')  # SQLite DB path
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/uploads')  # Optional if using uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16MB

# For future environments (example)
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
