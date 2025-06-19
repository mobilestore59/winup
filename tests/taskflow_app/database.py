import sqlite3
from collections import namedtuple

DB_FILE = "taskflow.db"
Task = namedtuple("Task", ["id", "title", "completed"])

def get_db_conn():
    conn = sqlite3.connect(DB_FILE)
    return conn

def init_db():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    """)
    # Add some sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] == 0:
        sample_tasks = [
            ('Finish WinUp refactor', True),
            ('Implement Drag and Drop', False),
            ('Write documentation', False)
        ]
        cursor.executemany("INSERT INTO tasks (title, completed) VALUES (?, ?)", sample_tasks)
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_db_conn()
    conn.row_factory = lambda cursor, row: Task(*row)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks ORDER BY id")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(title: str):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, completed) VALUES (?, ?)", (title, False))
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return Task(id=task_id, title=title, completed=False)

def delete_task(task_id: int):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def toggle_task_status(task_id: int):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = NOT completed WHERE id = ?", (task_id,))
    conn.commit()
    conn.close() 