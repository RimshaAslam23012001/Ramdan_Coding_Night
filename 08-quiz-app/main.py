import streamlit as st  # 🚀 for creating the web app
import random  # 🎲 for random selection of questions
import time  # ⏳ for adding delay

st.title("📝 Quiz App")  # 🏆 Title of the quiz app

# List of questions and answers 📚
questions = [
    {
        "question": "What is the capital of Pakistan? 🇵🇰",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan? 🇵🇰",
        "options": ["Muhammad Ali Jinnah", "Allama Iqbal", "Liaquat Ali Khan", "Zulfiqar Ali Bhutto"],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "What is the national animal of Pakistan? 🦌",
        "options": ["Markhor", "Lion", "Tiger", "Elephant"],
        "answer": "Markhor"
    },
    {
        "question": "What is the national flower of Pakistan? 🌸",
        "options": ["Rose", "Jasmine", "Lily", "Sunflower"],
        "answer": "Jasmine"
    },
    {
        "question": "What is the national bird of Pakistan? 🦆",
        "options": ["Eagle", "Parrot", "Peacock", "Sparrow"],
        "answer": "Chukar"
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan? 🌃",
        "options": ["Karachi", "Lahore", "Islamabad", "Faisalabad"],
        "answer": "Karachi"
    }
]

# Check if there is a current question in session state 🌟
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state 🧐
question = st.session_state.current_question
st.subheader(question["question"])

# Show options to the user 📋
selected_option = st.radio("Choose your answer 💡", question["options"], key="answer")

# Handle the submission of the answer 📝
if st.button("Submit"):
    if selected_option == question["answer"]:
        st.success("Correct! 🎉")  # 🎉 Success message when the answer is correct
    else:
        st.error("❌Incorrect!  The correct answer is " + question['answer'])  # ❌ Error message for wrong answers

    time.sleep(3)  # ⏳ Wait for 3 seconds before showing the next question

    # Choose a new random question for the next round 🔄
    st.session_state.current_question = random.choice(questions)
    st.rerun()  # 🔁 Reload the app to display the next question
