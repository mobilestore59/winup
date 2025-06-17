from winup.data import SQLiteConnector

class TaskDatabase:
    def __init__(self, db_file="tasks.db"):
        self.db = SQLiteConnector(db_file)
        self._init_db()

    def _init_db(self):
        """Initializes the database and creates the 'tasks' table if it doesn't exist."""
        with self.db:
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    done BOOLEAN NOT NULL CHECK (done IN (0, 1))
                )
            """)

    def load_tasks(self):
        """Loads all non-done tasks from the database."""
        with self.db:
            cursor = self.db.execute("SELECT id, text FROM tasks WHERE done = 0")
            rows = cursor.fetchall()
            return [{"id": row[0], "text": row[1]} for row in rows]

    def add_task(self, text: str):
        """Adds a new task to the database and returns it with its new ID."""
        with self.db:
            cursor = self.db.execute("INSERT INTO tasks (text, done) VALUES (?, 0)", (text,))
            return {"id": cursor.lastrowid, "text": text}

    def mark_task_done(self, task_id: int):
        """Marks a task as done in the database."""
        with self.db:
            self.db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,)) 