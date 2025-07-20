import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the analyzed feedback data
csv_path = os.path.join("..", "Data", "Analyzed_Feedback.csv")
df = pd.read_csv(csv_path)

# Sentiment Distribution Plot
def plot_sentiment_distribution(df):
    plt.figure(figsize=(6,4))
    sns.countplot(x='Sentiment', data=df, palette='Set2')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig("sentiment_distribution_bar.png")
    plt.close()

# Sentiment Pie Chart
def plot_sentiment_pie(df):
    sentiment_counts = df["Sentiment"].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set2'))
    plt.title('Sentiment Distribution')
    plt.savefig("sentiment_distribution_pie.png")
    plt.close()


def plot_average_rating_per_sentiment(df):
    plt.figure(figsize=(6,4))
    sns.barplot(x='Sentiment', y='Rating', data=df, palette='Set1')
    plt.title('Average Rating per Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Average Rating')
    plt.tight_layout()
    plt.savefig("average_rating_per_sentiment.png")
    plt.close()


# Run the plotting functions
plot_sentiment_distribution(df)
plot_sentiment_pie(df)
plot_average_rating_per_sentiment(df)

print("Report generated successfully and saved as PNG files in the report folder!")
