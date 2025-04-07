import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="BiophiliaConnect",
    page_icon="🌿",
    layout="wide"
)

# App title
st.title("🌿 BiophiliaConnect")
st.subheader("Your companion for connecting with nature")

# Simple user authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    
if 'username' not in st.session_state:
    st.session_state.username = ""

# Login section
if not st.session_state.logged_in:
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username and password:  # Very basic validation
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()  # Changed from experimental_rerun
else:
    # Main app content for logged-in users
    st.header(f"Welcome, {st.session_state.username}!")
    
    # Navigation sidebar
    page = st.sidebar.radio("Navigate", ["Home", "Find Trails", "My Profile"])
    
    if page == "Home":
        # Display biophilia score
        score = random.randint(10, 40)
        st.subheader("Your Biophilia Score")
        st.markdown(f"<h1 style='text-align: center; color: #43a047;'>{score}/50</h1>", unsafe_allow_html=True)
        
        # Biophilia elements
        st.subheader("Biophilia Elements")
        elements = [
            {"name": "Time spent in nature", "score": random.randint(0, 10)},
            {"name": "Diversity of experiences", "score": random.randint(0, 10)},
            {"name": "Connection to ecosystem", "score": random.randint(0, 10)},
            {"name": "Knowledge of flora/fauna", "score": random.randint(0, 10)},
            {"name": "Sensory engagement", "score": random.randint(0, 10)}
        ]
        
        for element in elements:
            st.text(f"{element['name']}: {element['score']}/10")
            st.progress(element['score']/10)
    
    elif page == "Find Trails":
        st.subheader("Find Nature Trails Near You")
        location = st.text_input("Enter your location")
        
        if st.button("Search"):
            st.info("This is a basic version. Trail search will be added in future updates.")
            
            # Show sample trail
            st.subheader("Sample Nearby Trail")
            st.write("Forest Loop Trail - 1.2 miles away")
            st.write("Difficulty: Easy")
            st.write("A peaceful trail through a forested area with diverse plant life.")
    
    elif page == "My Profile":
        st.subheader("My Profile")
        st.write(f"Username: {st.session_state.username}")
        st.write("Member since: April 2025")
        
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()  # Changed from experimental_rerun

# Footer
st.sidebar.markdown("---")
st.sidebar.info("BiophiliaConnect © 2025")
