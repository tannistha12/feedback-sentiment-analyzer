import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import os
from streamlit_lottie import st_lottie
import requests
import time

st.set_page_config(page_title="Feedback Sentiment Analyzer", layout="centered")

st.markdown("<h1 style='text-align: center;'>Feedback Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Analyze the mood behind user feedback in real time.</h4>", unsafe_allow_html=True)

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = os.path.join(os.path.dirname(__file__), '..', 'static', 'style.css')
if os.path.exists(css_file):
    load_css(css_file)

# Load Lottie animation from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_feedback = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_puciaact.json")
st_lottie(lottie_feedback, speed=1, reverse=False, loop=True, height=250, quality="high", key="feedback")

# Initialize session state
if "counts" not in st.session_state:
    st.session_state.counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

# --- Main Content Container ---
main_container = st.container()

# File upload section
st.subheader("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file with feedback data", type=["csv"])

# Prediction function
def predict_sentiment(text):
    if not text.strip():
        return None, None
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "Positive", polarity
    elif polarity < -0.1:
        return "Negative", polarity
    else:
        return "Neutral", polarity

if uploaded_file is not None:
    st.markdown("""
        <style>
        #main-content { filter: blur(4px); }
        #overlay-message {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 40px;
            font-weight: bold;
            color: #222;
            background: rgba(255,255,255,0.95);
            padding: 40px 60px;
            border-radius: 20px;
            z-index: 9999;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            text-align: center;
        }
        </style>
        <div id="overlay-message">
            Please wait...<br>
            <img src="https://assets10.lottiefiles.com/packages/lf20_puciaact.json" width="120"/>
        </div>
        """, unsafe_allow_html=True)

    with st.spinner("Analyzing file..."):
        df = None
        try:
            df = pd.read_csv(uploaded_file)
            if 'Feedback' not in df.columns:
                st.error("The uploaded CSV must contain a 'Feedback' column.")
            else:
                df["Sentiment Label"] = df["Feedback"].astype(str).apply(lambda x: predict_sentiment(x)[0])
                sentiment_counts = df["Sentiment Label"].value_counts().reindex(["Positive", "Neutral", "Negative"], fill_value=0)
                st.session_state.counts = sentiment_counts.to_dict()
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")

    time.sleep(2)  # Simulate processing time

    st.markdown("""
        <style>
        #main-content { filter: none !important; }
        #overlay-message { display: none !important; }
        </style>
        """, unsafe_allow_html=True)

    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    

    if df is not None:
        fig, ax = plt.subplots()
        colors = ['green', 'grey', 'red']
        ax.pie(sentiment_counts.values, labels=sentiment_counts.index, colors=colors, startangle=90, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)

# --- Main Content (wrap in a div for blur effect) ---
with main_container:
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    # ...rest of your dashboard code (summary, stats, etc.)...
    st.markdown('</div>', unsafe_allow_html=True)

# Dashboard Summary
st.markdown("Sentiment Summary")
col1, col2, col3 = st.columns(3)

Positive = st.session_state.counts.get("Positive", 0)
Negative = st.session_state.counts.get("Negative", 0)
Neutral = st.session_state.counts.get("Neutral", 0)

with col1:
    st.markdown(
        f"""
        <div style='background-color:#d4edda;padding:20px;border-radius:10px;text-align:center;box-shadow:2px 2px 10px rgba(0,0,0,0.1);'>
            <h3 style='color:#155724;'>Positive</h3>
            <p style='font-size:30px;font-weight:bold;color:Black;'>{Positive}</p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style='background-color:#fff3cd;padding:20px;border-radius:10px;text-align:center;box-shadow:2px 2px 10px rgba(0,0,0,0.1);'>
            <h3 style='color:#856404;'>Neutral</h3>
            <p style='font-size:30px;font-weight:bold;color:black;'>{Neutral}</p>
        </div>
        """, unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style='background-color:#f8d7da;padding:20px;border-radius:10px;text-align:center;box-shadow:2px 2px 10px rgba(0,0,0,0.1);'>
            <h3 style='color:#721c24;'>Negative</h3>
            <p style='font-size:30px;font-weight:bold;color:Black;'>{Negative}</p>
        </div>
        """, unsafe_allow_html=True
    )

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 20px;'> 
        <p style='color: grey;'>Created by Tan</p>
        <p style='color: grey;'>Feedback Sentiment Analyzer © 2023</p>
    </div>
    """, unsafe_allow_html=True)
