import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, '..', 'data', 'task_tracker.db')

print(DATABASE_PATH) 