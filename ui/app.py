import streamlit as st
from core.database import get_db_connection
from features.auth import register_user, get_user_id
from features.tasks import add_task, get_tasks, mark_task_completed

# User Registration/Login
st.sidebar.title("User Login/Register")
username = st.sidebar.text_input("Username")
if st.sidebar.button("Register"):
    register_user(username)
if st.sidebar.button("Login"):
    st.session_state['user_id'] = get_user_id(username)

# Task Management
if 'user_id' in st.session_state:
    user_id = st.session_state['user_id']
    st.title(f"Welcome, {username}!")

    # Add Task
    task_name = st.text_input("Enter task name:")
    if st.button("Add Task"):
        add_task(user_id, task_name)

    # Display Tasks
    tasks = get_tasks(user_id)
    for task in tasks:
        if st.checkbox(task['task_name'], key=task['id'], value=task['completed']):
            mark_task_completed(task['id'], True)
        else:
            mark_task_completed(task['id'], False)
    
    # Display Progress
    st.title("Progress")
    st.line_chart([task['completed'] for task in tasks])
