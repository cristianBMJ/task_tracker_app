from core.database import get_db_connection
from datetime import datetime

def add_task(user_id, task_name):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (user_id, task_name, completed, date)
            VALUES (?, ?, 0, ?)
        ''', (user_id, task_name, datetime.now().strftime('%Y-%m-%d')))
        conn.commit()

def get_tasks(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        tasks = cursor.fetchall()
        return [dict(task) for task in tasks]

def mark_task_completed(task_id, completed):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (int(completed), task_id))
        conn.commit()
