import streamlit as st
from inference_engine import infer_conditions


st.set_page_config(
    page_title="Medical Symptom Expert System",
    page_icon="🩺",
    layout="centered"
)
st.markdown(
    """
    <style>
    h1 { color: #0F9D8A; }
    h2, h3 { color: #1F6F8B; }

    div.stButton > button {
        background-color: #0F9D8A;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #0B7A6B;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------------
# Page Title
# -------------------------------

st.title("🩺 Medical Symptom Expert System")

st.write(
    "Select your symptoms below and the rule-based "
    "expert system will identify possible conditions."
)


# -------------------------------
# Symptoms
# -------------------------------

symptom_options = {
    "Fever": "fever",
    "Cough": "cough",
    "Sore Throat": "sore_throat",
    "Runny Nose": "runny_nose",
    "Sneezing": "sneezing",
    "Itchy Eyes": "itchy_eyes",

    "Headache": "headache",
    "Nausea": "nausea",
    "Light Sensitivity": "light_sensitivity",

    "Stomach Pain": "stomach_pain",
    "Vomiting": "vomiting",
    "Diarrhea": "diarrhea",

    "Thirst": "thirst",
    "Dry Mouth": "dry_mouth",
    "Dizziness": "dizziness",

    "Facial Pain": "facial_pain",
    "Nasal Congestion": "nasal_congestion",

    "Chest Discomfort": "chest_discomfort",
    "Fatigue": "fatigue",

    "Heartburn": "heartburn",

    "Rapid Heartbeat": "rapid_heartbeat",
    "Sweating": "sweating",

    "Difficulty Concentrating": "difficulty_concentrating",
    "Daytime Sleepiness": "daytime_sleepiness",

    "Eye Pain": "eye_pain",
    "Blurred Vision": "blurred_vision",

    "Body Pain": "body_pain",

    "Breathing Difficulty": "breathing_difficulty",

    "Pale Skin": "pale_skin",

    "Burning Urination": "burning_urination",
    "Frequent Urination": "frequent_urination",
    "Lower Abdominal Pain": "lower_abdominal_pain",

    "Difficulty Passing Stool": "difficulty_passing_stool",
    "Abdominal Discomfort": "abdominal_discomfort",
    "Bloating": "bloating",

    "Heavy Sweating": "heavy_sweating",
    "Weakness": "weakness"
}


st.subheader("Select Your Symptoms")

selected_labels = st.multiselect(
    "Choose the symptoms you are experiencing:",
    list(symptom_options.keys())
)


# Convert labels into internal symptom names

selected_symptoms = {
    symptom_options[label]
    for label in selected_labels
}


# -------------------------------
# Analyze Button
# -------------------------------

if st.button("🔍 Analyze Symptoms"):

    if not selected_symptoms:

        st.warning(
            "Please select at least one symptom."
        )

    else:

        results = infer_conditions(
            selected_symptoms
        )

        st.subheader("🔎 Expert System Result")

        if not results:

            st.info(
                "No matching rule was found in the knowledge base."
            )

        else:

            best_result = results["conditions"][0]

            st.success(
                f"Possible Condition: "
                f"{best_result['name']}"
            )

            match_percentage = (
                best_result["score"]
            )

            st.write(
                f"Rule Match: "
                f"{match_percentage:.0f}%"
            )

            st.write("### Matched Symptoms")

            for symptom in best_result["matched_symptoms"]:

                st.write(
                    f"✓ {symptom.replace('_', ' ').title()}"
                )

            st.write("### Basic Guidance")

            for advice in best_result["guidance"]:

                st.write(
                    f"• {advice}"
                )


# -------------------------------
# Disclaimer
# -------------------------------

st.divider()

st.warning(
    "⚠️ This system is an educational rule-based "
    "expert system and does not provide a medical diagnosis. "
    "For proper diagnosis and treatment, consult a qualified "
    "healthcare professional."
)