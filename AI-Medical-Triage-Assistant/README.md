README.md

🧠 AI Medical Triage Assistant

An intelligent machine learning system that analyzes patient-described symptoms and predicts the urgency level of their medical condition.


🚀 Overview

This project simulates a real-world medical triage system used in emergency care.

Users describe their symptoms in natural language, and the system:

Extracts key medical symptoms
Handles negations (e.g., "no chest pain")
Builds structured clinical features
Predicts triage level using a trained ML model


🏗️ System Architecture

User Input (Text)
        ↓
Symptom Extraction (Keyword + Negation Detection)
        ↓
Feature Engineering
        ↓
Random Forest Model
        ↓
Triage Prediction (Emergency / Urgent / Mild / Non-Urgent)


⚙️ Tech Stack

Python
Scikit-learn (RandomForestClassifier)
Streamlit (UI)
Pandas
Regex-based NLP



📊 Features

✅ Natural language symptom input

✅ Custom symptom extraction engine

✅ Negation detection (e.g., “no bleeding”)

✅ Real-time triage classification

✅ Confidence scoring

✅ Interactive UI with alerts


🧪 Example Input
"I am 70 years old with chest pain and shortness of breath"



📤 Output

Predicted Level: Emergency

Status: Critical

Confidence: 0.91

Detected Symptoms: chest_pain, shortness_of_breath



⚠️ Challenges & Learnings

1. Overfitting

The model initially achieved near 100% accuracy due to:

Dataset imbalance
Feature leakage



✅ Solution:

Applied hyperparameter tuning

Improved feature selection

Validated with proper splits


2. Feature Misalignment (“Severity Error”)

Mismatch between:

Training features

Inference-time features

✅ Solution:

Used:

df = df.reindex(columns=model.feature_names_in_, fill_value=0)


3. Dataset Quality Issues
   
Inconsistent symptom labeling
Missing values

✅ Solution:

Cleaned and standardized inputs
Built robust fallback defaults



🖥️ How to Run

pip install -r requirements.txt

streamlit run MED_TRIAGE_UI_2.py



📁 Project Structure

medical-triage-ai/

│
├── feature_builder.py

├── MED_TRIAGE_UI_2.py

├── Medical_triage_model.pkl

├── requirements.txt

└── README.md


⚠️ Disclaimer

This system is for educational purposes only and is not a substitute for professional medical diagnosis.



🚀 Future Improvements

Upgrade to NLP models (SpaCy / Transformers)

Deploy as a web API (FastAPI)

Integrate real-time hospital recommendation

Improve dataset quality and size
