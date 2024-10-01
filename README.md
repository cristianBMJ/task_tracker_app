# Task Tracker App

This is an prototype app to track daily tasks and habits.

## Features
- Task (habit) management
- User-specific task registers
- Frontend with Streamlit to register task completion
- Display progress history and daily achievement percentage using widgets
- Lightweight data storage (SQLite)

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/task_tracker_app.git
   cd task_tracker_app

## Install 

Use it poetry. 

Install Poetry if you don't have it:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install the dependencies:

```bash
poetry install
```

Activate the virtual environment:

```bash
poetry shell
```


## Usage

### Run 

```sh
export PYTHONPATH=$(pwd)
streamlit run ui/app.py
```
