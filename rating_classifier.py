# fixed_review_sentiment_app.py

import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Review Sentiment Classifier", layout="centered")

st.title("💬 Review Sentiment Classifier")
st.write("This app classifies reviews as **Positive** or **Negative** using trained models and a text vectorizer.")

# --- Model selection ---
model_choice = st.radio(
    "Choose model to use:",
    ("Naive Bayes", "Logistic Regression")
)

MODEL_PATHS = {
    "Naive Bayes": "naive_bayes_model.pkl",
    "Logistic Regression": "logistic_regression_model.pkl"
}

VECTORIZER_PATH = "vectorizer.pkl"  # Make sure to have this file saved

# --- Load model and vectorizer ---
try:
    model = joblib.load(MODEL_PATHS[model_choice])
    vectorizer = joblib.load(VECTORIZER_PATH)
    st.success(f"✅ {model_choice} model and vectorizer loaded successfully.")
except Exception as e:
    st.error(f"❌ Failed to load model/vectorizer: {e}")
    st.stop()

# --- User input ---
user_input = st.text_area("📝 Type your review or comment:", placeholder="e.g. The movie was amazing!")

if st.button("Classify Review"):
    if user_input.strip() == "":
        st.warning("Please enter a review before classifying.")
    else:
        try:
            # Transform text before prediction
            X_vec = vectorizer.transform([user_input])

            # Predict sentiment
            prediction = model.predict(X_vec)[0]

            # Confidence
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(X_vec)[0]
                confidence = np.max(proba)
            else:
                confidence = None

            sentiment = "😊 Positive" if prediction == 1 or str(prediction).lower() == "positive" else "☹️ Negative"
            color = "green" if "Positive" in sentiment else "red"

            st.markdown(f"### Prediction: <span style='color:{color}'>{sentiment}</span>", unsafe_allow_html=True)
            if confidence is not None:
                st.write(f"**Confidence:** {confidence:.2f}")

            # Visualization
            st.subheader("📊 Sentiment Confidence Visualization")
            fig, ax = plt.subplots()
            if confidence is not None:
                ax.pie(
                    [confidence, 1 - confidence],
                    labels=[sentiment, "Opposite sentiment"],
                    autopct="%1.1f%%",
                    startangle=90,
                    colors=["#2ecc71" if "Positive" in sentiment else "#e74c3c", "#bdc3c7"]
                )
                ax.axis("equal")
                st.pyplot(fig)
            else:
                st.info("Model does not provide probability scores, so only label is shown.")

        except Exception as e:
            st.error(f"Error making prediction: {e}")

st.caption("Made with ❤️ using Streamlit, Naive Bayes & Logistic Regression models.")
