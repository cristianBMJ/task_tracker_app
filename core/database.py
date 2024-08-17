import sqlite3
from datetime import date
from core.config import DATABASE_PATH

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL
            )
        ''')
        
        # Create tasks table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                task_name TEXT NOT NULL,
                completed INTEGER NOT NULL,
                date DATE,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        # Create daily_task_completion table with UNIQUE constraint
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_task_completion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                task_id INTEGER,
                completion_date DATE,
                completed BOOLEAN,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (task_id) REFERENCES tasks(id),
                UNIQUE(user_id, task_id, completion_date)
            )
        ''')

        # Create task_history table with UNIQUE constraint
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS task_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date DATE,
                total_tasks INTEGER,
                completed_tasks INTEGER,
                completion_rate REAL,
                UNIQUE(user_id, date) 
            )
        ''')
        
        conn.commit()

# Initialize the database
initialize_database()

def get_daily_task_completion(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT task_id, completion_date, completed FROM daily_task_completion WHERE user_id = ? ORDER BY completion_date",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def save_daily_task_completion(user_id, task_id, completed):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        '''
        INSERT INTO daily_task_completion (user_id, task_id, completion_date, completed)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id, task_id, completion_date) DO UPDATE SET completed=excluded.completed
        ''',
        (user_id, task_id, date.today(), completed)
    )
    
    conn.commit()
    conn.close()

# #
def update_task_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT user_id, COUNT(*) as total_tasks, 
               SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed_tasks,
               date(completion_date) as completion_date
        FROM daily_task_completion
        GROUP BY user_id, date(completion_date)
    ''')
    
    rows = cursor.fetchall()
    for row in rows:
        user_id = row['user_id']
        completion_date = row['completion_date']
        total_tasks = row['total_tasks']
        completed_tasks = row['completed_tasks']
        completion_rate = completed_tasks / total_tasks if total_tasks > 0 else 0
        
        cursor.execute('''
            INSERT INTO task_history (user_id, date, total_tasks, completed_tasks, completion_rate)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT (user_id, date) DO UPDATE SET 
            total_tasks=excluded.total_tasks,
            completed_tasks=excluded.completed_tasks,
            completion_rate=excluded.completion_rate
            ''',
            (user_id, completion_date, total_tasks, completed_tasks, completion_rate)
        )
    
    conn.commit()
    conn.close()

def update_task_history_V2():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT user_id, COUNT(*) as total_tasks, 
               SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed_tasks,
               date(completion_date) as completion_date
        FROM daily_task_completion
        GROUP BY user_id, date(completion_date)
    ''')
    
    rows = cursor.fetchall()
    for row in rows:
        user_id = row['user_id']
        completion_date = row['completion_date']
        total_tasks = row['total_tasks']
        completed_tasks = row['completed_tasks']
        completion_rate = completed_tasks / total_tasks if total_tasks > 0 else 0

        # Check if the record already exists
        cursor.execute('''
            SELECT COUNT(*) FROM task_history WHERE user_id = ? AND date = ?
        ''', (user_id, completion_date))
        
        exists = cursor.fetchone()[0]
        
        if exists:
            # Update the existing record
            cursor.execute('''
                UPDATE task_history
                SET total_tasks = ?, completed_tasks = ?, completion_rate = ?
                WHERE user_id = ? AND date = ?
            ''', (total_tasks, completed_tasks, completion_rate, user_id, completion_date))
        else:
            # Insert a new record
            cursor.execute('''
                INSERT INTO task_history (user_id, date, total_tasks, completed_tasks, completion_rate)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, completion_date, total_tasks, completed_tasks, completion_rate))
    
    conn.commit()
    conn.close()


# Update task history
# update_task_history()
