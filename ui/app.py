import sys
import os

# Add the path to the core module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../path/to/core')))

from datetime import date
import streamlit as st
from core.database import get_db_connection,save_daily_task_completion,get_daily_task_completion, update_task_history, get_task_history
from features.auth import register_user, get_user_id
from features.tasks import add_task, get_tasks, mark_task_completed, delete_task

import plotly.graph_objs as go
import pandas as pd


# User Registration/Login
st.sidebar.title("User Login/Register")
username = st.sidebar.text_input("Username")
if st.sidebar.button("Register"):
    register_user(username)
if st.sidebar.button("Login"):
    st.session_state['user_id'] = get_user_id(username)

# Task Management (go after of the graphs)
if 'user_id' in st.session_state:
    user_id = st.session_state['user_id']
    st.title(f"Welcome, {username}!")

    #Create the graph Cumulative from task_history
    history_data = get_task_history(user_id)
    

    # Assuming daily_data is a list of tuples (task_id, completion_date, completed)
    df = pd.DataFrame(history_data, columns=['date', 'total_tasks', 'completed_tasks', 'completion_rate'] )
    df['date'] = pd.to_datetime(df['date'])

    # Create the graph Cumulative Completions
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['completion_rate'],
        fill='tozeroy',  # Fill to the y-axis
        mode='lines',
        line=dict(color='purple')
    ))

    st.title("Progress")

    # Update layout
    fig.update_layout(
        #title="Cumulative Task Completions Over Time",
        xaxis_title="Date",
        #yaxis_title="Completions Rate",
        yaxis_range=[0, max(df['completion_rate']) + 0.1]  # Adjust based on your data
    )

    # Display the graph in Streamlit
    
    st.plotly_chart(fig)

    st.write(f"DONE!")

    


    #######################
  
    completion_percentage = df['completion_rate'].iloc[-1]*100   
 
    # Display Progress - Completion Percentage
    st.title("Completion Percentage %")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=completion_percentage,
        title={'text': "Completion Percentage"},
        gauge={
            'axis': {'range': [0, 100 ]},
            'bar': {'color': "blue"},
        }
    ))
    st.plotly_chart(fig)





    # Add Task
    task_name = st.text_input("Enter task name:")
    if st.button("Add Task"):
        if task_name.strip():  # Check if the task is not blank
            add_task(user_id, task_name)
        else:
            st.warning("Task name cannot be blank.")


    # Display Tasks
    tasks = get_tasks(user_id)
    for task in tasks:
        # Get last completion date
        task_last_completed_date = task.get('date')

    # Display the values using Streamlit
        today = str(date.today())
        # st.write(f"Task Last Completed Date: {task_last_completed_date}")
        # st.write(f"Today's Date: {today}")

        # Reset task if it's a new day
        if task_last_completed_date != str(date.today()):
            mark_task_completed(task['id'], False)  # Reset to unchecked
            task['completed'] = False  # Update in the current session too


        # Display the task checkbox
        if st.checkbox(task['task_name'], key=task['id'], value=task['completed']):
            mark_task_completed(task['id'], True) # update date
            save_daily_task_completion(user_id, task['id'], True)
            update_task_history()

        else:
            mark_task_completed(task['id'], False)
            save_daily_task_completion(user_id, task['id'], False)
            update_task_history()

        # if st.checkbox(task['task_name'], key=task['id'], value=task['completed']):
        #     mark_task_completed(task['id'], True)  # Save checked state
        # else:
        #     mark_task_completed(task['id'], False)  # Save unchecked state

    # Delete a Task Provided by the User
    st.title("Delete Task")
    task_to_delete = st.selectbox("Select a task to delete", [task['task_name'] for task in tasks if task['task_name'].strip()])
    if st.button("Delete Task"):
        for task in tasks:
            if task['task_name'] == task_to_delete:
                delete_task(task['id'])
                st.success(f"Task '{task_to_delete}' deleted!")
                break



    #