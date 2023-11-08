-- Create a table to store information about fitness classes.
CREATE TABLE Class (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each class.
    name TEXT NOT NULL, -- Name of the class.
    instructor TEXT NOT NULL, -- Name of the instructor.
    time TIME NOT NULL, -- Time of the class.
    capacity INTEGER NOT NULL -- Maximum number of students allowed in the class.
);

-- Create a table to store information about students.
CREATE TABLE Student (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each student.
    name TEXT NOT NULL, -- Name of the student.
    email TEXT UNIQUE NOT NULL -- Unique email address of the student.
);

-- Create a table to record class bookings made by students.
CREATE TABLE Booking (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each booking.
    studentId INTEGER, -- References the student who made the booking.
    classId INTEGER, -- References the class that was booked.
    FOREIGN KEY (studentId) REFERENCES Student(id), -- Enforce referential integrity.
    FOREIGN KEY (classId) REFERENCES Class(id) -- Enforce referential integrity.
);

-- Create a table to track attendance in classes.
CREATE TABLE Attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each attendance record.
    bookingId INTEGER, -- References the booking associated with the attendance.
    status TEXT NOT NULL, -- Attendance status (e.g., "Present" or "Absent").
    FOREIGN KEY (bookingId) REFERENCES Booking(id) -- Enforce referential integrity.
);


-- Insert data into the Book table
INSERT INTO Book (title, author, genre, price, stock)
VALUES
    ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 19.99, 50),
    ('The Da Vinci Code', 'Dan Brown', 'Mystery', 15.95, 30),
    ('To Kill a Mockingbird', 'Harper Lee', 'Classic', 12.99, 25),
    ('Dune', 'Frank Herbert', 'Science Fiction', 22.50, 40);

-- Insert data into the Customer table
INSERT INTO Customer (name, email)
VALUES
    ('Mera Johnson', 'Mera@example.com'),
    ('David Smith', 'david@example.com'),
    ('Eve Wilson', 'eve@example.com');

-- Insert data into the "Order" table
INSERT INTO "Order" (customerId, date)
VALUES
    (1, '2023-10-10'),
    (2, '2023-10-09'),
    (3, '2023-10-08');

-- Insert data into the OrderDetail table
INSERT INTO OrderDetail (orderId, bookId, quantity)
VALUES
    (1, 1, 2),
    (1, 2, 1),
    (2, 3, 3),
    (3, 4, 2);
