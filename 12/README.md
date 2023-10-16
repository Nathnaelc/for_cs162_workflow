# Online Learning Management System Database

## Overview

The Online Learning Management System (LMS) is designed to facilitate the educational journey of students in a digital environment. The database serves as the backbone of the system, storing vital information about courses, instructors, students, enrollments, assignments, and submissions. It aims to provide a seamless experience for both students and instructors by organizing data in a structured manner.

## Database Schema

The database consists of six main tables:

1. `Courses`: Stores details about the courses offered, including course name and description.
2. `Instructors`: Contains information about the instructors, such as name and email.
3. `Students`: Holds details about the students, including name and email.
4. `Enrollments`: Records the courses that students are enrolled in.
5. `Assignments`: Contains information about assignments for each course.
6. `Submissions`: Keeps track of assignment submissions by students.

## Context

The database is designed to answer key questions that are essential for the functioning of an online learning platform:

- What courses are available?
- Who are the instructors for each course?
- Which students are enrolled in a particular course?
- What assignments are due in each course?
- Have students submitted their assignments?

---

# Patient Health Record and Medical History Tracker Database

## Overview

The Patient Health Record and Medical History Tracker is a healthcare database system designed to store and manage critical information about patients, doctors, appointments, medical records, and prescriptions. The database aims to streamline healthcare processes and improve patient care by providing a centralized repository of data.

## Database Schema

The database consists of five main tables:

1. `Patients`: Stores personal and contact details of patients.
2. `Doctors`: Contains professional details of doctors.
3. `Appointments`: Holds appointment details between patients and doctors.
4. `MedicalRecords`: Keeps a record of each patient's medical history.
5. `Prescriptions`: Stores prescription details for patients.

## Context

The database is structured to answer essential questions that healthcare providers and patients commonly have:

- What are the upcoming appointments for a patient?
- What prescriptions have been issued to a patient?
- What is the medical history of a patient?

By answering these questions, the database serves as a valuable tool for healthcare providers, enabling them to make informed decisions and provide better care.

Both databases are designed with normalization principles to ensure data integrity, reduce data redundancy, and improve data retrieval speed. They are scalable and can be extended easily to include more functionalities as needed.
