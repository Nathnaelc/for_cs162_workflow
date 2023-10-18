import sqlite3
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# Connect to SQLite database
conn = sqlite3.connect('db/Fleetapp.db')
cursor = conn.cursor()

# Generate and insert data for Cars
for _ in range(20):
    model = fake.unique.first_name()
    make = fake.company()
    year = fake.year()
    status = fake.random_element(['available', 'rented', 'under_maintenance'])
    cursor.execute("INSERT INTO Cars (model, make, year, status) VALUES (?, ?, ?, ?)",
                   (model, make, year, status))

# Generate and insert data for Customers
for _ in range(20):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    cursor.execute(
        "INSERT INTO Customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))

# Generate and insert data for Rentals
for _ in range(20):
    car_id = fake.random_int(min=1, max=20)
    customer_id = fake.random_int(min=1, max=20)
    start_date_str = fake.date()
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = fake.date_between_dates(date_start=start_date)
    total_price = fake.random_number(digits=4)
    cursor.execute("INSERT INTO Rentals (car_id, customer_id, start_date, end_date, total_price) VALUES (?, ?, ?, ?, ?)",
                   (car_id, customer_id, start_date_str, end_date, total_price))

# Generate and insert data for Maintenance
for _ in range(20):
    car_id = fake.random_int(min=1, max=20)
    start_date_str = fake.date()
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = fake.date_between_dates(date_start=start_date)
    cost = fake.random_number(digits=3)
    cursor.execute("INSERT INTO Maintenance (car_id, start_date, end_date, cost) VALUES (?, ?, ?, ?)",
                   (car_id, start_date_str, end_date, cost))

# Commit changes and close connection
conn.commit()
conn.close()
