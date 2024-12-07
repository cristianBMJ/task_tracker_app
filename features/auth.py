from core.database import get_db_connection
import sqlite3

def register_user(username):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
            conn.commit()
            return True  # Indicate success
        except sqlite3.IntegrityError:
            return False  # Indicate that the username already exists

def get_user_id(username):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        return user['id'] if user else None
