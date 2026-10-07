RULES = [

    # Rule 1
    {
        "name": "Flu-like Symptoms",
        "symptoms": {"fever", "cough", "sore_throat"},
        "guidance": [
            "Take adequate rest.",
            "Drink plenty of fluids.",
            "Monitor your temperature.",
            "Consult a healthcare professional if symptoms become severe."
        ]
    },

    # Rule 2
    {
        "name": "Common Cold",
        "symptoms": {"runny_nose", "sneezing", "sore_throat"},
        "guidance": [
            "Get adequate rest.",
            "Drink warm fluids.",
            "Stay hydrated.",
            "Seek medical advice if symptoms persist or worsen."
        ]
    },

    # Rule 3
    {
        "name": "Allergic Rhinitis",
        "symptoms": {"sneezing", "runny_nose", "itchy_eyes"},
        "guidance": [
            "Try to avoid known allergens.",
            "Keep your surroundings clean.",
            "Monitor your symptoms.",
            "Consult a healthcare professional if symptoms persist."
        ]
    },

    # Rule 4
    {
        "name": "Migraine-like Symptoms",
        "symptoms": {"headache", "nausea", "light_sensitivity"},
        "guidance": [
            "Rest in a quiet environment.",
            "Stay hydrated.",
            "Avoid bright lights if they worsen symptoms.",
            "Consult a healthcare professional for recurrent or severe headaches."
        ]
    },

    # Rule 5
    {
        "name": "Gastrointestinal Infection-like Symptoms",
        "symptoms": {"stomach_pain", "vomiting", "diarrhea"},
        "guidance": [
            "Drink fluids to reduce the risk of dehydration.",
            "Take adequate rest.",
            "Monitor your symptoms.",
            "Seek medical attention if symptoms are severe or persistent."
        ]
    },

    # Rule 6
    {
        "name": "Possible Dehydration",
        "symptoms": {"thirst", "dry_mouth", "dizziness"},
        "guidance": [
            "Drink water regularly.",
            "Rest in a cool environment.",
            "Monitor your symptoms.",
            "Seek medical attention if dizziness is severe or persistent."
        ]
    },

    # Rule 7
    {
        "name": "Possible Sinus-related Symptoms",
        "symptoms": {"headache", "facial_pain", "nasal_congestion"},
        "guidance": [
            "Stay hydrated.",
            "Rest adequately.",
            "Avoid known irritants.",
            "Consult a healthcare professional if symptoms persist."
        ]
    },

    # Rule 8
    {
        "name": "Possible Bronchitis-like Symptoms",
        "symptoms": {"cough", "chest_discomfort", "fatigue"},
        "guidance": [
            "Take adequate rest.",
            "Stay hydrated.",
            "Avoid smoke and other respiratory irritants.",
            "Consult a healthcare professional for persistent or worsening symptoms."
        ]
    },

    # Rule 9
    {
        "name": "Possible Acid Reflux Symptoms",
        "symptoms": {"heartburn", "chest_discomfort", "nausea"},
        "guidance": [
            "Avoid large meals.",
            "Avoid lying down immediately after eating.",
            "Monitor foods that trigger symptoms.",
            "Consult a healthcare professional if symptoms are frequent or severe."
        ]
    },

    # Rule 10
    {
        "name": "Possible Food Poisoning",
        "symptoms": {"stomach_pain", "vomiting", "diarrhea", "fever"},
        "guidance": [
            "Drink fluids to prevent dehydration.",
            "Take adequate rest.",
            "Avoid foods that worsen symptoms.",
            "Seek medical attention if symptoms are severe."
        ]
    },

    # Rule 11
    {
        "name": "Possible Anxiety-related Symptoms",
        "symptoms": {"rapid_heartbeat", "sweating", "dizziness"},
        "guidance": [
            "Move to a calm environment.",
            "Try slow and controlled breathing.",
            "Rest and monitor your symptoms.",
            "Seek professional help if symptoms are frequent or severe."
        ]
    },

    # Rule 12
    {
        "name": "Possible Sleep-related Fatigue",
        "symptoms": {"fatigue", "difficulty_concentrating", "daytime_sleepiness"},
        "guidance": [
            "Maintain a regular sleep schedule.",
            "Aim for adequate sleep.",
            "Limit excessive screen use before bedtime.",
            "Consult a healthcare professional if persistent."
        ]
    },

    # Rule 13
    {
        "name": "Possible Eye Strain",
        "symptoms": {"eye_pain", "blurred_vision", "headache"},
        "guidance": [
            "Take regular breaks from screens.",
            "Use adequate lighting.",
            "Rest your eyes.",
            "Consult an eye-care professional if symptoms persist."
        ]
    },

    # Rule 14
    {
        "name": "Possible Viral Infection",
        "symptoms": {"fever", "fatigue", "body_pain"},
        "guidance": [
            "Take adequate rest.",
            "Drink plenty of fluids.",
            "Monitor your temperature.",
            "Consult a healthcare professional if symptoms worsen."
        ]
    },

    # Rule 15
    {
        "name": "Possible Respiratory Infection",
        "symptoms": {"cough", "fever", "breathing_difficulty"},
        "guidance": [
            "Rest and stay hydrated.",
            "Monitor your breathing.",
            "Avoid smoke and other respiratory irritants.",
            "Seek prompt medical attention, especially if breathing difficulty is significant."
        ]
    },

    # Rule 16
    {
        "name": "Possible Anemia-related Symptoms",
        "symptoms": {"fatigue", "dizziness", "pale_skin"},
        "guidance": [
            "Maintain a balanced diet.",
            "Discuss persistent symptoms with a healthcare professional.",
            "A healthcare professional may recommend appropriate blood tests."
        ]
    },

    # Rule 17
    {
        "name": "Possible Urinary Tract Infection",
        "symptoms": {"burning_urination", "frequent_urination", "lower_abdominal_pain"},
        "guidance": [
            "Drink adequate fluids unless medically restricted.",
            "Monitor your symptoms.",
            "Consult a healthcare professional for proper evaluation and treatment."
        ]
    },

    # Rule 18
    {
        "name": "Possible Constipation",
        "symptoms": {"difficulty_passing_stool", "abdominal_discomfort", "bloating"},
        "guidance": [
            "Drink adequate water.",
            "Include appropriate dietary fiber.",
            "Maintain regular physical activity.",
            "Consult a healthcare professional if symptoms are persistent or severe."
        ]
    },

    # Rule 19
    {
        "name": "Possible Heat-related Illness",
        "symptoms": {"heavy_sweating", "dizziness", "weakness"},
        "guidance": [
            "Move to a cool place.",
            "Drink fluids.",
            "Rest and avoid strenuous activity.",
            "Seek urgent medical attention if confusion, fainting, or severe symptoms occur."
        ]
    },

    # Rule 20
    {
        "name": "Possible Headache-related Condition",
        "symptoms": {"headache", "fatigue", "difficulty_concentrating"},
        "guidance": [
            "Rest in a quiet environment.",
            "Stay hydrated.",
            "Take breaks from prolonged screen use.",
            "Consult a healthcare professional if headaches are severe, recurrent, or unusual."
        ]
    }
]
EMERGENCY_RULES = [

    {
        "name": "Severe Breathing Difficulty",
        "symptoms": {
            "severe_breathing_difficulty"
        },
        "message": (
            "Severe breathing difficulty can require urgent medical attention."
        )
    },

    {
        "name": "Severe Chest Pain",
        "symptoms": {
            "severe_chest_pain"
        },
        "message": (
            "Severe chest pain can require urgent medical evaluation."
        )
    },

    {
        "name": "Fainting or Loss of Consciousness",
        "symptoms": {
            "fainting"
        },
        "message": (
            "Fainting or loss of consciousness may require urgent medical evaluation."
        )
    },

    {
        "name": "Confusion",
        "symptoms": {
            "confusion"
        },
        "message": (
            "Sudden or severe confusion can require urgent medical attention."
        )
    },

    {
        "name": "Blue Lips or Face",
        "symptoms": {
            "blue_lips"
        },
        "message": (
            "Blue lips or face can indicate a serious problem and require urgent medical attention."
        )
    }
]