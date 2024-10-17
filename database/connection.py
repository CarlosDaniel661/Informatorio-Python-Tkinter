import sqlite3
import os

class DatabaseConnection:
    def __init__(self, db_name="database/expenses.db"):
        self.db_path = os.path.join(os.getcwd(), db_name)
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """)

    def execute_query(self, query, params=()):
        with self.conn:
            self.conn.execute(query, params)

    def fetch_all(self, query, params=()):
        with self.conn:
            return self.conn.execute(query, params).fetchall()

    def close(self):
        self.conn.close()
