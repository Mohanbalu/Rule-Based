import json

with open('knowledge_base.json', 'r') as file:
    knowledge_base = json.load(file)

def match_symptoms_with_explanation(user_symptoms, disease_entry):
    disease_symptoms = disease_entry["symptoms"]
    matched = list(set(user_symptoms) & set(disease_symptoms))
    if len(user_symptoms) == 0:
        match_score = 0
    else:
        match_score = len(matched) / len(user_symptoms)
    overall_confidence = match_score * disease_entry["confidence"]
    return overall_confidence, matched
def diagnose_with_explanation(user_symptoms, threshold=0.1, top_n=3):
    results = []
    for disease in knowledge_base:
        confidence, matched_symptoms = match_symptoms_with_explanation(user_symptoms, disease)
        if confidence >= threshold:
            critical_matched = []
            if "critical_symptoms" in disease:
                critical_matched = list(set(user_symptoms) & set(disease["critical_symptoms"]))
            results.append({
                "disease": disease["disease"],
                "confidence": round(confidence, 2),
                "matched_symptoms": matched_symptoms,
                "critical_matched": critical_matched,
                "recommendation": disease["recommendation"]
            })
    results.sort(key=lambda x: x["confidence"], reverse=True)
    return results[:top_n]
