import sqlite3

class USDADatabase:
    def __init__(self):
        self.conn = sqlite3.connect('usda.db')

    def close(self):
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    db = USDADatabase()
