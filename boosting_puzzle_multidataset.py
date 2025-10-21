import streamlit as st
import pandas as pd

st.set_page_config(page_title="Boosting Puzzle - Multi Dataset", layout="centered")

st.title("🧩 Boosting Puzzle: Learn Boosting the Fun Way!")
st.write("Choose a real-world scenario and guess the outcomes — just like a weak learner in a boosting model!")

# ------------------------------------
# Datasets (hidden labels included)
# ------------------------------------

datasets = {
    "E-Commerce (Who Will Buy?)": {
        "emoji": "🛍️",
        "description": "Predict which users will buy a product based on their profile.",
        "data": pd.DataFrame({
            "Person": ["A", "B", "C", "D", "E", "F"],
            "Age": [22, 35, 30, 19, 40, 28],
            "Income": ["Low", "High", "Medium", "High", "High", "Low"],
            "Browsing (min)": [5, 20, 10, 3, 25, 15],
            "Label": [0, 1, 1, 0, 1, 1]
        }),
        "boosting_rules": [
            "Rule 1: If Income = High → Predict Buy",
            "Rule 2: If Browsing Time > 10 → Predict Buy",
            "Rule 3: If Age > 25 → Predict Buy"
        ]
    },
    "Finance (Loan Approval)": {
        "emoji": "🏦",
        "description": "Predict which applicants get their loan approved.",
        "data": pd.DataFrame({
            "Person": ["P1", "P2", "P3", "P4", "P5", "P6"],
            "Credit Score": [750, 650, 700, 600, 800, 720],
            "Income (LPA)": [8, 5, 6, 4, 9, 7],
            "Loan (L)": [3, 6, 4, 5, 2, 5],
            "Label": [1, 0, 1, 0, 1, 1]
        }),
        "boosting_rules": [
            "Rule 1: If Credit Score > 700 → Approve",
            "Rule 2: If Income > 6 → Approve",
            "Rule 3: If Loan Amount < 4 → Approve"
        ]
    },
    "Healthcare (Disease Prediction)": {
        "emoji": "🏥",
        "description": "Predict which patients have the disease based on health indicators.",
        "data": pd.DataFrame({
            "Person": ["H1", "H2", "H3", "H4", "H5", "H6"],
            "Age": [55, 40, 60, 30, 50, 45],
            "BP": ["High", "Normal", "High", "Normal", "High", "Normal"],
            "Sugar": ["High", "Low", "High", "Normal", "Normal", "High"],
            "Label": [1, 0, 1, 0, 1, 1]
        }),
        "boosting_rules": [
            "Rule 1: If BP = High → Predict Disease",
            "Rule 2: If Sugar = High → Predict Disease",
            "Rule 3: If Age > 45 → Predict Disease"
        ]
    },
    "Spam Detection (Email Classification)": {
        "emoji": "📧",
        "description": "Predict which emails are spam based on their content.",
        "data": pd.DataFrame({
            "Email": ["E1", "E2", "E3", "E4", "E5", "E6"],
            "Contains 'Offer'": ["Yes", "No", "Yes", "No", "Yes", "No"],
            "Has Link": ["Yes", "Yes", "No", "No", "Yes", "Yes"],
            "Sender Trusted": ["No", "Yes", "No", "Yes", "No", "No"],
            "Label": [1, 0, 1, 0, 1, 1]
        }),
        "boosting_rules": [
            "Rule 1: If Contains 'Offer' = Yes → Spam",
            "Rule 2: If Has Link = Yes → Spam",
            "Rule 3: If Sender Trusted = Yes → Not Spam"
        ]
    }
}

# ------------------------------------
# Dataset Selector
# ------------------------------------
choice = st.selectbox("Choose a dataset / scenario", list(datasets.keys()))

info = datasets[choice]
emoji = info["emoji"]
st.markdown(f"### {emoji} Dataset: {choice}")
st.write(info["description"])

data = info["data"]
st.dataframe(data.drop(columns=["Label"]))

# ------------------------------------
# Guessing Section
# ------------------------------------
st.markdown("### 🤔 Select who you think are positive cases (1️⃣):")

user_guesses = {}
cols = st.columns(3)
for i, row in data.iterrows():
    label = row[0]
    details = ", ".join([f"{col}: {row[col]}" for col in data.columns[1:-1]])
    with cols[i % 3]:
        user_guesses[label] = st.checkbox(f"{label} ({details})")

# ------------------------------------
# Check Answers
# ------------------------------------
if st.button("Check Answers"):
    st.markdown("---")
    correct = 0
    total = len(data)

    for i, row in data.iterrows():
        person = row[0]
        actual = row["Label"]
        guess = 1 if user_guesses[person] else 0

        if guess == actual:
            st.success(f"✅ {person}: Correct!")
            correct += 1
        else:
            st.error(f"❌ {person}: Wrong!")

    st.markdown(f"## 🎯 Score: {correct}/{total}")

    if correct == total:
        st.balloons()
        st.success("Perfect! You matched the boosted model! 🚀")
    else:
        st.info("Not perfect yet — just like a weak learner! See how boosting can improve you 👇")

    # ------------------------------------
    # Boosting Explanation
    # ------------------------------------
    with st.expander("💡 See how Boosting improves this"):
        st.write("Each boosting round learns from previous mistakes. Here’s how the rules evolve:")
        for r in info["boosting_rules"]:
            st.markdown(f"- {r}")
        st.write("✅ Final boosted model combines these weak rules to achieve near-perfect accuracy!")

