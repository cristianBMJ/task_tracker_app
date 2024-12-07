from core.database import get_db_connection
import sqlite3
import streamlit as st  # Import Streamlit

def register_user(username):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
            conn.commit()
            st.success("User registered successfully!")  # Show success message
            return True  # Indicate success
        except sqlite3.IntegrityError:
            st.error("Username already exists. Please choose a different one.")  # Show error message
            return False  # Indicate that the username already exists

def get_user_id(username):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        return user[0] if user else None  # Access the first element of the tuple
        #return user['id'] if user else None
