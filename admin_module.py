import json
from inference_engine import knowledge_base

def add_rule(disease, symptoms, confidence, recommendation):
    new_rule = {
        "disease": disease,
        "symptoms": symptoms,
        "confidence": confidence,
        "recommendation": recommendation
    }
    knowledge_base.append(new_rule)
    with open('knowledge_base.json', 'w') as file:
        json.dump(knowledge_base, file, indent=4)

def update_rule_confidence(disease_name, new_confidence):
    for disease in knowledge_base:
        if disease["disease"].lower() == disease_name.lower():
            disease["confidence"] = new_confidence
    with open('knowledge_base.json', 'w') as file:
        json.dump(knowledge_base, file, indent=4)

def delete_rule(disease_name):
    global knowledge_base
    knowledge_base = [d for d in knowledge_base if d["disease"].lower() != disease_name.lower()]
    with open('knowledge_base.json', 'w') as file:
        json.dump(knowledge_base, file, indent=4)
