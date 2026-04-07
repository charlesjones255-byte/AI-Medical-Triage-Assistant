import streamlit as st
import joblib
import pandas as pd

from feature_builder import build_features


# load model

model = joblib.load("Medical_triage_model.pkl")

st.title("AI Medical Triage Assistant")

st.write("Describe your symptoms in plain English.")

user_input = st.text_area(
    "Patient description",
    "Example: I am 70 years old with chest pain and shortness of breath"
)

if st.button("Assess Triage Level"):

    features, detected = build_features(user_input)

    df = pd.DataFrame([features])

    # ensure correct column order
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df).max()

    triage_map = {
        0: "Non-Urgent",
        1: "Mild",
        2: "Urgent",
        3: "Emergency"
    }

    st.subheader("Triage Assessment")

    st.write("Predicted Level:", prediction)
    st.write("Status:", triage_map[prediction])
    st.write("Confidence:", round(probability, 3))
    st.write("Detected symptoms:", detected)

    # Display alert message
    if prediction == 3:
        st.error("🚨 Emergency - Seek immediate medical care")

    elif prediction == 2:
        st.warning("⚠️ Urgent - Medical attention recommended")

    elif prediction == 1:
        st.info("Mild condition")

    else:
        st.success("Non-urgent case")


    #Symptom Frequency Visualization
    symptom_df = pd.DataFrame({
    "Symptom": detected,
    "Presence": [1]*len(detected)
    })

    st.bar_chart(symptom_df.set_index("Symptom"))


st.subheader("Clinical Disclaimer")
st.caption("⚠️ This tool is an AI assistant and not a medical diagnosis system. Always consult a healthcare professional.")
