from faker import Faker
import sqlite3
import random

fake = Faker()

# Connect to the database
conn = sqlite3.connect('db/OnlineLearningManagementSystem.db')
cursor = conn.cursor()

# Generate data for Courses
for _ in range(10):
    cursor.execute(
        "INSERT INTO Courses (course_name, description) VALUES (?, ?)", (fake.word(), fake.text()))

# Generate data for Instructors
for _ in range(5):
    cursor.execute("INSERT INTO Instructors (name, email) VALUES (?, ?)",
                   (fake.name(), fake.email()))

# Generate data for Students
for _ in range(20):
    cursor.execute("INSERT INTO Students (name, email) VALUES (?, ?)",
                   (fake.name(), fake.email()))

# Generate data for Enrollments
for _ in range(30):
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)",
                   (random.randint(1, 20), random.randint(1, 10)))

# Generate data for Assignments
for _ in range(15):
    cursor.execute("INSERT INTO Assignments (course_id, title, due_date) VALUES (?, ?, ?)",
                   (random.randint(1, 10), fake.word(), fake.date()))

# Generate data for Submissions
for _ in range(40):
    cursor.execute("INSERT INTO Submissions (assignment_id, student_id, submission_date, grade) VALUES (?, ?, ?, ?)",
                   (random.randint(1, 15), random.randint(1, 20), fake.date(), random.randint(0, 100)))

# Commit and close
conn.commit()
conn.close()
