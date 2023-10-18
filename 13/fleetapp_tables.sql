CREATE TABLE Cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    make TEXT NOT NULL,
    year INTEGER NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE Rentals (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    customer_id INTEGER,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    total_price REAL NOT NULL,
    FOREIGN KEY (car_id) REFERENCES Cars(car_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Maintenance (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    cost REAL NOT NULL,
    FOREIGN KEY (car_id) REFERENCES Cars(car_id)
);
