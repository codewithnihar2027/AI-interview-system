import os
import sqlite3

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

        cursor.execute(
            """
            INSERT INTO users
            (username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, password)
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
        AND password = ?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# Run Test

if __name__ == "__main__":

    create_users_table()

    create_user(
        "meghna",
        "meghna@gmail.com",
        "1234"
    )

    print(
        login_user(
            "meghna",
            "1234"
        )
    )
    create_user("sujal", "sujal@gmail.com", "1234")
    create_user("amit", "amit@gmail.com", "1234")
    create_user("nihar", "nihar@gmail.com", "1234")
    create_user("nilanjan", "nilanjan@gmail.com", "1234")