# *******************************************************
# Name ......... : streamlit_app.py
# Role ......... : Application to search for a birthdate in the digits of PI and mathematical demonstration
#                  of the sum of natural numbers
# Author ....... : Maxim Khomenko
# Version ...... : V1.0.0 dated 1/06/2024
# License ...... : Developed as part of the Architecture of Machines course
# Usage ........ : Run the script with "streamlit run streamlit_app.py" to start the application
# *******************************************************

import streamlit as st
import os
import requests
from datetime import datetime

# Function to download and save PI digits locally
def download_and_save_pi_digits():
    url = "https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt"
    response = requests.get(url)
    with open("pi_digits.txt", "w") as f:
        f.write(response.text[:1000000])  # Save the first million digits

# Function to load PI digits from a local file
def load_pi_digits():
    if not os.path.exists("pi_digits.txt"):
        download_and_save_pi_digits()
    with open("pi_digits.txt", "r") as f:
        return f.read()

# Load PI digits only once at the beginning
pi_digits = load_pi_digits().replace(".", "")

# Function to search for a birthdate in PI digits
def search_birthdate_in_pi(birthdate):
    birthdate_str = birthdate.replace("-", "")
    position = pi_digits.find(birthdate_str)
    return position

# Function to calculate the sum of the first n digits of PI
def sum_pi_digits(n):
    return sum(int(digit) for digit in pi_digits[:n])

# Streamlit Interface
st.title("Search for Birthdate in PI Digits")

# User input for birthdate
birthdate = st.text_input("Enter your birthdate (format YYYYMMDD):")

if birthdate:
    position = search_birthdate_in_pi(birthdate)
    if position != -1:
        st.write(f"Your birthdate is at position {position} in PI digits.")
    else:
        st.write("Your birthdate was not found in the first million digits of PI.")

    # Display the day of the week in English
    birth_day_of_week = datetime.strptime(birthdate, '%Y%m%d').strftime('%A')
    st.write(f"Birth day of the week: {birth_day_of_week.capitalize()}")

# Calculate sums of PI digits
sum_20_digits = sum_pi_digits(20)
sum_144_digits = sum_pi_digits(144)

st.write(f"The sum of the first 20 digits of PI is: {sum_20_digits}")
st.write(f"The sum of the first 144 digits of PI is: {sum_144_digits}")

# Remarks on the calculated sums
st.write("What do you notice?")
st.write("The sum of the first 20 digits is much smaller than that of the first 144 digits, which is expected due to the much higher number of terms added.")

# Embed a video
st.write("Here's a video explaining that the sum of all natural numbers equals -1/12:")
st.video("https://www.youtube.com/watch?v=w-I6XTVZXww")
