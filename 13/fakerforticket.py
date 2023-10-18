import sqlite3
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to SQLite database
conn = sqlite3.connect('db/ticketapp.db')
cursor = conn.cursor()

# Generate and insert data for Customers
for _ in range(20):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    cursor.execute(
        "INSERT INTO Customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))

# Generate and insert data for Tickets
for _ in range(20):
    customer_id = fake.random_int(min=1, max=20)
    issue_type = fake.random_element(['Technical', 'Billing', 'General'])
    status = fake.random_element(['open', 'in_progress', 'closed'])
    created_at = fake.date_time_this_year()
    closed_at = fake.date_time_this_year() if status == 'closed' else None
    cursor.execute("INSERT INTO Tickets (customer_id, issue_type, status, created_at, closed_at) VALUES (?, ?, ?, ?, ?)",
                   (customer_id, issue_type, status, created_at, closed_at))

# Generate and insert data for Agents
for _ in range(5):
    name = fake.name()
    email = fake.email()
    cursor.execute(
        "INSERT INTO Agents (name, email) VALUES (?, ?)", (name, email))

# Generate and insert data for Ticket_Assignments
for _ in range(20):
    ticket_id = fake.random_int(min=1, max=20)
    agent_id = fake.random_int(min=1, max=5)
    cursor.execute(
        "INSERT INTO Ticket_Assignments (ticket_id, agent_id) VALUES (?, ?)", (ticket_id, agent_id))

# Commit changes and close connection
conn.commit()
conn.close()
