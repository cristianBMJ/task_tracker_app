# Task Tracker App

This is an prototype app to track daily tasks and habits. You can see version Beta [here.](https://task-tracker-app.streamlit.app/)

## Features
- Task (habit) management
- User-specific task registers
- Frontend with Streamlit to register task completion
- Display progress history and daily achievement percentage using widgets
- Lightweight data storage (SQLite)

## Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/task_tracker_app.git
cd task_tracker_app
```

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

## Contributing

We welcome contributions to improve the Task Tracker App! Here's how you can contribute:

1. **Fork the repository**  
   Click the "Fork" button on the top-right corner of this repository to create your own copy.

2. **Clone your fork**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/task_tracker_app.git
   cd task_tracker_app

