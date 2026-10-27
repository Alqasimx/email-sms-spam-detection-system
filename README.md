# Email/SMS Spam Detection System

> A machine-learning system that classifies email and SMS messages as **Spam** or **Ham** through an interactive Streamlit application and a FastAPI backend.

## Overview

**Email/SMS Spam Detection System** is an educational natural-language-processing project developed as part of a cybersecurity and machine-learning graduation project at the **University of Science and Technology**.

The system provides two ways to use the classifier:

- A simple interactive web interface built with **Streamlit**.
- A REST API built with **FastAPI** for integration with other applications.

The training pipeline compares multiple supervised-learning algorithms, evaluates them using classification metrics, selects the best model by F1 score, and saves the trained model and TF-IDF vectorizer for reuse during prediction.

## Problem Statement

Spam messages are common across email and SMS platforms and may contain misleading offers, fraudulent links, unwanted advertising, or social-engineering attempts. Manual review is time-consuming and unreliable at scale.

This project addresses the problem by transforming message text into numerical features and using a supervised machine-learning classifier to estimate whether a message is legitimate (**ham**) or unwanted (**spam**).

## Project Goals

- Build a practical text-classification system for email and SMS messages.
- Apply a consistent preprocessing pipeline during both training and inference.
- Compare Naive Bayes, Logistic Regression, and Linear SVM approaches.
- Select the best model using the F1-score.
- Provide a user-friendly interface for testing messages.
- Expose the classifier through a documented HTTP API.
- Preserve the trained artifacts so users can run predictions without retraining first.

## Main Features

- English text normalization and tokenization.
- Stop-word removal and Porter stemming using NLTK.
- TF-IDF feature extraction with a configurable maximum vocabulary size.
- Comparison of three classification approaches:
  - Multinomial Naive Bayes
  - Logistic Regression
  - Calibrated LinearSVC
- Evaluation using accuracy, precision, recall, F1-score, and a classification report.
- Persisted `model.pkl` and `vectorizer.pkl` artifacts.
- Streamlit interface with a confidence score and visual result state.
- FastAPI endpoints for health checks and predictions.
- Input validation and a maximum input length of 10,000 characters.

## Reported Result

The project documentation reports a best accuracy of approximately **97.9%**, with the LinearSVC-based model selected as the strongest candidate in the tested setup. Exact metrics can vary when the dataset, preprocessing, split, or dependency versions change. Run `train.py` to reproduce the evaluation locally.

## Technology Stack

- **Python 3**
- **pandas** and **NumPy** for data handling
- **NLTK** for tokenization, stop words, and stemming
- **scikit-learn** for TF-IDF, model training, and evaluation
- **Streamlit** for the interactive web UI
- **FastAPI**, **Uvicorn**, and **Pydantic** for the REST API
- **pickle** for storing the trained model and vectorizer
- **pytest** and **httpx** listed for testing and API validation

## Project Structure

```text
.
├── app.py                    # Streamlit user interface
├── api.py                    # FastAPI application
├── predict.py                # Shared inference logic
├── train.py                  # Data loading, training, evaluation, and saving
├── data_preprocessing.py     # Shared NLTK text preprocessing
├── spam.csv                  # SMS Spam Collection dataset used for training
├── model.pkl                 # Persisted trained classifier
├── vectorizer.pkl            # Persisted TF-IDF vectorizer
├── requirements.txt          # Python dependencies
├── setup.sh                  # Dependency and NLTK resource setup
├── Procfile                  # Process command for compatible deployment services
├── nltk.txt                  # NLTK resource reference
└── run-guide-ar.txt          # Arabic operating guide
```

## Installation

Clone the repository and create an isolated Python environment:

```bash
git clone https://github.com/Alqasimx/email-sms-spam-detection-system.git
cd email-sms-spam-detection-system
python3 -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate      # Windows PowerShell
```

Install the dependencies and NLTK resources:

```bash
chmod +x setup.sh
./setup.sh
```

On Windows, the equivalent commands are:

```powershell
python -m pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

## Train the Model

Training reads `spam.csv`, cleans the data, applies the shared preprocessing pipeline, compares the candidate models, and saves the best model and vectorizer:

```bash
python train.py
```

The generated artifacts are:

- `model.pkl`
- `vectorizer.pkl`

The repository already contains trained artifacts, so retraining is optional for basic prediction. Retrain when changing the dataset, preprocessing, or model configuration.

## Run the Streamlit Application

```bash
streamlit run app.py
```

The application opens a local browser page. Enter an email or SMS message and select **Predict**. The interface displays:

- `SPAM` when the classifier detects unwanted content.
- `HAM` when the message appears legitimate.
- A confidence score returned by the trained model.

## Run the FastAPI Backend

Start the API with:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### Health Check

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

### Prediction Request

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Congratulations! You have won a free prize."}'
```

Example response:

```json
{"label":"spam","confidence":0.98}
```

The API also exposes interactive documentation at `/docs` when the server is running.

## Model Pipeline

1. Load the SMS Spam Collection CSV.
2. Keep the label and message columns and remove duplicate rows.
3. Encode `ham` and `spam` labels.
4. Lowercase and tokenize each message.
5. Remove non-alphanumeric tokens and English stop words.
6. Apply Porter stemming.
7. Convert the processed text into TF-IDF vectors.
8. Split the data into stratified training and test sets.
9. Train MultinomialNB, LogisticRegression, and calibrated LinearSVC models.
10. Compare accuracy, precision, recall, and F1-score.
11. Save the best model and vectorizer as pickle artifacts.

## Dataset Note

The included `spam.csv` is based on the SMS Spam Collection format, with `v1` as the label and `v2` as the message text. The training script also accepts a compatible CSV using `target` and `text` columns.

Review the dataset provenance and redistribution terms before using the data in commercial or public products. This repository is intended for educational and research use.

## My Role

I contributed to the project as a member of the graduation-project team and was responsible for the project work documented and submitted under my name, including the machine-learning application workflow, integration of the prediction pipeline with the user-facing application, and preparation of the project documentation. The project was completed collaboratively, and the final result reflects the contributions of the full team.

## Team

- **Alqasem Alahdl — Team Leader**
- Rami Wadee
- Anas Eissa
- Hashem Waheed
- Mohammed Abdurrabah Al-Wazir
- Ziyad Saeed

### Supervisor

**Dr. Waheeb Abdullah**

## Ethical and Responsible Use

This project classifies message content for educational purposes. It should not be treated as a perfect security control or as a replacement for human review, email security gateways, or organizational policies.

Do not use the system to collect, expose, or process private messages without appropriate authorization. Remove personal information from datasets before sharing them, protect deployed API endpoints, and validate model results before taking action against a user or account.

## Future Improvements

- Add automated unit and API tests.
- Add a held-out evaluation report with reproducible metric output.
- Add multilingual preprocessing and Arabic-language support.
- Add model versioning and artifact integrity checks.
- Add Docker and deployment configuration.
- Add explainability features showing influential terms.
- Add rate limiting and authentication for public API deployments.
