from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes.sql")

# Retrieve all recipes
repository = RecipeRepository(connection)
recipes = repository.all()

# Print them out
for recipe in recipes:
    print(recipe)
