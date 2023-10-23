-- List of all appointments for a patient.
-- This is crucial for both patients and healthcare providers to keep track of scheduled visits, treatments, or consultations. 
-- It helps in planning and ensures that no appointments are missed.
SELECT a.appointment_id, a.appointment_date, d.name AS doctor_name, d.specialty
FROM Appointments AS a
JOIN Doctors AS d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 1;

-- output: 
-- appointment_id	appointment_date	doctor_name	specialty
-- 11	2023-08-09	Samantha Hernandez	Lawyer

-- List of all prescriptions for a patient.
-- Medication management is a key aspect of healthcare. 
-- Having a centralized list of all prescriptions helps in avoiding drug interactions, overdoses, and ensures that the patient is on the correct treatment plan.
SELECT p.prescription_id, p.medication, p.dosage
FROM Prescriptions AS p
WHERE p.patient_id = 1;

-- output:
-- prescription_id	medication	dosage
-- 28	             Aspirin	50mg
-- 36	             Aspirin	100mg
-- 43	             Aspirin	200mg
-- 48	         Paracetamol	100mg
-- 76	         Paracetamol	200mg

-- Medical history of a patient.
-- A comprehensive medical history is essential for diagnosis and treatment planning. 
-- It provides doctors with the information they need to make informed medical decisions.
SELECT m.record_id, m.diagnosis, m.treatment
FROM MedicalRecords AS m
WHERE m.patient_id = 1;


-- output:
-- record_id	        diagnosis	                treatment
-- 36	disintermediate world-class technologies	Implemented value-added data-warehouse
-- 57	facilitate back-end web-readiness	Synergistic even-keeled middleware
-- 64	optimize enterprise channels	Phased context-sensitive intranet

-- Transaction for adding a new patient and scheduling an appointment
BEGIN TRANSACTION;
    INSERT INTO Patients (name, email, dob) VALUES ('John Doe', 'john.doe@example.com', '1980-01-01');
    INSERT INTO Appointments (patient_id, doctor_id, appointment_date) VALUES (LAST_INSERT_ROWID(), 1, '2023-10-10');
COMMIT;

-- Explanation: This transaction ensures that when a new patient is added, an appointment is also scheduled for them. If either operation fails, the transaction will be rolled back, maintaining data integrity.

-- Transaction for updating a medical record and adding a prescription
BEGIN TRANSACTION;
    UPDATE MedicalRecords SET diagnosis = 'Updated Diagnosis', treatment = 'Updated Treatment' WHERE record_id = 1;
    INSERT INTO Prescriptions (patient_id, medication, dosage) VALUES (1, 'NewMed', '50mg');
COMMIT;

-- Explanation: This transaction ensures that when a medical record is updated, a new prescription is also added for the patient. If either operation fails, the transaction will be rolled back.

