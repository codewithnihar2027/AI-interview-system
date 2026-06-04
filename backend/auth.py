import os
import sqlite3
import bcrypt

# Database Path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "users.db"
)


# Create Users Table

def create_users_table():

    os.makedirs(
        os.path.join(BASE_DIR, "data"),
        exist_ok=True
    )

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()


# Create New User

def create_user(username, email, password):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    try:

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        cursor.execute(
            """
            INSERT INTO users
            (username, email, password)
            VALUES (?, ?, ?)
            """,
            (
                username,
                email,
                hashed_password
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# Login User

def login_user(username, password):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return None

    stored_hash = user[3]

    if bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    ):
        return user

    return None


# Run Test

if __name__ == "__main__":

    create_users_table()