# Importing Streamlit
import streamlit as st 

# Page Configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠")

# Title
st.title("💪 Growth Mindset Challenge: Web App with Streamlit 🚀")

# Introduction
st.header("🌱 Welcome to Your Journey of Growth!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. "
         "This AI-powered app helps you build a growth mindset through reflection, challenges, and achievements!")

# Quote Section
st.header("🌟 Today's Inspirational Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill')

# Growth Challenge
st.header("🎯 What’s Your Growth Challenge Today?")
user_input = st.text_input("Describe a Challenge you're Facing:")

# Condition for Challenge Input
if user_input:
    st.success(f"You're Facing: {user_input}. Keep pushing forward towards your goal! 💪")
else:
    st.warning("Tell us about your challenge to get started! Every challenge is a step toward growth. 🌱")

# Reflecting on Learning
st.header("🧠 Take a Moment to Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection} 🌟")
else:
    st.info("Reflection on past experiences helps you grow! Share your thoughts to deepen your learning. 📖")

# Achievements Section
st.header("🎉 Celebrate Your Achievements! 🏆")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement} 🎊")
else:
    st.info("Big or small, every achievement counts! Share one now and celebrate your progress. 🎯")

# Footer
st.write("---")  
st.write("🌟 Keep believing in yourself. Growth is a journey, not a destination! 🚀")     
st.write("**Created by Muhammad Asad**")  


