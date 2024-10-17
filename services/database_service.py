from database.connection import DatabaseConnection

class DatabaseService:
    def __init__(self, db_path):
        self.db_connection = DatabaseConnection(db_path)

    def validate_user(self, username, password):
        cursor = self.db_connection.conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        user = cursor.fetchall()
        return len(user) > 0

    def register_user(self, username, password):
        cursor = self.db_connection.conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(query, (username, password))
        self.db_connection.conn.commit()
        

    def close_connection(self):
        self.db_connection.close()
