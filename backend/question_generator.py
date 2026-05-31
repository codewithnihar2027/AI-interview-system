import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_question(role, experience, difficulty):

    prompt = f"""
    You are a professional technical interviewer.

    Generate ONE interview question.

    Role: {role}
    Experience: {experience}
    Difficulty: {difficulty}

    Rules:
    - Ask only ONE question.
    - The question can be theoretical, coding, or mixed.
    - Return only the question text.
    """

    response = model.generate_content(prompt)

    question = response.text.strip()

    question_lower = question.lower()

    # ------------------------------------------------
    # DETECT QUESTION TYPE
    # ------------------------------------------------

    if any(word in question_lower for word in [
        "write a program",
        "write code",
        "implement",
        "coding question",
        "algorithm",
        "debug",
        "solve the problem",
        "create a function"
    ]):
        qtype = "coding"

    elif any(word in question_lower for word in [
        "explain",
        "describe",
        "difference",
        "what is",
        "why",
        "advantages",
        "disadvantages"
    ]):
        qtype = "theory"

    else:
        qtype = "theory"
    # ------------------------------------------------
    # RETURN DATA
    # ------------------------------------------------

    return {
        "question": question,
        "type": qtype
    }