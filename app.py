import streamlit as st
import random

# ---------------- TITLE ----------------
st.title("🎮 Snake Water Gun")
st.caption("Created by Ali Raza Saleem")

st.markdown("---")

# ---------------- GAME STATE ----------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.round = 0

# ---------------- DATA ----------------
choices = {"Snake 🐍": 1, "Water 💧": -1, "Gun 🔫": 0}
reverse = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

# ---------------- SCOREBOARD ----------------
st.sidebar.header("Score")
st.sidebar.write(f"You: {st.session_state.user_score}")
st.sidebar.write(f"Computer: {st.session_state.comp_score}")
st.sidebar.write(f"Round: {st.session_state.round}/5")

# ---------------- GAME ----------------
if st.session_state.round < 5:

    user_choice = st.radio("Choose your move:", list(choices.keys()))

    if st.button("Play"):

        computer = random.choice([-1, 0, 1])
        user = choices[user_choice]

        st.session_state.round += 1

        if user == computer:
            result = "Draw"
        elif (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
            st.session_state.user_score += 1
            result = "You Win"
        else:
            st.session_state.comp_score += 1
            result = "You Lose"

        st.write(f"You: {reverse[user]}")
        st.write(f"Computer: {reverse[computer]}")
        st.success(result)

# ---------------- END ----------------
if st.session_state.round == 5:
    st.markdown("---")

    if st.session_state.user_score > st.session_state.comp_score:
        st.success("🏆 You won the match!")
    elif st.session_state.user_score < st.session_state.comp_score:
        st.error("💀 Computer won the match!")
    else:
        st.warning("🤝 Match Draw")

# ---------------- RESET ----------------
if st.button("Restart"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.round = 0
    st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.write("Built with Python & Streamlit")
