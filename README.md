# 💬 Review Sentiment Classifier - Harshal Meshram 22070521171 Sec : B

A simple **Streamlit** web app that classifies user reviews as **Positive 😊** or **Negative ☹️** using pre-trained **Naive Bayes** and **Logistic Regression** models.

---

## 🚀 Features

- Choose between **Naive Bayes** or **Logistic Regression**
- Enter any review or comment
- Get **sentiment prediction** with a confidence score
- View a **pie chart visualization** of model confidence
- Built using **Streamlit**, **scikit-learn**, and **Joblib**

---

## 🧠 Tech Stack

| Category | Tools |
|-----------|--------|
| **Backend/Core** | Python |
| **Web App** | Streamlit |
| **Machine Learning** | scikit-learn |
| **Data Handling** | NumPy |
| **Visualization** | Matplotlib |
| **Model Persistence** | Joblib |

---

## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/review-sentiment-classifier.git
   cd review-sentiment-classifier


## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/review-sentiment-classifier.git
   cd review-sentiment-classifier
   
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure model files exist:
Make sure you have the following trained model files in the same directory as app.py:

```bash
naive_bayes_model.pkl
logistic_regression_model.pkl
vectorizer.pkl
```
4. Run the app:

```bash
streamlit run app.py
```

## 🧾 Example Usage

**Input:**
> The movie was absolutely fantastic!

**Output:**
> 😊 Positive  
> Confidence: 0.94  

(Along with a dynamic pie chart showing model confidence.)

---

## 🗂️ Project Structure

```bash
📁 review-sentiment-classifier/
│
├── app.py
├── requirements.txt
├── README.md
├── naive_bayes_model.pkl
├── logistic_regression_model.pkl
└── vectorizer.pkl
```
