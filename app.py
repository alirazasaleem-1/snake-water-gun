'''
1 for snake 
-1 for water
0 for gun
'''

import random 
import streamlit as st 

st.set_page_config(page_title="Snake Water Gun", page_icon="🎮")

st.title("🐍💧🔫 Snake Water Gun Game")
st.caption("Created by Ali Raza Saleem")

with st.expander("ℹ️ About this game"):
    st.write("""
    Snake Water Gun is a simple logic-based Python game where you play against the computer.

    The game is designed to demonstrate basic programming concepts such as conditionals, randomness, and user interaction in a fun and interactive way.

    Built using Python and Streamlit to provide a lightweight web-based experience.
    """)
choices = {"Snake 🐍": 1, "Water 💧": -1, "Gun 🔫": 0}
reverse = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫" }

computer = random.choice([-1, 0, 1])

user_choice = st.radio("Choose your move:", list(choices.keys()))

if st.button("Play 🎮"):
    user =  choices[user_choice]

    st.write(f"You chose: **{user_choice}**")
    st.write(f"Computer chose: **{reverse[computer]}**")

    if user == computer:
        st.success("It's a Draw 🤝")
    elif (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
        st.success("You Win 🎉🔥")
    else:
        st.error("You lose")

st.markdown("---")

st.markdown("""
<div style="text-align: center; font-size: 14px; color: gray;">
    Built with Python & Streamlit • Simple Project for Learning & Practice <br>
    © 2026 • All Rights Reserved
</div>
""", unsafe_allow_html=True)