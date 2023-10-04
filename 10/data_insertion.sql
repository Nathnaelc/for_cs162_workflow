-- Insert mock data for Recipe Recommendation and Meal Planning app
-- User
INSERT INTO User (username, email) VALUES ('CookMaster', 'cook@example.com');
INSERT INTO User (username, email) VALUES ('Foodie', 'foodie@example.com');

-- Recipe
INSERT INTO Recipe (name, cuisine) VALUES ('Spaghetti', 'Italian');
INSERT INTO Recipe (name, cuisine) VALUES ('Tacos', 'Mexican');
INSERT INTO Recipe (name, cuisine) VALUES ('Sushi', 'Japanese');

-- Ingredient
INSERT INTO Ingredient (name, quantity, unit) VALUES ('Pasta', 200, 'g');
INSERT INTO Ingredient (name, quantity, unit) VALUES ('Tomato Sauce', 1, 'cup');
INSERT INTO Ingredient (name, quantity, unit) VALUES ('Tortilla', 4, 'pieces');
INSERT INTO Ingredient (name, quantity, unit) VALUES ('Chicken', 200, 'g');
INSERT INTO Ingredient (name, quantity, unit) VALUES ('Rice', 1, 'cup');
INSERT INTO Ingredient (name, quantity, unit) VALUES ('Fish', 100, 'g');


-- Insert mock data for Expense app
-- Users
-- Insert mock data for Personal Finance Management app
-- User
INSERT INTO User (username, email) VALUES ('JohnDoe', 'john@example.com');
INSERT INTO User (username, email) VALUES ('JaneDoe', 'jane@example.com');

-- Expense
INSERT INTO Expense (amount, category, date, userId) VALUES (200, 'Groceries', '2023-09-25', 1);
INSERT INTO Expense (amount, category, date, userId) VALUES (50, 'Entertainment', '2023-09-20', 1);
INSERT INTO Expense (amount, category, date, userId) VALUES (100, 'Utilities', '2023-09-22', 2);

-- Income
INSERT INTO Income (amount, source, date, userId) VALUES (2000, 'Salary', '2023-09-25', 1);
INSERT INTO Income (amount, source, date, userId) VALUES (1500, 'Salary', '2023-09-20', 2);


