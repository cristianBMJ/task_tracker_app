from core.database import get_db_connection
from datetime import datetime, date


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
        # Update the `completed` status and set the `date` to today's date
        cursor.execute('UPDATE tasks SET completed = ?, date = ? WHERE id = ?', 
                       (int(completed), str(date.today()), task_id))
        conn.commit()
        
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()