import pandas as pd
import random
from datetime import datetime, timedelta
from geopy.distance import geodesic

def calculate_distance(user_lat, user_lon, trail_lat, trail_lon):
    """Calculate the distance between user location and a trail in miles"""
    user_location = (user_lat, user_lon)
    trail_location = (trail_lat, trail_lon)
    
    # Calculate distance in kilometers and convert to miles
    distance_km = geodesic(user_location, trail_location).kilometers
    distance_miles = distance_km * 0.621371
    
    return round(distance_miles, 1)

def load_trails_data():
    """Load trail data from CSV file"""
    try:
        return pd.read_csv("data/trails.csv")
    except FileNotFoundError:
        # Return empty DataFrame with expected columns if file not found
        return pd.DataFrame(columns=[
            'id', 'name', 'latitude', 'longitude', 'difficulty', 
            'description', 'biophilia_element'
        ])

def load_events_data():
    """Load events data from CSV file"""
    try:
        return pd.read_csv("data/events.csv")
    except FileNotFoundError:
        # Return empty DataFrame with expected columns if file not found
        return pd.DataFrame(columns=[
            'id', 'name', 'organizer', 'location', 'date', 'time',
            'description', 'biophilia_element'
        ])

def get_nearby_trails(user_lat, user_lon, max_distance=25):
    """Get trails within specified distance of user location"""
    df = load_trails_data()
    
    if df.empty:
        return []
        
    # Calculate distance for each trail
    nearby_trails = []
    
    for _, row in df.iterrows():
        distance = calculate_distance(user_lat, user_lon, row['latitude'], row['longitude'])
        
        if distance <= max_distance:
            nearby_trails.append({
                'id': row['id'],
                'name': row['name'],
                'distance': f"{distance} miles away",
                'difficulty': row['difficulty'],
                'description': row['description'],
                'biophilia_boost': f"+{random.randint(2, 5)} {row['biophilia_element']}",
                'events': get_trail_events(row['id'])
            })
    
    return nearby_trails

def get_trail_events(trail_id, limit=3):
    """Get events associated with a specific trail"""
    # In a real app, you would filter events by trail ID
    # Here we'll just return random events as an example
    events = []
    
    # Generate 0-2 random events
    num_events = random.randint(0, 2)
    
    for i in range(num_events):
        # Generate a random date in the next 14 days
        event_date = datetime.now() + timedelta(days=random.randint(1, 14))
        date_str = event_date.strftime("%b %d, %Y")
        
        # Generate a random time
        hour = random.randint(7, 18)
        minute = random.choice([0, 15, 30, 45])
        time_str = f"{hour}:{minute:02d} {'AM' if hour < 12 else 'PM'}"
        
        events.append({
            'id': f"event_{i}_{trail_id}",
            'name': random.choice([
                "Guided Nature Walk", 
                "Bird Watching Tour", 
                "Forest Bathing Workshop",
                "Wildlife Photography",
                "Native Plant Identification",
                "Sunset Meditation Hike"
            ]),
            'date': date_str,
            'time': time_str
        })
    
    return events

def calculate_biophilia_score(user_data):
    """Calculate biophilia score based on user activity data"""
    # In a real app, this would use real user data
    # For demo purposes, we'll generate random scores
    
    elements = [
        {"name": "Time spent in nature", "score": random.randint(0, 10), "max": 10},
        {"name": "Diversity of experiences", "score": random.randint(0, 10), "max": 10},
        {"name": "Connection to ecosystem", "score": random.randint(0, 10), "max": 10}, 
        {"name": "Knowledge of flora/fauna", "score": random.randint(0, 10), "max": 10},
        {"name": "Sensory engagement", "score": random.randint(0, 10), "max": 10}
    ]
    
    total_score = sum(element["score"] for element in elements)
    
    return {
        "total": total_score,
        "elements": elements
    }
