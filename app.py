import streamlit as st
import random

# ---------------- UI ----------------
st.title("🎮 Snake Water Gun – Battle Arena")
st.caption("Created by Ali Raza Saleem")

st.markdown("---")

# ---------------- INIT STATE ----------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.round = 0
    st.session_state.history = []

# ---------------- GAME DATA ----------------
choices = {"Snake 🐍": 1, "Water 💧": -1, "Gun 🔫": 0}
reverse = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

# ---------------- SIDEBAR SCOREBOARD ----------------
st.sidebar.header("🏆 Scoreboard")
st.sidebar.write(f"👤 You: {st.session_state.user_score}")
st.sidebar.write(f"🤖 Computer: {st.session_state.comp_score}")
st.sidebar.write(f"🔁 Round: {st.session_state.round}/5")

# ---------------- GAME END CHECK ----------------
def check_winner():
    if st.session_state.round >= 5:
        if st.session_state.user_score > st.session_state.comp_score:
            st.success("🏆 You WON the Battle!")
        elif st.session_state.user_score < st.session_state.comp_score:
            st.error("💀 Computer WON the Battle!")
        else:
            st.warning("🤝 It's a DRAW match!")

# ---------------- GAME UI ----------------
if st.session_state.round < 5:

    user_choice = st.radio("Choose your move:", list(choices.keys()))

    if st.button("⚔️ Play Round"):

        computer = random.choice([-1, 0, 1])
        user = choices[user_choice]

        st.session_state.round += 1

        result_text = ""

        if user == computer:
            result_text = "Draw 🤝"
        elif (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
            st.session_state.user_score += 1
            result_text = "You Win 🎉"
        else:
            st.session_state.comp_score += 1
            result_text = "You Lose 😢"

        # save history
        st.session_state.history.append(
            f"Round {st.session_state.round}: You({reverse[user]}) vs Computer({reverse[computer]}) → {result_text}"
        )

        st.rerun()

# ---------------- GAME HISTORY ----------------
st.markdown("### 📜 Match History")
for h in st.session_state.history:
    st.write(h)

# ---------------- END SCREEN ----------------
check_winner()

# ---------------- RESET BUTTON ----------------
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.round = 0
    st.session_state.history = []
    st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:gray; font-size:14px;">
Built with Python + Streamlit • Mini Game Project • 2026
</div>
""", unsafe_allow_html=True)
