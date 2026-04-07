import re


def extract_age(text):

    match = re.search(r"\b(\d{1,3})\s*(?:years?|yrs?)\b", text)
    return int(match.group(1)) if match else 40


def detect_symptoms(text):

    text = text.lower()

    symptom_keywords = {
    "chest_pain": ["chest pain", "pain in chest", "chest hurts"],
    "shortness_of_breath": ["shortness of breath", "breathless", "cant breathe"],
    "vomiting": ["vomiting", "throwing up", "nausea"],
    "dizziness": ["dizziness", "dizzy", "lightheaded"],
    "headache": ["headache", "head pain"],
    "trauma": ["trauma", "injury", "accident"],
    "bleeding": ["bleeding", "bleed", "blood"],
    "confusion": ["confusion", "confused", "disoriented"]
}

    negations = ["no", "not", "denies", "without"]

    symptoms = {}
    detected = []

    for symptom, keywords in symptom_keywords.items():

        value = 0

        for word in keywords:

            if word in text:

                negated = False

                for neg in negations:
                    if f"{neg} {word}" in text:
                        negated = True

                if not negated:
                    value = 1
                    detected.append(symptom)

        symptoms[symptom] = value

    return symptoms, detected


def build_features(text):

    text = text.lower()

    symptoms, detected = detect_symptoms(text)

    features = {

        "age": extract_age(text),

        "heart_rate": 90,
        "systolic_blood_pressure": 120,
        "oxygen_saturation": 98,

        "body_temperature": 38 if "fever" in text else 36.5,

        "chronic_disease_count": 0,
        "previous_er_visits": 0,

        "chest_pain": symptoms.get("chest_pain", 0),
        "shortness_of_breath": symptoms.get("shortness_of_breath", 0),
        "vomiting": symptoms.get("vomiting", 0),
        "dizziness": symptoms.get("dizziness", 0),
        "headache": symptoms.get("headache", 0),
        "trauma": symptoms.get("trauma", 0),
        "bleeding": symptoms.get("bleeding", 0),
        "confusion": symptoms.get("confusion", 0),

        "arrival_mode_walk_in": 1,
        "arrival_mode_wheelchair": 0
    }

    return features, detected
