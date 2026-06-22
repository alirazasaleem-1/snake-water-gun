import streamlit as st
import random

# ---------------- TITLE ----------------
st.title("🎮 Snake Water Gun Battle Arena")
st.caption("Built by Ali Raza Saleem • CS Student | Python & AI Learner")

st.markdown("---")

# ---------------- SESSION STATE INIT (VERY IMPORTANT) ----------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0

if "round" not in st.session_state:
    st.session_state.round = 0

# ---------------- GAME DATA ----------------
choices = {"🐍 Snake": 1, "💧 Water": -1, "🔫 Gun": 0}
reverse = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}

# ---------------- SCOREBOARD ----------------
st.sidebar.header("🏆 Scoreboard")
st.sidebar.write(f"👤 You: {st.session_state.user_score}")
st.sidebar.write(f"🤖 Computer: {st.session_state.comp_score}")
st.sidebar.write(f"🔁 Round: {st.session_state.round}/5")

st.sidebar.markdown("---")
st.sidebar.write("🎯 Play 5 rounds to decide the winner")

# ---------------- GAME PLAY ----------------
if st.session_state.round < 5:

    user_choice = st.radio("👇 Choose your move:", list(choices.keys()))

    if st.button("⚔️ Play Round"):

        computer = random.choice([-1, 0, 1])
        user = choices[user_choice]

        st.session_state.round += 1

        st.markdown("### 🎮 Round Result")

        st.write(f"👤 You chose: **{user_choice}**")
        st.write(f"🤖 Computer chose: **{reverse[computer]}**")

        if user == computer:
            st.info("🤝 It's a Draw!")
        elif (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
            st.session_state.user_score += 1
            st.success("🎉 You Win this round!")
        else:
            st.session_state.comp_score += 1
            st.error("💀 Computer wins this round!")

# ---------------- GAME STATUS ----------------
st.markdown("---")
st.subheader("📊 Game Status")

if st.session_state.round == 0:
    st.write("🎮 Start your first round!")
elif st.session_state.round < 5:
    st.write(f"🔁 Round {st.session_state.round}/5 in progress...")
else:
    st.write("🏁 Game finished!")

# ---------------- FINAL RESULT ----------------
if st.session_state.round >= 5:

    st.markdown("### 🏆 Final Result")

    if st.session_state.user_score > st.session_state.comp_score:
        st.success("🏆 You WON the match!")
    elif st.session_state.user_score < st.session_state.comp_score:
        st.error("💀 Computer WON the match!")
    else:
        st.warning("🤝 It's a DRAW!")

# ---------------- RESET ----------------
st.markdown("---")
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.round = 0
    st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:14px; color:gray;">
🎮 Built with Python & Streamlit • Simple Game Project <br>
⚡ Clean • Fun • Interactive
</div>
""", unsafe_allow_html=True)
