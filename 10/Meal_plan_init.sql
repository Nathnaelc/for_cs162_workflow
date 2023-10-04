-- Recipe Recommendation and Meal Planning App
-- Create tables
CREATE TABLE Recipe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cuisine TEXT NOT NULL
);

CREATE TABLE Ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit TEXT NOT NULL
);

CREATE TABLE MealPlan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    recipeId INTEGER,
    FOREIGN KEY (recipeId) REFERENCES Recipe(id)
);

CREATE TABLE RecipeIngredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipeId INTEGER,
    ingredientId INTEGER,
    FOREIGN KEY (recipeId) REFERENCES Recipe(id),
    FOREIGN KEY (ingredientId) REFERENCES Ingredient(id)
);

