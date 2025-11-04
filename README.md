# 💬 Review Sentiment Classifier -
## Harshal Meshram 22070521171 Sec : B

A simple **Streamlit** web app that classifies user reviews as **Positive 😊** or **Negative ☹️** using pre-trained **Naive Bayes** and **Logistic Regression** models.

🔗 **Live App:** [Click here to try it out!](https://machinelearning-nmurdphbnqjliz6fk2zvc6.streamlit.app/)

---
## 🧩 Title & Short Description

### **Problem Statement**
In today’s digital world, thousands of product and movie reviews are shared online daily. Manually analyzing them to understand customer sentiment is time-consuming and inefficient.  

This project focuses on building an **automated sentiment analysis model** that classifies reviews as positive or negative based on their textual content.  

### **Why It’s Important**
Sentiment analysis plays a vital role in:
- **Understanding customer feedback** for product improvement  
- **Brand reputation monitoring**  
- **Market analysis and decision-making**

### **Overview of Results**
Our trained models — **Naive Bayes** and **Logistic Regression** — achieve high accuracy and produce confidence scores for predictions. The Streamlit app provides a clean and interactive interface where users can input any text and instantly view the sentiment prediction with visualization.

---

## 📊 Dataset Source

The dataset used is based on publicly available **IMDb Movie Reviews Dataset** and similar labeled sentiment datasets.  
- **Size:** ~50,000 reviews  
- **Classes:** Positive (1) and Negative (0)

### **Preprocessing Steps**
- Removed HTML tags and special symbols  
- Converted all text to lowercase  
- Removed stopwords  
- Tokenized and vectorized using **TF-IDF Vectorizer**  
- Split into training and testing sets (80/20)

---

## ⚙️ Methods

### **Approach**
We trained two classic supervised models:
1. **Naive Bayes (MultinomialNB)** — works well for text classification with word frequency data  
2. **Logistic Regression** — provides better interpretability and confidence scores  
Both models were trained on TF-IDF vectorized text features.

 Model               | Accuracy | Precision | Recall | F1-score |
|----------------------|-----------|------------|---------|-----------|
| Naive Bayes          | 0.91734   | 0.924178   | 0.90928 | 0.916668  |
| Logistic Regression  | 0.93492   | 0.928712   | 0.94216 | 0.935388  |

➡️ The **Logistic Regression** model slightly outperformed Naive Bayes in all metrics and is therefore set as the **default model** in the deployed Streamlit app.

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
## 🏁 Conclusion

- Both **Naive Bayes** and **Logistic Regression** effectively classify text-based reviews.  
- **Logistic Regression** performs slightly better in accuracy and interpretability.  
- The **Streamlit interface** provides a simple, interactive way for users to test the models.  

### **Key Takeaways**
- Text preprocessing and vectorization greatly influence sentiment classification performance.  
- Classic ML models can achieve strong performance without deep learning for smaller datasets.  

---

## 📚 References

1. Maas, A.L., et al. *"Learning Word Vectors for Sentiment Analysis."* Proceedings of ACL (2011).  
2. [Scikit-learn Documentation](https://scikit-learn.org/)  
3. [Streamlit Documentation](https://docs.streamlit.io/)  
4. [IMDb Review Dataset (Kaggle)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

---

## 👩‍💻 Author
Harshal Meshram
Sec B
22070521171

⭐ *Don’t forget to star this repo if you found it helpful!*
