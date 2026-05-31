import re

def parse_feedback(text):

    result = {
        "score": 0,
        "strengths": [],
        "weaknesses": [],
        "suggestions": []
    }

    score_match = re.search(
        r"Score:\s*(\d+)",
        text
    )

    if score_match:
        result["score"] = int(
            score_match.group(1)
        )

    current_section = None

    for line in text.split("\n"):

        line = line.strip()

        if "Strengths" in line:
            current_section = "strengths"

        elif "Weaknesses" in line:
            current_section = "weaknesses"

        elif "Suggestions" in line:
            current_section = "suggestions"

        elif line.startswith("-"):

            item = line.replace("-", "").strip()

            if current_section:
                result[current_section].append(item)

    return result