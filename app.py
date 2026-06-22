# ---------------- GAME ----------------
if st.session_state.round < 5:

    user_choice = st.radio("👇 Choose your move:", list(choices.keys()))

    if st.button("⚔️ Play Round"):

        computer = random.choice([-1, 0, 1])
        user = choices[user_choice]

        st.session_state.round += 1

        st.write("### 🎮 Round Result")
        st.write(f"👤 You: **{user_choice}**")
        st.write(f"🤖 Computer: **{reverse[computer]}**")

        if user == computer:
            st.info("🤝 Draw")
        elif (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
            st.session_state.user_score += 1
            st.success("🎉 You Win!")
        else:
            st.session_state.comp_score += 1
            st.error("💀 Computer Wins")

# ---------------- ALWAYS SHOW STATUS ----------------
st.markdown("---")
st.subheader("📊 Game Status")

if st.session_state.round == 0:
    st.write("🎮 Start playing your first round!")
elif st.session_state.round < 5:
    st.write(f"🔁 Round {st.session_state.round}/5 in progress...")
else:
    st.write("🏁 Game Finished!")

# ---------------- FINAL RESULT (ALWAYS VISIBLE) ----------------
if st.session_state.round >= 5:

    st.markdown("### 🏆 Final Result")

    if st.session_state.user_score > st.session_state.comp_score:
        st.success("🏆 You WON the match!")
    elif st.session_state.user_score < st.session_state.comp_score:
        st.error("💀 Computer WON the match!")
    else:
        st.warning("🤝 It's a DRAW!")

# ---------------- RESET ALWAYS VISIBLE ----------------
st.markdown("---")
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.round = 0
    st.rerun()
