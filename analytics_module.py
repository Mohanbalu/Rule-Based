import pandas as pd
import sqlite3

conn = sqlite3.connect('patients.db')

def get_patient_data():
    conn = sqlite3.connect("patients.db", check_same_thread=False)
    try:
        df = pd.read_sql_query("SELECT * FROM patient_history", conn)
    except Exception:
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

def most_common_diseases():
    df = get_patient_data()
    return df['diagnosis'].value_counts()

def most_common_symptoms():
    df = get_patient_data()
    all_symptoms = df['symptoms'].str.split(', ')
    all_symptoms_flat = [sym for sublist in all_symptoms for sym in sublist]
    return pd.Series(all_symptoms_flat).value_counts()
