-- Create table for Patients
CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    dob DATE NOT NULL
);

-- Create table for Doctors
CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL
);

-- Create table for Appointments
CREATE TABLE Appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Create table for MedicalRecords
CREATE TABLE MedicalRecords (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    diagnosis TEXT NOT NULL,
    treatment TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Create table for Prescriptions
CREATE TABLE Prescriptions (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    medication TEXT NOT NULL,
    dosage TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
