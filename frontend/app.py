import streamlit as st
import pandas as pd
from styles import load_css
from backend.question_generator import generate_question
from backend.dashboard import (
    total_attempts,
    average_score,
    highest_score,
    recent_attempts
)
# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="AI Interview Evaluator",
    page_icon="🤖",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.title("🎯 AI Interview")

    st.markdown("---")

    st.metric("Interviews", "0")
    st.metric("Average Score", "0%")
    st.metric("Best Score", "0%")

    st.markdown("---")

    st.info("Practice interviews powered by Gemini AI")

# ------------------------------------------------
# HERO SECTION
# ------------------------------------------------

st.markdown("""
<div class="hero">
<h1>🤖 AI Interview Evaluation System</h1>
<p>Powered by Gemini AI</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Questions Attempted", "12")

with col2:
    st.metric("Average Score", "25%")

with col3:
    st.metric("Best Score", "76%")

st.markdown("---")

# ------------------------------------------------
# INTERVIEW CONFIGURATION
# ------------------------------------------------

st.subheader("⚙ Interview Configuration")

col1, col2, col3 = st.columns(3)

with col1:
    role = st.selectbox(
        "Role",
        [
            "Java Developer",
            "Python Developer",
            "Data Analyst",
            "AI/ML Engineer"
        ]
    )

with col2:
    experience = st.selectbox(
        "Experience",
        [
            "Fresher",
            "1-2 Years",
            "3-5 Years"
        ]
    )

with col3:
    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

# ------------------------------------------------
# GENERATE QUESTION
# ------------------------------------------------

if st.button("🚀 Generate AI Interview"):

    with st.spinner("Generating AI Interview Question..."):
        data = generate_question(
            role,
            experience,
            difficulty
        )

        st.session_state["question"] = data["question"]
        st.session_state["type"] = data["type"]

# ------------------------------------------------
# QUESTION SECTION
# ------------------------------------------------

if "question" in st.session_state:

    st.markdown("---")

    st.subheader("📝 Generated Question")
    if st.session_state["type"] == "coding":
        st.warning("💻 Coding Question")

    else:
        st.info("🎤 Theory Question")

    st.info("⏱ Recommended Time: 2 Minutes")

    st.markdown(
        f"""
        <div class="question-card">
            {st.session_state["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    answer_mode = None
    audio = None
    # ------------------------------------------------
    # ANSWER SECTION
    # ------------------------------------------------

    if st.session_state["type"] == "coding":

        st.radio(
            "Answer Mode",
            ["💻 Code Answer"],
            disabled=True
        )

        st.subheader("💻 Code Editor")

        answer = st.text_area(
            "Write your code here",
            height=300
        )

    else:

        answer_mode = st.radio(
            "Answer Mode",
            [
                "⌨️ Text Answer",
                "🎤 Voice Answer"
            ]
        )

        if answer_mode == "⌨️ Text Answer":

            st.subheader("💬 Your Answer")

            answer = st.text_area(
                "Type your answer here",
                height=250
            )

        else:

            st.subheader("🎤 Voice Answer")

            from streamlit_mic_recorder import mic_recorder

            audio = mic_recorder(
                start_prompt="🎙 Start Recording",
                 stop_prompt="⏹ Stop Recording",
                 key="voice_answer"
            )

    if answer_mode == "🎤 Voice Answer":

        if audio:
            st.success("Voice recorded successfully!")

            st.write("Audio Format:", audio["format"])
            st.write("Sample Rate:", audio["sample_rate"])

            import tempfile
            from backend.speech_to_text import audio_to_text

            with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".webm"
            ) as temp_audio:
                temp_audio.write(audio["bytes"])
                temp_audio_path = temp_audio.name

            answer = audio_to_text(temp_audio_path)

            st.subheader("📝 Transcript")
            st.info(answer)

    # ------------------------------------------------
    # EVALUATE ANSWER
    # ------------------------------------------------

if st.button("📊 Evaluate Answer"):

    if answer.strip() == "":
        st.warning("Please enter an answer.")

    else:

        from backend.evaluator import evaluate_answer
        from backend.parser import parse_feedback

        with st.spinner("AI Evaluating Your Answer..."):

            feedback_text = evaluate_answer(
                st.session_state["question"],
                answer
            )

            result = parse_feedback(
                feedback_text
            )
            from backend.history import save_attempt

            save_attempt(
                st.session_state["question"],
                result["score"],
                role,
                difficulty
            )

        st.session_state["result"] = result
        st.session_state["feedback_text"] = feedback_text

    # ------------------------------------------------
    # SHOW RESULT
    # ------------------------------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.markdown("---")

    st.subheader("📊 Evaluation Result")

    st.progress(result["score"])

    st.metric(
        "Final Score",
        f"{result['score']} / 100"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success("✅ Strengths")

        for item in result["strengths"]:
            st.write("•", item)

    with c2:

        st.error("❌ Weaknesses")

        for item in result["weaknesses"]:
            st.write("•", item)

    with c3:

        st.info("💡 Suggestions")

        for item in result["suggestions"]:
            st.write("•", item)

    st.download_button(
        label="📄 Download Evaluation Report",
        data=st.session_state["feedback_text"],
        file_name="Interview_Report.txt",
        mime="text/plain"
    )
    st.markdown("""
    <style>

    div.stButton > button {
        height: 65px;
        font-size: 22px;
        font-weight: 700;
        border-radius: 15px;

        background: linear-gradient(
            135deg,
            #667eea,
            #764ba2
        );

        color: white;
        border: none;

        box-shadow: 0px 6px 20px rgba(102,126,234,0.4);

        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 8px 25px rgba(102,126,234,0.6);
    }

    </style>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        show_solution = st.button(
            "📖 View Ideal Answer",
            use_container_width=True
        )


    if show_solution:
        from backend.solution_generator import generate_solution

        with st.spinner("Generating ideal answer..."):
            solution = generate_solution(
                st.session_state["question"]
            )

        st.markdown("""
        <style>
        .ideal-answer-box {
            background: linear-gradient(
                135deg,
                #1e3c72,
                #2a5298,
                #4e54c8
            );
            padding: 30px;
            border-radius: 20px;
            margin-top: 20px;
            margin-bottom: 20px;
            color: white;
            font-size: 18px;
            line-height: 1.8;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.4);
        }
        .ideal-title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="ideal-answer-box">
                <div class="ideal-title">
                    📖 Ideal Answer
                </div>
                {solution}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ==========================================
        # DASHBOARD
        # ==========================================

        st.markdown("---")

        st.header("📊 Performance Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Questions Attempted",
                total_attempts()
            )

        with col2:
            st.metric(
                "Average Score",
                average_score()
            )

        with col3:
            st.metric(
                "Highest Score",
                highest_score()
            )

        # OUTSIDE THE COLUMNS
        st.markdown("---")

        st.subheader("📜 Recent Attempts")

        history = recent_attempts()

        if history:

            df = pd.DataFrame(history)

            df = df[
                [
                    "question",
                    "score",
                    "role",
                    "difficulty",
                    "date"
                ]
            ]

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info("No attempts found yet.")