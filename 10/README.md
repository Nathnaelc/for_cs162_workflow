![ER Diagram of Recipe app](https://mermaid.ink/img/pako:eNqVU8FqwzAM_RXjc_sDOa-HMAZlY7fAELaaisVyJ9uw0Pbf56bBy9ItrBcj3pOf9GT5qI23qCuN8kDQCriGlXoNKOp4iZQiq7ZCDqR_e8T-iqXMMzhUIQpxewXRAXUT5Hw5Np8H5IBLYuB84qh2nYd4RQxEbL30P-RtBofju4XaKuJYatVsvLuzVPBJDN5Z6BkNHRYL3QzHJArEOB9Pza2gJcxN3aP2kYAjxX7qJDHFufwTQrftgJfEZ3Zl8Par4f81OxVQY1q5ONMd9ux0Wq_9sWxKpfYQ5uT4tIUbX2Bki80_-Jv2S94EW8zVK-1Q8oLb_FUG842Oe3TY6CqHFuS90Q2fcx6k6F96NrqKknCl0-Ey3PFz6WoHXSjoxlL0MoLnL4ClMVE)

The ER diagram for the Recipe Recommendation and Meal Planning App consists of four tables: Recipe, Ingredient, MealPlan, and RecipeIngredient. The Recipe table is connected to both the MealPlan and RecipeIngredient tables through one-to-many relationships. The Ingredient table is also connected to the RecipeIngredient table through a one-to-many relationship

[![ER Diagram of Expense tracker app](https://mermaid.ink/img/pako:eNqVUcuqQjEM_JWQtf5A13pB3AjirpvQxmPxtJW0hSvH8-_2PPAFwr2bkMyUzGTaoYmWUSHLylEj5HUAOCQW6IYOwFlwIcNuO42lUoE8Q8riQjOB7Mm1L0g_lPXvhUPiL3vIx1LHYxspT4ihzE2U69tmW8GxPNU306Kf7UNpE0z0fxdKsYjh_8uMqdxuy2XsHscpOFH6JGc_M4cL9Cw1IVtjHj1qzCf2rFHV1pKcNerQ13dUctxfg0GVpfACy2XwNH8MqiO1ifs7V1aOYg?type=png)](https://mermaid.live/edit#pako:eNqVUcuqQjEM_JWQtf5A13pB3AjirpvQxmPxtJW0hSvH8-_2PPAFwr2bkMyUzGTaoYmWUSHLylEj5HUAOCQW6IYOwFlwIcNuO42lUoE8Q8riQjOB7Mm1L0g_lPXvhUPiL3vIx1LHYxspT4ihzE2U69tmW8GxPNU306Kf7UNpE0z0fxdKsYjh_8uMqdxuy2XsHscpOFH6JGc_M4cL9Cw1IVtjHj1qzCf2rFHV1pKcNerQ13dUctxfg0GVpfACy2XwNH8MqiO1ifs7V1aOYg)

The ER diagram for the Personal Finance Management App consists of three tables: User, Expense, and Income. The User table is connected to both the Expense and Income tables through one-to-many relationships. This means that a single user can have multiple expenses and incomes but each expense or income is associated with only one user.

Personal Finance Management App Schema

Tables:

    User
        id: Primary key uniquely identifying each user.
        username: String The name chosen by the user.
        email: String

    Expense
        id: Primary key     uniquely identifying each expense entry.
        amount: Float       The amount of money spent.
        category: String    The category of the expense (e.g., Food, Rent).
        date: Date          The date the expense occurred.
        userId: Foreign key references User.id      Foreign key referencing User.id, indicating which user the income belongs to.

    Income
        id: Primary key
        amount: Float
        source: String
        date: Date
        userId: Foreign key references User.id

Questions:

    What is the total monthly expenditure for a user?
    Relevant because it helps the user budget and manage their finances.
    What is the total monthly income for a user?
    Relevant for understanding how much the user earns and can spend.
    What is the most common expense category?

    Helps the user identify where they are spending the most.

Recipe Recommendation and Meal Planning App Schema
Tables:

    Recipe

        id: Primary key uniquely identifying each recipe.
        name: String The name of the recipe.
        cuisine: String The type of cuisine the recipe belongs to.

    Ingredient

        id: Primary key Primary key uniquely identifying each ingredient.
        name: String The name of the ingredient.
        quantity: Float
        unit: String

    MealPlan

        id: Primary key
        date: Date
        recipeId: Foreign key references Recipe.id   Foreign key referencing Recipe.id, indicating which recipe is planned.

    RecipeIngredient

        id: Primary key
        recipeId: Foreign key references Recipe.id
        ingredientId: Foreign key references Ingredient.id.  Foreign key referencing Ingredient.id.

Questions:

    What are the recipes planned for the week?
    Helps the user know what they will be eating and what they need to prepare for.
    What ingredients are needed for a specific recipe?
    Helps the user know what to buy from the grocery store.
    What is the most frequently used ingredient in the meal plans?

    Helps the user understand what ingredients they should always have in stock.
