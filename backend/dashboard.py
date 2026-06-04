import os
import sqlite3

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "users.db"
)


def total_attempts(username):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM interview_history
        WHERE username = ?
        """,
        (username,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def average_score(username):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(score)
        FROM interview_history
        WHERE username = ?
        """,
        (username,)
    )

    avg = cursor.fetchone()[0]

    conn.close()

    return round(avg, 2) if avg else 0


def highest_score(username):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT MAX(score)
        FROM interview_history
        WHERE username = ?
        """,
        (username,)
    )

    highest = cursor.fetchone()[0]

    conn.close()

    return highest if highest else 0


def recent_attempts(username):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            question,
            score,
            role,
            difficulty,
            date
        FROM interview_history
        WHERE username = ?
        ORDER BY id DESC
        """,
        (username,)
    )

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:

        history.append(
            {
                "question": row[0],
                "score": row[1],
                "role": row[2],
                "difficulty": row[3],
                "date": row[4]
            }
        )

    return history