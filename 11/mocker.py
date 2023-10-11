import sqlite3
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('session11.db')

# Create cursor object
cursor = conn.cursor()

# Generate and insert fake data for Online Bookstore
# Inserting into Book table
for _ in range(10):
    title = fake.catch_phrase()
    author = fake.name()
    genre = fake.word()
    price = fake.random_int(min=10, max=100)
    stock = fake.random_int(min=1, max=50)  # Generate a fake stock value
    cursor.execute("INSERT INTO Book (title, author, genre, price, stock) VALUES (?, ?, ?, ?, ?)",
                   (title, author, genre, price, stock))

# Inserting into Customer table
for _ in range(5):
    name = fake.name()
    email = fake.email()
    cursor.execute(
        "INSERT INTO Customer (name, email) VALUES (?, ?)", (name, email))

# Generate and insert fake data for Fitness Class Booking
# Inserting into Class table
for _ in range(5):
    class_name = fake.word()
    instructor = fake.name()
    cursor.execute(
        "INSERT INTO Class (class_name, instructor) VALUES (?, ?)", (class_name, instructor))

# Inserting into Student table
for _ in range(10):
    student_name = fake.name()
    email = fake.email()
    cursor.execute(
        "INSERT INTO Student (student_name, email) VALUES (?, ?)", (student_name, email))

# Commit changes to the database
conn.commit()

# Close the database connection
conn.close()
