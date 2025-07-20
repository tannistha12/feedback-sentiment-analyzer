# SRC/sentiment_analyzer.py

import pandas as pd
from textblob import TextBlob
import os

# Load the CSV
csv_path = os.path.join("..", "Data", "feedback_sample_v2.csv")
df = pd.read_csv(csv_path)

# Function to analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['Sentiment'] = df['Feedback'].apply(get_sentiment)

# Save updated file
output_path = os.path.join("..", "Data", "Analyzed_Feedback.csv")
df.to_csv(output_path, index=False)

print("Sentiment analysis complete. Output saved to Data/Analyzed_Feedback.csv")
