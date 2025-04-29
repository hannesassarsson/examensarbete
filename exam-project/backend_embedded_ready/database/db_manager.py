import sqlite3
from datetime import datetime
class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    nfc_id TEXT UNIQUE NOT NULL,
                    pin TEXT
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    action TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)

    def get_user_by_nfc(self, nfc_id):
        with self.conn:
            user = self.conn.execute("""
                SELECT id, name, pin FROM users WHERE nfc_id = ?
            """, (nfc_id,)).fetchone()
            if user:
                return {"id": user[0], "name": user[1], "pin": user[2]}
            return None

    def get_user_by_pin(self, pin):
        with self.conn:
            user = self.conn.execute("""
                SELECT id, name FROM users WHERE pin = ?
            """, (pin,)).fetchone()
            if user:
                return {"id": user[0], "name": user[1]}
            return None

    def log_history(self, user_id, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.conn:
            self.conn.execute("""
                INSERT INTO history (user_id, action, timestamp)
                VALUES (?, ?, ?)
            """, (user_id, action, timestamp))

    def get_history(self):
        with self.conn:
            return self.conn.execute("""
                SELECT h.id, u.name, h.action, h.timestamp
                FROM history h
                JOIN users u ON h.user_id = u.id
                ORDER BY h.timestamp DESC
            """).fetchall()
        
    def get_user_history(self, user_id):
        with self.conn:
            return self.conn.execute("""
            SELECT * FROM history
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT 1
            """, (user_id,)).fetchall()
    def update_user_pin(self, user_id, new_pin):
        with self.conn:
            self.conn.execute("""
            UPDATE users SET pin = ? WHERE id = ?
            """, (new_pin, user_id))