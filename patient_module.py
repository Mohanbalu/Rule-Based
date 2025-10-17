import sqlite3

def save_patient_data(name, age, gender, symptoms, results):
    conn = sqlite3.connect("patients.db", check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            symptoms TEXT,
            results TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO patients(name, age, gender, symptoms, results)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        name,
        age,
        gender,
        ",".join(symptoms),
        str(results)
    ))

    conn.commit()
    conn.close()
