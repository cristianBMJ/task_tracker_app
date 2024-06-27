import sqlite3

def view_data():
    # Path to your database file
    db_path = '/home/cris/workaplace/register_app/data/task_tracker.db'
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query and display data from users table
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Users:")
    for user in users:
        print(user)
    
    # Query and display data from tasks table
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    print("\nTasks:")
    for task in tasks:
        print(task)
    
    # Close the connection
    conn.close()

# Run the function to view data
view_data()
