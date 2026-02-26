import sqlite3
import os

DB_FILE = 'users.db'


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def setup_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Просто создаем таблицу с новыми полями, если она не существует
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            foot_length REAL,
            foot_width REAL,
            oblique_circumference REAL,
            toe_circumference REAL,
            instep_circumference REAL,
            foot_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()