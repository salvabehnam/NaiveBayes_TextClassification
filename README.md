# 📝 Naive Bayes Text Classification

This project implements a **Naive Bayes classifier** to categorize text data into predefined labels. The classifier is trained on a dataset of text documents, enabling it to predict the label of new, unseen text inputs.

## 📌 Features

- **Data Collection**: Utilizes a web crawler to gather text data from specified sources.
- **Data Preprocessing**: Cleans and prepares raw text data for model training.
- **Model Training**: Implements a Naive Bayes algorithm to train the classifier.
- **Prediction**: Classifies new text inputs based on the trained model.

## 📂 Project Structure

    NaiveBayes_TextClassification/
    ├── README.md
    ├── WebCrawler/
    │   ├── crawler.py          # Script for web scraping
    ├── data/
    │   ├── raw_data.txt        # Collected raw text data
    │   ├── processed_data.csv  # Preprocessed data ready for modeling
    ├── models/
    │   ├── naive_bayes_model.pkl  # Trained Naive Bayes model
    ├── notebooks/
    │   ├── preprocessing.ipynb  # Jupyter Notebook for data preprocessing
    │   ├── training.ipynb       # Jupyter Notebook for model training and evaluation
    └── requirements.txt        # List of required Python packages

## 🚀 Installation & Usage

1. **Clone the Repository**

       git clone https://github.com/salvabehnam/NaiveBayes_TextClassification.git
       cd NaiveBayes_TextClassification

2. **Install Dependencies**

   Ensure you have Python 3.x installed. Install the required packages using:

       pip install -r requirements.txt

3. **Collect Data**

   Use the web crawler to collect training data:

       python WebCrawler/crawler.py

   *Note: Modify the `crawler.py` script to target your desired websites.*
   
   *P.S. The training data was crawled from www.mstajbakhsh.ir.*

5. **Preprocess Data**

   Process the raw data to prepare it for modeling. You can use the provided Jupyter Notebook:

       jupyter notebook notebooks/preprocessing.ipynb

6. **Train the Model**

   Train the Naive Bayes classifier using the processed data:

       jupyter notebook notebooks/training.ipynb

7. **Make Predictions**

   After training, use the model to classify new text data. Implement your prediction script or expand the existing notebooks as needed.

## ✨ Technologies Used

- **Python**: Core programming language.
- **scikit-learn**: Machine learning library for implementing the Naive Bayes algorithm.
- **newspaper3k**: Library for web scraping and article extraction.
- **Pandas**: Data manipulation and analysis.
- **Jupyter Notebook**: Interactive environment for developing and running code.



