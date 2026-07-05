import streamlit as st
import pydeck as pdk
import pandas as pd
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Anjali & Adarsh's Wedding", page_icon="💍", layout="centered")

# --- CUSTOM CSS FOR INDIAN WEDDING THEME ---
# Theme colors: Maroon background, Gold text, elegant fonts
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

    /* Overall Background and Text */
    .stApp {
        background-color: #5b0e2d; /* Deep Maroon */
        color: #f9e596; /* Pale Gold */
        font-family: 'Playfair Display', serif;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #f4c430 !important; /* Rich Gold */
        text-align: center;
        font-family: 'Great Vibes', cursive;
    }
    
    /* Itinerary Cards */
    .itinerary-card {
        background-color: #7b1836;
        border: 2px solid #f4c430;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        text-align: center;
    }
    
    .itinerary-date {
        font-size: 1.2rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .event-item {
        margin-bottom: 5px;
        font-size: 1.1rem;
    }
    
    /* Hero Video Container */
    .hero-container {
        position: relative;
        text-align: center;
        color: white;
        height: 60vh;
        width: 100%;
        overflow: hidden;
        border-bottom: 5px solid #f4c430;
        border-radius: 10px;
        margin-bottom: 40px;
    }
    
    .hero-video {
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.6;
    }
    
    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-family: 'Great Vibes', cursive;
        font-size: 5rem;
        color: #f4c430;
        text-shadow: 2px 2px 8px #000000;
        width: 100%;
    }
    .hero-subtext {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# --- BACKGROUND MUSIC ---
# Note: Most modern browsers require the user to interact with the page before audio autoplays.
def add_bg_music(audio_file_path):
    try:
        with open(audio_file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Please add 'wedding_music.mp3' to the 'assets' folder to enable background music.")

add_bg_music("assets/wedding_music.mp3")

# --- HERO SECTION WITH BACKGROUND VIDEO ---
# You can replace the src with a local base64 video similar to the audio if needed, 
# but for large videos, referencing an external URL or putting it in a public folder is best.
st.markdown("""
<div class="hero-container">
    <video class="hero-video" autoplay loop muted playsinline>
        <source src="https://assets.mixkit.co/videos/preview/mixkit-sparkles-of-light-on-a-dark-background-490-large.mp4" type="video/mp4">
    </video>
    <div class="hero-text">
        Anjali & Adarsh
        <div class="hero-subtext">Are getting married! <br> Scroll down to join our celebration</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- ITINERARY SECTION ---
st.markdown("<h1>Wedding Itinerary</h1>", unsafe_allow_html=True)

# Day 1
st.markdown("""
<div class="itinerary-card">
    <h2>Day 1</h2>
    <div class="itinerary-date">December 2, 2026</div>
    <div class="event-item">🏨 <b>12:00 PM:</b> Check-in at Hotel Amardeep</div>
    <div class="event-item">🍽️ <b>1:00 PM - 3:00 PM:</b> Lunch</div>
    <div class="event-item">🌿 <b>5:00 PM onwards:</b> Mehendi Ceremony followed by High Tea</div>
    <div class="event-item">🌙 <b>8:00 PM onwards:</b> Dinner</div>
</div>
""", unsafe_allow_html=True)

# Day 2
st.markdown("""
<div class="itinerary-card">
    <h2>Day 2</h2>
    <div class="itinerary-date">December 3, 2026</div>
    <p style="color: #f4c430; font-style: italic;">Morning - Afternoon</p>
    <div class="event-item">☕ <b>7:00 AM - 10:00 AM:</b> Breakfast</div>
    <div class="event-item">🌺 <b>10:00 AM - 11:00 AM:</b> Anjali’s Maku Ceremony</div>
    <div class="event-item">🟡 <b>12:00 PM onwards:</b> Haldi Carnival</div>
    <div class="event-item">🍽️ <b>1:00 PM - 3:00 PM:</b> Lunch</div>
    <br>
    <p style="color: #f4c430; font-style: italic;">Evening</p>
    <div class="event-item">💍 <b>Evening:</b> Engagement & Sangeet Ceremony followed by Dinner</div>
</div>
""", unsafe_allow_html=True)

# Day 3
st.markdown("""
<div class="itinerary-card">
    <h2>Day 3</h2>
    <div class="itinerary-date">December 4, 2026</div>
    <div class="event-item">☕ <b>7:00 AM - 10:00 AM:</b> Breakfast</div>
    <div class="event-item">🍽️ <b>1:00 PM - 3:00 PM:</b> Lunch</div>
    <div class="event-item">🥁 <b>8:30 PM:</b> Baraat Entry + Dwar Pooja</div>
    <div class="event-item">🌸 <b>9:00 PM - 9:30 PM:</b> Jaimaal</div>
    <div class="event-item">🍽️ <b>9:00 PM onwards:</b> Dinner</div>
    <div class="event-item">🔥 <b>11:00 PM onwards:</b> Wedding Rituals</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- MAP & FLIGHT ANIMATION ---
st.markdown("<h1>Journey to Our Wedding</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Mumbai to Hotel Amardeep, Haldwani</p>", unsafe_allow_html=True)

# Coordinates
mumbai_lon, mumbai_lat = 72.8777, 19.0760
haldwani_lon, haldwani_lat = 79.5130, 29.2183

# Data for the flight arc
flight_data = pd.DataFrame({
    "start_lon": [mumbai_lon],
    "start_lat": [mumbai_lat],
    "end_lon": [haldwani_lon],
    "end_lat": [haldwani_lat],
})

# PyDeck map configuration for the "Slide/Flight Transition"
arc_layer = pdk.Layer(
    "ArcLayer",
    data=flight_data,
    get_source_position=["start_lon", "start_lat"],
    get_target_position=["end_lon", "end_lat"],
    get_source_color=[244, 196, 48, 160], # Gold
    get_target_color=[244, 196, 48, 255], # Solid Gold
    get_width=5,
    pickable=True,
)

scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=pd.DataFrame({
        "lon": [mumbai_lon, haldwani_lon],
        "lat": [mumbai_lat, haldwani_lat],
        "name": ["Mumbai", "Haldwani"]
    }),
    get_position=["lon", "lat"],
    get_color=[255, 255, 255, 255],
    get_radius=20000,
)

view_state = pdk.ViewState(
    latitude=(mumbai_lat + haldwani_lat) / 2,
    longitude=(mumbai_lon + haldwani_lon) / 2,
    zoom=4.5,
    pitch=45, # Gives the 3D flying effect
)

st.pydeck_chart(pdk.Deck(
    layers=[arc_layer, scatter_layer],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/dark-v10",
    tooltip={"text": "Flight from Mumbai to Haldwani"}
))

# Exact Location Embedded Google Map
st.markdown("<br><h3 style='text-align: center;'>Venue Location</h3>", unsafe_allow_html=True)
st.markdown("""
<div style="display: flex; justify-content: center;">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1m3!1d111244.75704940502!2d79.44474773822187!3d29.219808600000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39a09ad205272a85%3A0xc66c1b34c0db46d2!2sHaldwani%2C%20Uttarakhand!5e0!3m2!1sen!2sin!4v1714488000000!5m2!1sen!2sin" width="100%" height="400" style="border: 2px solid #f4c430; border-radius: 10px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
<p style='text-align: center; margin-top: 10px;'><b>Hotel Amardeep, Haldwani, Uttarakhand</b></p>
""", unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align: center; font-family: \"Great Vibes\", cursive; font-size: 2rem;'>We can't wait to celebrate with you!</p>", unsafe_allow_html=True)