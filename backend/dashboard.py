import json
import os

def get_history():

    if not os.path.exists("history.json"):
        return []

    with open("history.json", "r") as file:
        return json.load(file)


def total_attempts():

    return len(get_history())


def average_score():

    data = get_history()

    if len(data) == 0:
        return 0

    total = sum(item["score"] for item in data)

    return round(total / len(data), 2)


def highest_score():

    data = get_history()

    if len(data) == 0:
        return 0

    return max(item["score"] for item in data)

def recent_attempts():
    return get_history()[::-1]