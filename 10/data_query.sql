-- FOR THE EXPENSE TRACKER APP

-- What is the total balance for a specific user?
-- Relevant because users need to know their total financial standing.

SELECT SUM(balance) FROM Accounts WHERE user_id = 1;


-- What are the latest 5 transactions for a specific account?
-- Relevant for users to track recent account activity.
SELECT * FROM Transactions WHERE account_id = 1 ORDER BY date DESC LIMIT 5;


-- What is the total income and expense for a specific account this month?
-- Relevant for budgeting and financial planning.
SELECT transaction_type, SUM(amount) FROM Transactions WHERE account_id = 1 AND strftime('%Y-%m', date) = '2023-09' GROUP BY transaction_type;


-- FOR THE RECIPE RECOMMENDATION AND MEAL PLANNING APP

-- 1. What are the recipes available for a specific user?
-- Relevant for users to quickly find their saved recipes.

SELECT recipe_name FROM Recipes WHERE user_id = 1;

-- 2. What ingredients are needed for a specific recipe?
-- Relevant for grocery shopping and meal preparation.

SELECT ingredient_name, quantity FROM Ingredients WHERE recipe_id = 1;


-- What are the different cuisines available in the recipes?
-- Relevant for users looking to try different types of food.

SELECT DISTINCT cuisine FROM Recipes;
