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

    if (
        ("explain" in question_lower or "describe" in question_lower)
        and
        (
            "write" in question_lower
            or "implement" in question_lower
            or "code" in question_lower
            or "program" in question_lower
        )
    ):
        qtype = "mixed"

    elif any(word in question_lower for word in [
        "write",
        "code",
        "program",
        "implement",
        "algorithm",
        "function",
        "class"
    ]):
        qtype = "coding"

    else:
        qtype = "theory"

    # ------------------------------------------------
    # RETURN DATA
    # ------------------------------------------------

    return {
        "question": question,
        "type": qtype
    }