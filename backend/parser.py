import re

def parse_feedback(text):

    result = {
        "score": 0,
        "semantic": 0,
        "keyword": 0,
        "completeness": 0,
        "ideal_answer": "",
        "strengths": [],
        "weaknesses": [],
        "suggestions": []
    }

    # -------------------------
    # Score Extraction
    # -------------------------

    score_match = re.search(
        r"Score:\s*(\d+)",
        text
    )

    if score_match:
        result["score"] = int(
            score_match.group(1)
        )

    # -------------------------
    # Semantic Similarity
    # -------------------------

    semantic_match = re.search(
        r"Semantic Similarity:\s*([\d.]+)",
        text
    )

    if semantic_match:
        result["semantic"] = float(
            semantic_match.group(1)
        )

    # -------------------------
    # Keyword Coverage
    # -------------------------

    keyword_match = re.search(
        r"Keyword Coverage:\s*([\d.]+)",
        text
    )

    if keyword_match:
        result["keyword"] = float(
            keyword_match.group(1)
        )

    # -------------------------
    # Completeness
    # -------------------------

    completeness_match = re.search(
        r"Completeness:\s*([\d.]+)",
        text
    )

    if completeness_match:
        result["completeness"] = float(
            completeness_match.group(1)
        )

    # -------------------------
    # Ideal Answer
    # -------------------------

    ideal_match = re.search(
        r"Ideal Answer:(.*)$",
        text,
        re.DOTALL
    )

    if ideal_match:
        result["ideal_answer"] = (
            ideal_match.group(1).strip()
        )

    # -------------------------
    # Strengths / Weaknesses / Suggestions
    # -------------------------

    current_section = None

    for line in text.split("\n"):

        line = line.strip()

        if "Strengths" in line:
            current_section = "strengths"

        elif "Weaknesses" in line:
            current_section = "weaknesses"

        elif "Suggestions" in line:
            current_section = "suggestions"

        elif "Ideal Answer" in line:
            current_section = None

        elif line.startswith("-"):

            item = line.replace("-", "").strip()

            if current_section:
                result[current_section].append(item)

    return result