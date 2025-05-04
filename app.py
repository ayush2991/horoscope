import streamlit as st
import random
from datetime import timedelta

@st.cache_data(ttl=timedelta(minutes=10))
def random_horoscope(name, zodiac):
    horoscopes = [
        "Today is a great day to start something new!",
        "You will find success in your endeavors today.",
        "A surprise is waiting for you around the corner.",
        "You may face some challenges, but you will overcome them.",
        "Your creativity will shine today.",
        "A good day for socializing and making new friends.",
        "You will receive good news from a friend.",
        "Take some time to relax and recharge.",
        "A financial opportunity may present itself.",
        "You will find clarity in a situation that has been troubling you."
    ]
    return random.choice(horoscopes)

def main():
    st.title("Welcome to Your Daily Horoscope")
    st.write("Get ready to explore your daily insights!")
    # Get user's name from a free text form and zodiac from a dropdown
    name = st.text_input("Enter your name:")
    zodiac = st.selectbox("Select your zodiac sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
                                                      "Libra", "Scorpio", "Sagittarius", "Capricorn", 
                                                      "Aquarius", "Pisces"])
    horoscope = random_horoscope(name, zodiac)
    # Show only after the user has entered their name
    if name:
        st.write(f"Hello, {name}! Here is your horoscope for today:")
        st.success(horoscope)
    else:
        st.write("Please enter your name to see your horoscope.")
    

if __name__ == "__main__":
    main()