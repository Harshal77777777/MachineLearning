# MachineLearning
💬 Review Sentiment ClassifierA simple  Streamlit web app that classifies user reviews as Positive 😊 or Negative ☹️ using pre-trained Naive Bayes and Logistic Regression models.🚀 FeaturesChoose between Naive Bayes or Logistic RegressionEnter any review or commentGet sentiment prediction with confidence scoreView pie chart visualization of model confidenceBuilt with ❤️ using Streamlit, scikit-learn, and Joblib🧠 Tech StackCategoryToolsBackend/CorePythonWeb AppStreamlitMachine Learningscikit-learnData HandlingNumPyVisualizationMatplotlibModel PersistenceJoblib📦 InstallationClone this repository:git clone [https://github.com/your-username/review-sentiment-classifier.git](https://github.com/your-username/review-sentiment-classifier.git)
cd review-sentiment-classifier
Install dependencies:pip install -r requirements.txt
Ensure Model Files Exist:Make sure you have the following trained model files:naive_bayes_model.pkllogistic_regression_model.pklvectorizer.pklPlace them in the same directory as app.py.Run the app:streamlit run app.py
🧾 Example UsageInput:The movie was absolutely fantastic!Output:😊 Positive
Confidence: 0.94
(Along with a dynamic pie chart showing model confidence)🗂️ Project Structure📁 review-sentiment-classifier/
│
├── app.py
├── requirements.txt
├── README.md
├── naive_bayes_model.pkl
├── logistic_regression_model.pkl
└── vectorizer.pkl
🖥️ DeploymentYou can deploy this app easily on platforms like:Streamlit CloudHugging Face Spaces🧑‍💻 AuthorYour Name💼 LinkedIn: [Your LinkedIn Profile URL]🐙 GitHub: [Your GitHub Profile URL]⭐ Don’t forget to star this repo if you like it!
