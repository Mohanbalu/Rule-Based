# Rule-Based Medical Diagnosis System

This project is a rule-based medical diagnosis system that utilizes a knowledge base of diseases and their associated symptoms to provide potential diagnoses based on user-provided symptoms. It includes both a patient interface for symptom input and diagnosis, and an admin interface for managing the knowledge base and viewing analytics.

## Features and Functionality

*   **Patient Module:**
    *   Step-by-step wizard for entering patient information (name, age, gender).
    *   Symptom selection via a multi-select dropdown populated from the knowledge base.
    *   Option to manually enter additional symptoms.
    *   Diagnosis based on the selected symptoms and the knowledge base.
    *   Displays the top probable diagnoses with confidence levels, matched symptoms, critical symptoms (if any), and recommendations.
    *   Saves patient data (name, age, gender, symptoms, and diagnosis results) to a SQLite database (`patients.db`).
*   **Admin Module:**
    *   Analytics dashboard displaying:
        *   Most common diseases diagnosed based on patient data.
        *   Most frequently reported symptoms.
    *   Rule management interface:
        *   **Add Rule:** Adds a new disease rule to the knowledge base.
        *   **Update Rule Confidence:** Modifies the confidence level of an existing disease rule.
        *   **Delete Rule:** Removes a disease rule from the knowledge base.

## Technology Stack

*   **Python:** The primary programming language.
*   **Streamlit:** For building the user interface.
*   **Pandas:** For data analysis in the analytics module.
*   **SQLite:** For storing patient data (`patients.db`).
*   **JSON:** For storing the knowledge base (`knowledge_base.json`).

## Prerequisites

Before running the application, ensure you have the following installed:

*   **Python 3.6 or higher:**  You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **Pip:** Python package installer (usually included with Python installations).

Install the necessary Python packages:

```bash
pip install streamlit pandas
```

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Mohanbalu/Rule-Based.git
    cd Rule-Based
    ```

2.  **Install the required Python packages (if not already done):**

    ```bash
    pip install streamlit pandas
    ```

## Usage Guide

1.  **Run the application:**

    ```bash
    streamlit run main.py
    ```

    This will start the Streamlit application and open it in your default web browser.

2.  **Using the Patient Module:**

    *   Select "Patient" from the "Select User Type" radio button in the sidebar.
    *   Follow the step-by-step wizard to enter your name, age, and gender.
    *   Select your symptoms from the multi-select dropdown.
    *   You can also type additional symptoms in the text input, separated by commas.  These will be converted to lowercase and spaces will be replaced with underscores.
    *   Click the "Diagnose" button to get the diagnosis results.  The application will display a list of potential diseases, along with their confidence levels, matched symptoms, and recommendations.

3.  **Using the Admin Module:**

    *   Select "Admin" from the "Select User Type" radio button in the sidebar.
    *   **Analytics:**  The dashboard displays charts showing the most common diagnoses and reported symptoms based on the data stored in the `patients.db` database.
    *   **Rule Management:**
        *   Select the desired action ("Add Rule", "Update Rule Confidence", or "Delete Rule") from the radio button.
        *   Fill in the required information in the corresponding form and click the submit button.
        *   **Add Rule:**
            *   **Disease Name:** The name of the disease.
            *   **Symptoms:** A comma-separated list of symptoms associated with the disease.  Each symptom will be converted to lowercase and spaces replaced with underscores.
            *   **Critical Symptoms:** A comma-separated list of *critical* symptoms for the disease.
            *   **Confidence (0-1):** A numerical value representing the confidence level of the rule.
            *   **Recommendation:**  A recommendation for the patient if they are diagnosed with this disease.
        *   **Update Rule Confidence:**
            *   **Disease Name:** The name of the disease whose confidence you want to update.
            *   **New Confidence (0-1):**  The new confidence level for the rule.
        *   **Delete Rule:**
            *   **Disease Name to Delete:**  The name of the disease rule you want to delete.

## API Documentation

This project doesn't expose a traditional API. However, the `inference_engine.py` module provides functions that could be considered as internal API endpoints:

*   **`diagnose_with_explanation(user_symptoms, threshold=0.1, top_n=3)`:**  This function takes a list of user-provided symptoms as input and returns a list of potential diagnoses, sorted by confidence level.
    *   `user_symptoms`: A list of strings representing the user's symptoms.  Symptoms should be lowercase and have underscores instead of spaces.  Example: `["cough", "fever", "sore_throat"]`
    *   `threshold`: (Optional) A minimum confidence threshold for including a diagnosis in the results. Default is `0.1`.
    *   `top_n`: (Optional) The maximum number of diagnoses to return. Default is `3`.
    *   Returns: A list of dictionaries, where each dictionary represents a diagnosis and contains the following keys: `disease`, `confidence`, `matched_symptoms`, `critical_matched`, and `recommendation`.

*   **`match_symptoms_with_explanation(user_symptoms, disease_entry)`:** This function calculates the confidence score and matched symptoms for a given disease based on user symptoms.
    *   `user_symptoms`: A list of strings representing the user's symptoms.
    *   `disease_entry`: A dictionary representing a disease entry from the `knowledge_base.json` file.
    *   Returns: A tuple containing the overall confidence score and a list of matched symptoms.

## Contributing Guidelines

Contributions to this project are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your branch to your forked repository.
5.  Submit a pull request.

Please ensure your code adheres to the following guidelines:

*   Follow PEP 8 style guidelines.
*   Write clear and concise code.
*   Add comments to explain complex logic.
*   Test your changes thoroughly.
*   Update the `README.md` file with any relevant changes to the project's functionality or usage.

## License Information

This project does not currently have a specified license.  All rights are reserved by the author.

## Contact/Support Information

For questions, bug reports, or feature requests, please contact: [Your Name/Email Here]  (Replace with the project maintainer's information)