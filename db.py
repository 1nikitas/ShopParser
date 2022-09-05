import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_item(self, name):
        with self.connection:
            return self.cursor.execute("INSERT INTO items(name) VALUES (?)", (name,))

    def item_exists(self, name):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM items WHERE name = ?", (name,)).fetchall()
            return bool(len(result))

