import streamlit as st
from gtts import gTTS
import os
import math

# Function to handle voice in Streamlit
def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp_audio.mp3")
    st.audio("temp_audio.mp3", format="audio/mp3", autoplay=True)

st.title("Voice Calculator - Igris Blood Red")

# Sidebar for instructions or status
st.sidebar.markdown("### Choose Operator:")
st.sidebar.text("1-Add\n2-Subtract\n3-Multiply\n4-Divide\n5-Square\n6-Cube\n7-Square Root")

# User Choice
choice = st.selectbox("Select your operator:", 
                      ["1 (Add)", "2 (Subtract)", "3 (Multiply)", "4 (Divide)", 
                       "5 (Square)", "6 (Cube)", "7 (Square Root)"])

# Extracting only the number from choice
c = choice[0]

# Input Section
a, b, N = 0, 0, 0
if c in ["1", "2", "3", "4"]:
    a = st.number_input("Enter first number:", value=0)
    b = st.number_input("Enter second number:", value=0)
elif c in ["5", "6", "7"]:
    N = st.number_input("Enter your number:", value=0)

if st.button("Calculate"):
    result = 0
    msg = ""

    if c == "1":
        result = a + b
        msg = f"You chose addition and your result is {result}"
    elif c == "2":
        result = a - b
        msg = f"You chose subtraction and your result is {result}"
    elif c == "3":
        result = a * b
        msg = f"You chose multiplication and your result is {result}"
    elif c == "4":
        if b != 0:
            result = a / b
            msg = f"You chose division and your result is {result}"
        else:
            msg = "Error: Denominator cannot be zero"
            st.error(msg)
    elif c == "5":
        result = N * N
        msg = f"You chose squaring and your result is {result}"
    elif c == "6":
        result = N * N * N
        msg = f"You chose cubing and your result is {result}"
    elif c == "7":
        result = math.sqrt(N)
        msg = f"You chose square root and your result is {result}"

    if msg and "Error" not in msg:
        st.success(f"Result: {result}")
        say(msg)
    elif "Error" in msg:
        say(msg)
