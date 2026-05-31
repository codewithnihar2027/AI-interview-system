import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def evaluate_answer(question, answer):

    prompt = f"""
    You are an expert technical interviewer.

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and return EXACTLY in this format:

    Score: <number between 0 and 100>

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

    response = model.generate_content(prompt)

    return response.text