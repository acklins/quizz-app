import streamlit as st  # type: ignore[reportMissingImports]

#Page config ──────────
st.set_page_config(
    page_title="Web Essentials Quiz",
    page_icon="🐍",
    layout="centered"
)
st.title("🐍 Web Essentials Quiz")
st.caption("Test your knowledge of HTML, CSS,JavaScript, Python and APIs.")

st.divider()

QUESTIONS = [
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Tech Modern Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "Hyper Text Markup Language",
        "explanation": "HTML is used to structure content on web pages."
    },
    {
        "question": "Which CSS property controls space inside a border?",
        "options": [
            "margin",
            "padding",
            "display",
            "position"
        ],
        "answer": "padding",
        "explanation": "Padding creates space between content and its border."
    },
    {
        "question": "Which JavaScript function makes HTTP requests?",
        "options": [
            "querySelector()",
            "JSON.stringify()",
            "fetch()",
            "alert()"
        ],
        "answer": "fetch()",
        "explanation": "fetch() is used to make HTTP requests to APIs."
    },
    {
        "question": "Which Python data type stores key-value pairs?",
        "options": [
            "list",
            "tuple",
            "set",
            "dictionary"
        ],
        "answer": "dictionary",
        "explanation": "Dictionaries store data as key-value pairs."
    },
    {
        "question": "Which HTTP status code means Not Found?",
        "options": [
            "200",
            "201",
            "404",
            "500"
        ],
        "answer": "404",
        "explanation": "HTTP 404 means the requested resource was not found."
    }
]
# ── Session state initialization ──
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected" not in st.session_state:
    st.session_state.selected = None

if "show_results" not in st.session_state:
    st.session_state.show_results = False

# ═════════════════
# RESULTS SCREEN
if st.session_state.show_results:

    total_questions = len(QUESTIONS)

    percentage = (
        st.session_state.score / total_questions
    ) * 100

    st.header("Quiz Complete!")

    st.metric(
        label="Final Score",
        value=f"{st.session_state.score} / {total_questions}"
    )

    if percentage >= 80:
        st.success(f"Excellent work! You scored {percentage:.0f}%.")

    elif percentage >= 60:
        st.info(f"Good job! You scored {percentage:.0f}%.")

    else:
        st.warning(f"Keep practicing! You scored {percentage:.0f}%")

    st.progress(percentage / 100)

    if st.button("Restart Quiz"):

        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.show_results = False

        st.rerun()

    st.stop()
#══════════════════════════════════════
# QUIZ SCREEN
# ═════════════════════════════════════
q_index = st.session_state.current_q

total_qs = len(QUESTIONS)

current_question = QUESTIONS[q_index]

#progress indicator
st.write(f"Question {q_index + 1} of {total_qs}")

progress = q_index / total_qs

st.progress(progress)

#Question and answer options display
st.subheader(current_question["question"])

choice = st.radio(
    "Choose your answer:",
    current_question["options"],
    index=None,
    key=f"q_{q_index}",
    disabled=st.session_state.answered
)

#Submit button
if not st.session_state.answered:

    if st.button("Submit Answer"):

        if choice is None:
            st.warning("Please select an answer first.")
        else:
            st.session_state.selected = choice
            st.session_state.answered = True

            if choice == current_question["answer"]:
                st.session_state.score += 1

            st.rerun()

#Display feedback after submission
if st.session_state.answered:

    if st.session_state.selected == current_question["answer"]:
        st.success("Correct! Great job!")

    else: 
        st.error("Incorrect answer.")

        st.write(
            f"Correct answer: **{current_question['answer']}**"
        )
    st.info(current_question["explanation"])

    #The next queestion button

    if q_index == total_qs - 1:
        button_label = "Finish Quiz"
    else:
        button_label = "Next Question"

    if st.button(button_label):

        if q_index == total_qs - 1:

            st.session_state.show_results = True
        else:

            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected = None

        st.rerun()