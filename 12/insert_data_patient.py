from faker import Faker
import sqlite3

fake = Faker()

# Connect to the database
conn = sqlite3.connect('db/PatientHealthRecord.db')
cursor = conn.cursor()

# Generate data for Patients
for _ in range(20):
    cursor.execute(
        "INSERT INTO Patients (name, email, dob) VALUES (?, ?, ?)", (fake.name(), fake.email(), fake.date_of_birth()))

# Generate data for Doctors
for _ in range(10):
    cursor.execute(
        "INSERT INTO Doctors (name, specialty) VALUES (?, ?)", (fake.name(), fake.job()))

# Generate data for Appointments
for _ in range(50):
    cursor.execute(
        "INSERT INTO Appointments (patient_id, doctor_id, appointment_date) VALUES (?, ?, ?)", (fake.random_int(min=1, max=20), fake.random_int(min=1, max=10), fake.date_this_year()))

# Generate data for MedicalRecords
for _ in range(100):
    cursor.execute(
        "INSERT INTO MedicalRecords (patient_id, diagnosis, treatment) VALUES (?, ?, ?)", (fake.random_int(min=1, max=20), fake.bs(), fake.catch_phrase()))

# Generate data for Prescriptions
for _ in range(100):
    cursor.execute(
        "INSERT INTO Prescriptions (patient_id, medication, dosage) VALUES (?, ?, ?)", (fake.random_int(min=1, max=20), fake.random_element(['Ibuprofen', 'Paracetamol', 'Aspirin']), fake.random_element(['100mg', '200mg', '50mg'])))

# Commit and close
conn.commit()
conn.close()
