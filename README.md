# 🧠 Feedback Sentiment Analyzer

An end-to-end **Sentiment Analysis & Feedback Insights** project built during my internship at **Ajinca Creation Pvt. Ltd.**  
This tool helps identify what users are *feeling* from their feedback — positive, neutral, or negative — and provides visual insights for better decision-making.

![Language](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square) ![Status](https://img.shields.io/badge/Internship%20Project-Complete-brightgreen?style=flat-square)

---

## 📌 Project Summary

> **Goal:** Analyze user feedback sentiment from training platforms or surveys and visualize trends to help improve service delivery.

### ✨ Core Features:
- Cleaned real-world-like feedback data
- Sentiment classification using TextBlob & rule-based logic
- Visual charts: Pie Chart (Sentiment split) & Bar Chart (Rating vs Sentiment)
- Business-level summary report inside `/Report`

---

## 📁 Project Structure

FeedbackSentimentAnalyzer/ <br>
├── Data/ # FeedbackSample.csv (raw input data) <br>
├── SRC/ # main.py (core logic, sentiment code, plots) <br>
├── Report/ # Visual charts + text summary <br>
├── README.md # You’re here! <br>
├── requirements.txt # Python libraries <br>
└── .gitignore # Ignored files <br>

---

## 📊 Tech Stack

- Python (Pandas, NumPy, scikit-learn, Matplotlib)
- VS Code
- NLP (Sentiment Classification)

## 📊 Visual Samples

| Sentiment Split Pie Chart | Sentiment Bar Chart | Rating vs Sentiment Bar Chart |
|---------------------------|---------------------|-------------------------------|
| ![Pie Chart](Report/sentiment_distribution_pie.png) | ![Bar Chart](Report/sentiment_distribution_bar.png) | ![Bar Chart](Report/average_rating_per_sentiment.png)

## 📂 Real-World Use Case

Imagine an LXP (Learning Experience Platform) where feedback is collected. This tool could:
- Quickly classify feedback sentiment
- Help product teams identify modules with low sentiment
- Provide monthly sentiment performance metrics
- Build internal dashboards for stakeholders

## 📜 License

MIT License

---

Made with ❤️ during my internship at [Ajinkya Creatiion Pvt. Ltd.]
