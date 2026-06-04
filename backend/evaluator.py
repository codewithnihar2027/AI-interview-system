import re

import google.generativeai as genai

from config import GEMINI_API_KEY


from backend.nlp_scoring import (
    semantic_similarity_score,
    keyword_coverage_score,
    completeness_score
)

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel(
    "gemini-2.5-flash"
)




def generate_ideal_answer(question):

    prompt = f"""
    You are an expert technical interviewer.

    Interview Question:
    {question}

    Give a concise ideal answer.

    Keep it accurate and professional.
    """

    response = gemini_model.generate_content(
        prompt
    )

    return response.text.strip()


def generate_feedback(
        question,
        answer,
        final_score
):

    prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Final Score:
    {final_score}

    Return EXACTLY in this format:

    Strengths:
    - point 1
    - point 2

    Weaknesses:
    - point 1
    - point 2

    Suggestions:
    - point 1
    - point 2
    """

    response = gemini_model.generate_content(
        prompt
    )

    return response.text


def evaluate_answer(
        question,
        answer
):

    # -------------------------
    # Generate Ideal Answer
    # -------------------------

    ideal_answer = generate_ideal_answer(
        question
    )

    # -------------------------
    # NLP Scores
    # -------------------------

    semantic = semantic_similarity_score(
        ideal_answer,
        answer
    )

    keyword = keyword_coverage_score(
        ideal_answer,
        answer
    )

    completeness = completeness_score(
        ideal_answer,
        answer
    )

    # -------------------------
    # PPT Formula
    # -------------------------

    final_score = round(
        (
            0.7 * semantic +
            0.2 * keyword +
            0.1 * completeness
        )
    )

    if final_score > 100:
        final_score = 100

    if final_score < 0:
        final_score = 0

    # -------------------------
    # Gemini Feedback
    # -------------------------

    feedback = generate_feedback(
        question,
        answer,
        final_score
    )

    # -------------------------
    # Parser Compatible Output
    # -------------------------

    result = f"""
    Score: {final_score}

    Semantic Similarity: {semantic}

    Keyword Coverage: {keyword}

    Completeness: {completeness}

    Strengths:
    """

    strengths_match = re.search(
        r"Strengths:(.*?)(Weaknesses:|$)",
        feedback,
        re.DOTALL
    )

    weaknesses_match = re.search(
        r"Weaknesses:(.*?)(Suggestions:|$)",
        feedback,
        re.DOTALL
    )

    suggestions_match = re.search(
        r"Suggestions:(.*)",
        feedback,
        re.DOTALL
    )

    if strengths_match:
        result += strengths_match.group(1)

    result += "\n\nWeaknesses:\n"

    if weaknesses_match:
        result += weaknesses_match.group(1)

    result += "\n\nSuggestions:\n"

    if suggestions_match:
        result += suggestions_match.group(1)

    result += f"""

    Ideal Answer:
    {ideal_answer}
    """

    return result