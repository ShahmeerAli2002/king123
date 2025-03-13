import streamlit as st
import time
import random
from datetime import datetime
import base64

def add_bg_color():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(45deg, #FF1493, #FF69B4, #FF1493);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        .stApp {
            background: linear-gradient(45deg, #FF1493, #FF69B4, #FF1493);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        .message-box {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 20px;
            font-size: 22px;
            color: #FFF;
            text-align: center;
            font-weight: bold;
            animation: fadeIn 2s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            backdrop-filter: blur(5px);
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .heart {
            color: red;
            font-size: 35px;
            animation: heartbeat 1.5s infinite, float 3s ease-in-out infinite;
            position: relative;
            display: inline-block;
        }
        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.3); }
            50% { transform: scale(1); }
            75% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }
        @keyframes float {
            0% { top: 0px; }
            50% { top: -10px; }
            100% { top: 0px; }
        }
        .love-counter {
            font-size: 24px;
            color: #FFB6C1;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .goal-item {
            padding: 10px;
            margin: 5px 0;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .goal-item:hover {
            transform: scale(1.05);
            background: rgba(255,255,255,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def love_duration(start_date):
    today = datetime.today()
    love_days = (today - start_date).days
    return love_days

love_messages = [
    "Alishba, Tum meri zindagi ka sabse khoobsurat hissa ho ❤️",
    "Meri duniya sirf tumse shuru hoti hai aur tum par hi khatam 💖",
    "Tum meri muskurahat ki wajah ho 💕",
    "Har pal tumhari yaadon se bhara hota hai 🌹",
    "Tum meri dil ki sabse pyari dhadkan ho 💘",
    "Tumhare bina zindagi adhuri hai 💝",
    "Tum mere dil ki dharkan ho 💗",
    "Tumhare saath har lamha khoobsurat hai 💓",
    "Meri mohabbat tumse beintehaa hai 💞",
    "Tum meri zindagi ki khushi ho 💕"
]

st.title("💖 Love Story App for Alishba 💖")
add_bg_color()

col1, col2 = st.columns(2)

with col1:
    st.write("Click for your special love message! 💌")
    if st.button("💞 Click Here Alishba 💞"):
        love_message = random.choice(love_messages)
        st.markdown(f'<div class="message-box">{love_message} ❤️</div>', unsafe_allow_html=True)

with col2:
    start_date = datetime(2021, 2, 14)
    days = love_duration(start_date)
    st.markdown(f'<div class="love-counter">❤️ {days} Days of Love ❤️<br>{days*24} Hours<br>{days*1440} Minutes<br>of endless love!</div>', unsafe_allow_html=True)

for _ in range(15):
    st.markdown(f'<div class="heart" style="margin-left: {random.randint(0, 100)}%">❤️</div>', unsafe_allow_html=True)
    time.sleep(0.2)

st.subheader("🌟 Our Love Goals")
love_goals = [
    "Go on a romantic trip to Paris ✈️",
    "Watch sunset together at the beach 🌅",
    "Write 100 love letters 📜",
    "Have a candlelight dinner under stars 🕯️",
    "Create a love song together 🎵",
    "Plant a love tree 🌳",
    "Make a time capsule of our memories 📦"
]

for goal in love_goals:
    st.markdown(f'<div class="goal-item">✨ {goal}</div>', unsafe_allow_html=True)

if st.button("💝 Click for a Special Surprise 💝"):
    st.balloons()
    st.snow()
    st.markdown('<div class="message-box">Alishba, you are my everything! My love for you grows stronger with each passing moment! 💖</div>', unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
    # Additional surprise elements
    st.markdown('<div class="message-box">Every moment with you is magical ✨</div>', unsafe_allow_html=True)
    st.write("💝 Our Love Story Timeline 💝")
    st.write("First Meet 👫 → First Date 🎬 → First Kiss 💋 → Forever Together 💑")