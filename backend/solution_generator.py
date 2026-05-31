import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_solution(question):

    prompt = f"""
    You are an expert technical interviewer.

    Interview Question:
    {question}

    Give:
    1. A concise ideal answer.
    2. A short explanation.
    3. If relevant, include a simple example.

    Keep the answer beginner friendly.
    """

    response = model.generate_content(prompt)

    return response.text