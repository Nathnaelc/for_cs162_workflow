-- Personal Finance Management App
-- Create tables section
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE Expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date DATE NOT NULL,
    userId INTEGER,
    FOREIGN KEY (userId) REFERENCES User(id)
);

CREATE TABLE Income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    source TEXT NOT NULL,
    date DATE NOT NULL,
    userId INTEGER,
    FOREIGN KEY (userId) REFERENCES User(id)
);

