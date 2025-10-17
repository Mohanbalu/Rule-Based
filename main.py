import streamlit as st
import json
from inference_engine import diagnose_with_explanation
from patient_module import save_patient_data
from analytics_module import most_common_diseases, most_common_symptoms
from admin_module import add_rule, update_rule_confidence, delete_rule

with open("knowledge_base.json", "r") as f:
    kb = json.load(f)

all_symptoms = set()
for disease in kb:
    all_symptoms.update(disease["symptoms"])

st.set_page_config(page_title="Medical Diagnosis System", layout="wide")
st.title("🩺 Advanced Medical Rule-Based System")

user_type = st.sidebar.radio("Select User Type", ["Patient", "Admin"])

if user_type == "Patient":
    st.header("Patient Module - Step-by-Step Wizard")

    # Initialize session state
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "name" not in st.session_state:
        st.session_state.name = ""
    if "age" not in st.session_state:
        st.session_state.age = 0
    if "gender" not in st.session_state:
        st.session_state.gender = ""
    if "user_symptoms" not in st.session_state:
        st.session_state.user_symptoms = []

    if st.session_state.step == 1:
        st.subheader("Step 1: Patient Information")
        st.session_state.name = st.text_input("Name", st.session_state.name)
        st.session_state.age = st.number_input("Age", min_value=0, max_value=120, value=st.session_state.age)
        st.session_state.gender = st.selectbox("Gender", ["M", "F"], index=0 if st.session_state.gender=="M" else 1)
        if st.button("Next"):
            if st.session_state.name.strip() == "":
                st.warning("Enter your name")
            else:
                st.session_state.step = 2

    elif st.session_state.step == 2:
        st.subheader("Step 2: Select Your Symptoms")
        selected_symptoms = st.multiselect(
            "Select symptoms",
            options=list(all_symptoms),
            default=st.session_state.user_symptoms
        )
        additional_input = st.text_input(
            "Or type additional symptoms (comma-separated)"
        )
        if st.button("Diagnose"):
            typed_symptoms = [s.strip().lower().replace(" ", "_") for s in additional_input.split(",") if s.strip()]
            st.session_state.user_symptoms = [s.lower().replace(" ", "_") for s in selected_symptoms] + typed_symptoms

            if len(st.session_state.user_symptoms) == 0:
                st.warning("Please enter at least one symptom!")
            else:
                results = diagnose_with_explanation(st.session_state.user_symptoms, threshold=0.1, top_n=1)
                
                if results:
                    st.subheader("Top Probable Diagnoses")
                    for i, res in enumerate(results, start=1):
                        st.markdown(f"**{i}. {res['disease']} (Confidence: {res['confidence']})**")
                        st.write(f"- Matched Symptoms: {', '.join(res['matched_symptoms'])}")
                        if res['critical_matched']:
                            st.error(f"⚠️ Critical Symptoms Matched: {', '.join(res['critical_matched'])}")
                        st.info(f"Recommendation: {res['recommendation']}")
                else:
                    st.error("No matching disease found. Please consult a doctor.")

                # Save patient data
                save_patient_data(st.session_state.name, st.session_state.age, st.session_state.gender, st.session_state.user_symptoms, results)

elif user_type == "Admin":
    st.header("Admin Dashboard")

    st.subheader("Analytics")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Most Common Diagnoses**")
        common_diseases = most_common_diseases()
        st.bar_chart(common_diseases)
    with col2:
        st.markdown("**Most Reported Symptoms**")
        common_symptoms = most_common_symptoms()
        st.bar_chart(common_symptoms)

    st.subheader("Rule Management")
    action = st.radio("Select Action", ["Add Rule", "Update Rule Confidence", "Delete Rule"])

    if action == "Add Rule":
        with st.form("add_rule_form"):
            disease = st.text_input("Disease Name")
            symptoms = st.text_area("Symptoms (comma-separated)")
            critical = st.text_area("Critical Symptoms (comma-separated)")
            confidence = st.number_input("Confidence (0-1)", min_value=0.0, max_value=1.0, value=0.8)
            recommendation = st.text_area("Recommendation")
            submit_add = st.form_submit_button("Add Rule")
        if submit_add:
            add_rule(disease, [s.strip().lower().replace(" ", "_") for s in symptoms.split(",")],
                     confidence,
                     recommendation)
            st.success(f"Rule for {disease} added successfully.")

    elif action == "Update Rule Confidence":
        with st.form("update_rule_form"):
            disease_name = st.text_input("Disease Name")
            new_confidence = st.number_input("New Confidence (0-1)", min_value=0.0, max_value=1.0, value=0.8)
            submit_update = st.form_submit_button("Update Confidence")
        if submit_update:
            update_rule_confidence(disease_name, new_confidence)
            st.success(f"Confidence for {disease_name} updated successfully.")

    elif action == "Delete Rule":
        with st.form("delete_rule_form"):
            disease_name = st.text_input("Disease Name to Delete")
            submit_delete = st.form_submit_button("Delete Rule")
        if submit_delete:
            delete_rule(disease_name)
            st.success(f"Rule for {disease_name} deleted successfully.")
