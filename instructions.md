# Stateful Quiz App

**Module:** 6 — Web Essentials & Streamlit
**Estimated time:** 35 minutes

## Objective

Build a multiple-choice quiz app that tracks state across Streamlit re-runs using `st.session_state`.

## What You'll Build

A 5-question quiz application with full state management. Session state tracks the current question index, score, and whether the current question has been answered. Each question displays radio-button options and a Submit button that reveals right/wrong feedback. A Next button advances to the next question. A progress bar and "Question X of 5" indicator show progress throughout. After the final question, a results screen displays the final score and a Restart button that resets all state to defaults.

## Reference Code

The starter file (`starter.py`) provides a scaffold with TODOs — fill in each section, then compare with the solution.

## Running

```bash
streamlit run starter.py
```

## Deliverable

A Streamlit quiz app with 5 questions, session state tracking, progress indication, and a results screen.
