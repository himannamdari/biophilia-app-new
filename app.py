import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
import random

# Page configuration
st.set_page_config(
    page_title="BiophiliaConnect",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #43a047;
    text-align: center;
}
.sub-header {
    font-size: 1.5rem;
    color: #66bb6a;
}
.info-box {
    background-color: #f1f8e9;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #43a047;
}
.score-box {
    background-color: #43a047;
    color: white;
    padding: 20px;
    border-radius: 50%;
    width: 150px;
    height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
}
.score {
    font-size: 3rem;
    font-weight: bold;
}
.score-label {
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# App functionality
def main():
    # Sidebar
    st.sidebar.title("🌿 BiophiliaConnect")
    
    # User authentication (simplified)
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        
    if not st.session_state.logged_in:
        show_login_page()
    else:
        # Navigation
        page = st.sidebar.radio("Navigate", ["Home", "Find Trails", "Events", "My Profile"])
        
        if page == "Home":
            show_home_page()
        elif page == "Find Trails":
            show_trails_page()
        elif page == "Events":
            show_events_page()
        elif page == "My Profile":
            show_profile_page()
            
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info("© 2025 BiophiliaConnect")

def show_login_page():
    st.markdown("<h1 class='main-header'>Welcome to BiophiliaConnect</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your companion for connecting with nature and improving your biophilia score</p>", unsafe_allow_html=True)
    
    # Create columns for layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h2 class='sub-header'>Login</h2>", unsafe_allow_html=True)
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        login_btn = st.button("Login")
        register_btn = st.button("Create Account")
        
        if login_btn and username and password:
            # In a real app, this would check against a database
            st.session_state.logged_in = True
            st.session_state.username = username.split('@')[0]
            st.experimental_rerun()
            
        if register_btn:
            st.info("In a real app, this would take you to a registration page.")

def show_home_page():
    st.markdown(f"<h1 class='main-header'>Welcome, {st.session_state.username}!</h1>", unsafe_allow_html=True)
    
    # Display date
    today = datetime.now().strftime("%A, %B %d")
    st.markdown(f"<p style='text-align: center;'>{today}</p>", unsafe_allow_html=True)
    
    # Display biophilia score
    score = random.randint(20, 45)
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown(f"""
        <div class='score-box'>
            <span class='score'>{score}</span>
            <span class='score-label'>/ 50</span>
        </div>
        <p style='text-align: center; margin-top: 10px;'>Your Biophilia Score</p>
        """, unsafe_allow_html=True)
    
    # Biophilia elements
    st.markdown("<h2 class='sub-header'>Biophilia Elements</h2>", unsafe_allow_html=True)
    
    elements = [
        {"name": "Time spent in nature", "score": random.randint(0, 10), "max": 10},
        {"name": "Diversity of experiences", "score": random.randint(0, 10), "max": 10},
        {"name": "Connection to ecosystem", "score": random.randint(0, 10), "max": 10}, 
        {"name": "Knowledge of flora/fauna", "score": random.randint(0, 10), "max": 10},
        {"name": "Sensory engagement", "score": random.randint(0, 10), "max": 10}
    ]
    
    for element in elements:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{element['name']}**")
            progress = element['score'] / element['max']
            st.progress(progress)
        with col2:
            st.markdown(f"**{element['score']}/{element['max']}**")
    
    # Recommendations
    st.markdown("<h2 class='sub-header'>Personalized Recommendations</h2>", unsafe_allow_html=True)
    
    recommendations = [
        "Try forest bathing to improve your sensory engagement",
        "Learn about local bird species to increase ecosystem knowledge",
        "Visit a water feature to diversify your nature experiences",
        "Practice mindfulness in natural settings to deepen your connection"
    ]
    
    for rec in recommendations:
        st.markdown(f"* {rec}")
        
    # Find trails button
    st.markdown("---")
    if st.button("Find Nearby Nature Trails", key="find_trails_btn"):
        st.session_state.page = "Find Trails"
        st.experimental_rerun()

def show_trails_page():
    st.markdown("<h1 class='main-header'>Nearby Nature Experiences</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Discover places to connect with nature</p>", unsafe_allow_html=True)
    
    # Location input
    location = st.text_input("Enter your location", "New York, NY")
    
    if st.button("Search Trails"):
        with st.spinner("Finding trails near you..."):
            # In a real app, this would call an API
            # Mock data for demonstration
            show_mock_trails()

def show_mock_trails():
    trails = [
        {
            "name": "Redwood Forest Trail",
            "distance": f"{round(random.uniform(0.5, 5.0), 1)} miles away",
            "difficulty": "Moderate",
            "description": "A peaceful trail winding through ancient redwood trees.",
            "biophilia_boost": "+3 Sensory engagement",
            "events": [
                {"name": "Forest Bathing Workshop", "date": "Apr 12, 2025", "time": "10:00 AM"},
                {"name": "Mindful Hiking Group", "date": "Apr 15, 2025", "time": "9:00 AM"}
            ]
        },
        {
            "name": "Lakeside Nature Path",
            "distance": f"{round(random.uniform(0.5, 5.0), 1)} miles away",
            "difficulty": "Easy",
            "description": "A gentle path alongside a pristine lake. Great for spotting waterfowl.",
            "biophilia_boost": "+4 Diversity of experiences",
            "events": [
                {"name": "Bird Watching Tour", "date": "Apr 10, 2025", "time": "8:00 AM"}
            ]
        },
        {
            "name": "Mountain Vista Loop",
            "distance": f"{round(random.uniform(0.5, 5.0), 1)} miles away",
            "difficulty": "Challenging",
            "description": "A challenging mountain trail with breathtaking views of the valley.",
            "biophilia_boost": "+5 Time spent in nature",
            "events": [
                {"name": "Sunset Meditation Hike", "date": "Apr 14, 2025", "time": "6:30 PM"},
                {"name": "Native Plant Identification", "date": "Apr 16, 2025", "time": "2:00 PM"}
            ]
        }
    ]
    
    for trail in trails:
        with st.expander(f"{trail['name']} - {trail['distance']}"):
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(f"**{trail['name']}**")
                st.markdown(f"Distance: {trail['distance']} | Difficulty: {trail['difficulty']}")
                st.markdown(trail['description'])
                st.markdown(f"**{trail['biophilia_boost']}**")
            
            with cols[1]:
                # Save location button
                if st.button("Save Location", key=f"save_{trail['name']}"):
                    st.success(f"Added {trail['name']} to your saved locations!")
            
            # Events section
            if trail['events']:
                st.markdown("**Upcoming Events:**")
                for event in trail['events']:
                    event_cols = st.columns([3, 1])
                    with event_cols[0]:
                        st.markdown(f"**{event['name']}**")
                        st.markdown(f"{event['date']} at {event['time']}")
                    with event_cols[1]:
                        if st.button("Add to Calendar", key=f"calendar_{event['name']}"):
                            st.success(f"Added {event['name']} to your calendar!")
            
            st.markdown("---")

def show_events_page():
    st.markdown("<h1 class='main-header'>Nature Events</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Discover events to enhance your connection with nature</p>", unsafe_allow_html=True)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        activity_type = st.selectbox("Activity Type", ["All", "Guided Hikes", "Wildlife Watching", "Meditation", "Education"])
    with col2:
        date_range = st.selectbox("Date Range", ["This Week", "This Month", "Next 3 Months"])
    with col3:
        distance = st.select_slider("Distance", options=["<5 miles", "<10 miles", "<25 miles", "Any"])
    
    # Search button
    if st.button("Search Events"):
        # Mock events data
        show_mock_events()

def show_mock_events():
    events = [
        {
            "name": "Spring Wildlife Walk",
            "organizer": "City Nature Society",
            "location": "Oakwood Park",
            "date": "Apr 15, 2025",
            "time": "9:00 AM - 11:00 AM",
            "description": "Join our expert naturalists for a guided walk focusing on spring wildlife.",
            "biophilia_boost": "+3 Knowledge of flora/fauna"
        },
        {
            "name": "Forest Meditation Retreat",
            "organizer": "Mindful Nature Connection",
            "location": "Pine Grove Forest",
            "date": "Apr 20, 2025",
            "time": "10:00 AM - 12:00 PM",
            "description": "Experience the healing power of forest meditation with certified instructors.",
            "biophilia_boost": "+4 Sensory engagement"
        },
        {
            "name": "Native Plant Workshop",
            "organizer": "Community Gardens",
            "location": "Riverside Botanical Garden",
            "date": "Apr 25, 2025",
            "time": "1:00 PM - 3:00 PM",
            "description": "Learn about native plants and their ecological importance.",
            "biophilia_boost": "+3 Connection to ecosystem"
        }
    ]
    
    for event in events:
        with st.expander(f"{event['name']} - {event['date']}"):
            st.markdown(f"**{event['name']}**")
            st.markdown(f"**Organizer:** {event['organizer']}")
            st.markdown(f"**Location:** {event['location']}")
            st.markdown(f"**Date & Time:** {event['date']}, {event['time']}")
            st.markdown(event['description'])
            st.markdown(f"**Biophilia Boost:** {event['biophilia_boost']}")
            
            cols = st.columns([1, 1])
            with cols[0]:
                if st.button("Register", key=f"register_{event['name']}"):
                    st.success(f"Registered for {event['name']}!")
            with cols[1]:
                if st.button("Add to Calendar", key=f"cal_{event['name']}"):
                    st.success(f"Added {event['name']} to your calendar!")
            
            st.markdown("---")

def show_profile_page():
    st.markdown("<h1 class='main-header'>My Profile</h1>", unsafe_allow_html=True)
    
    # Profile header
    col1, col2 = st.columns([1, 3])
    with col1:
        # Profile image (placeholder)
        st.markdown(f"""
        <div style="background-color: #43a047; color: white; width: 100px; height: 100px; 
               border-radius: 50%; display: flex; align-items: center; 
               justify-content: center; font-size: 2rem;">
            {st.session_state.username[0].upper()}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h2>{st.session_state.username}</h2>", unsafe_allow_html=True)
        st.markdown("Nature enthusiast since April 2025")
    
    # Tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Saved Locations", "Activity History", "Settings"])
    
    with tab1:
        st.subheader("My Saved Locations")
        if 'saved_locations' not in st.session_state:
            st.session_state.saved_locations = []
            
        if not st.session_state.saved_locations:
            st.info("You haven't saved any locations yet.")
        else:
            for loc in st.session_state.saved_locations:
                st.markdown(f"**{loc}**")
                if st.button("Remove", key=f"remove_{loc}"):
                    st.session_state.saved_locations.remove(loc)
                    st.experimental_rerun()
    
    with tab2:
        st.subheader("Recent Activity")
        activities = [
            {"type": "Trail Visit", "location": "Cedar Creek Trail", "date": "Apr 3, 2025"},
            {"type": "Event", "location": "Birdwatching Workshop", "date": "Mar 28, 2025"},
            {"type": "Badge Earned", "name": "Forest Explorer", "date": "Mar 25, 2025"}
        ]
        
        for activity in activities:
            if "type" in activity and activity["type"] == "Badge Earned":
                st.markdown(f"**{activity['date']}:** Earned the **{activity['name']}** badge")
            else:
                st.markdown(f"**{activity['date']}:** {activity['type']} - {activity['location']}")
    
    with tab3:
        st.subheader("Account Settings")
        
        st.checkbox("Receive email notifications")
        st.checkbox("Allow location tracking for proximity alerts")
        st.checkbox("Send me weekly nature activity suggestions")
        
        if st.button("Save Settings"):
            st.success("Settings saved successfully!")
            
        if st.button("Log Out", key="logout_btn"):
            st.session_state.logged_in = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
