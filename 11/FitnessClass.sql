-- Create a table to store information about books in the inventory.
CREATE TABLE Book (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each book.
    title TEXT NOT NULL, -- Title of the book.
    author TEXT NOT NULL, -- Author of the book.
    genre TEXT NOT NULL, -- Genre of the book.
    price REAL NOT NULL, -- Price of the book.
    stock INTEGER NOT NULL -- Quantity of the book in stock.
);

-- Create a table to store information about customers.
CREATE TABLE Customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each customer.
    name TEXT NOT NULL, -- Name of the customer.
    email TEXT UNIQUE NOT NULL -- Unique email address of the customer.
);

-- Create a table to record customer orders.
CREATE TABLE "Order" (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each order.
    customerId INTEGER, -- References the customer who placed the order.
    date DATE NOT NULL, -- Date when the order was placed.
    FOREIGN KEY (customerId) REFERENCES Customer(id) -- Enforce referential integrity.
);

-- Create a table to store details of items in each order.
CREATE TABLE OrderDetail (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each order detail.
    orderId INTEGER, -- References the order to which the detail belongs.
    bookId INTEGER, -- References the book in the order.
    quantity INTEGER NOT NULL, -- Quantity of the book in the order.
    FOREIGN KEY (orderId) REFERENCES "Order"(id), -- Enforce referential integrity.
    FOREIGN KEY (bookId) REFERENCES Book(id) -- Enforce referential integrity.
);


-- Insert data into the Class table
INSERT INTO Class (name, instructor, time, capacity)
VALUES
    ('Yoga', 'Instructor A', '09:00 AM', 20),
    ('Pilates', 'Instructor B', '10:30 AM', 15),
    ('Zumba', 'Instructor C', '12:00 PM', 25);

-- Insert data into the Student table
INSERT INTO Student (name, email)
VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Bob Johnson', 'bob@example.com');

-- Insert data into the Booking table
INSERT INTO Booking (studentId, classId)
VALUES
    (1, 1),
    (2, 1),
    (2, 2),
    (3, 3);

-- Insert data into the Attendance table
INSERT INTO Attendance (bookingId, status)
VALUES
    (1, 'Present'),
    (2, 'Present'),
    (3, 'Present'),
    (4, 'Present');

