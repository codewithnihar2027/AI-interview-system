import os
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "users.db"
)


def create_history_table():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interview_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            question TEXT,
            score REAL,
            role TEXT,
            difficulty TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_attempt(
        username,
        question,
        score,
        role,
        difficulty
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interview_history
        (
            username,
            question,
            score,
            role,
            difficulty,
            date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            username,
            question,
            score,
            role,
            difficulty,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )
    )

    conn.commit()
    conn.close()


def load_history():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            username,
            question,
            score,
            role,
            difficulty,
            date
        FROM interview_history
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows