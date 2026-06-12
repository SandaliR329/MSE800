import sqlite3


class Database:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    date_of_birth TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)
            conn.commit()