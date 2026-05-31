import json
import os
from datetime import datetime

FILE_NAME = "history.json"


def save_attempt(question, score, role, difficulty):

    data = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as f:
            data = json.load(f)

    data.append({
        "question": question,
        "score": score,
        "role": role,
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def load_history():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)