import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

st.set_page_config(page_title="Feedback Sentiment Analyzer", layout="centered")

st.title("Feedback Sentiment Analyzer")
st.write("Analyze the mood behind user feedback in real time.")

# Input field
feedback = st.text_area("Enter your feedback here:")

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

# Output
if st.button("Analyze"):
    sentiment, score = predict_sentiment(feedback)
    if sentiment:
        st.success(f"Sentiment: **{sentiment}** ({score:.2f})")

        # Pie chart
        fig, ax = plt.subplots()
        ax.pie([abs(score), 1 - abs(score)], labels=[sentiment, "Others"],
               colors=['green', 'grey'], startangle=90, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.warning("Please enter some text.")
