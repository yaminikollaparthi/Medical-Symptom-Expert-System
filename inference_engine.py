from rules import RULES, EMERGENCY_RULES


def calculate_rule_score(selected_symptoms, rule):
    rule_symptoms = set(rule["symptoms"])
    matched = set(selected_symptoms) & rule_symptoms

    if not rule_symptoms:
        return 0, matched

    match_percentage = len(matched) / len(rule_symptoms) * 100
    priority_bonus = (rule.get("priority", 1) - 1) * 5
    score = min(100, match_percentage + priority_bonus)

    return round(score, 2), matched



def check_emergency(selected_symptoms):
    """
    Check whether any emergency warning rule
    has been triggered.
    """

    emergencies = []

    for rule in EMERGENCY_RULES:

        matched = selected_symptoms.intersection(
            rule["symptoms"]
        )

        if matched:

            emergencies.append({
                "name": rule["name"],
                "message": rule["message"],
                "matched": matched
            })

    return emergencies


def infer_conditions(selected_symptoms):
    selected_symptoms = set(selected_symptoms)

    emergencies = check_emergency(selected_symptoms)

    results = []
    for rule in RULES:
        score, matched = calculate_rule_score(selected_symptoms, rule)

        if score > 0:
            results.append({
                "name": rule["name"],
                "score": score,                      # already 0-100
                "matched_count": len(matched),
                "matched_symptoms": sorted(matched),
                "priority": rule.get("priority", 1),
                "total_symptoms": len(rule["symptoms"]),
                "guidance": rule["guidance"],
            })

    results.sort(
        key=lambda x: (x["score"], x["matched_count"], x["priority"]),
        reverse=True,
    )

    if not results and not emergencies:
        return None

    return {
        "emergencies": emergencies,
        "conditions": results[:3],
    }