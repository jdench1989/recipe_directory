from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

"""
When calling the all() method
A list containing Recipe objects representing each row is returned
"""
def test_repository_all_method(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.all()
    assert result == [
        Recipe(1, 'Lasagna', 60, 5),
        Recipe(2, 'Spaghetti Carbonara', 30, 4),
        Recipe(3, 'Chicken Curry', 45, 5),
        Recipe(4, 'Beef Stew', 120, 4),
        Recipe(5, 'Vegetable Stir Fry', 20, 3),
        Recipe(6, 'Tacos', 25, 4),
        Recipe(7, 'Grilled Cheese Sandwich', 10, 3),
        Recipe(8, 'Caesar Salad', 15, 4),
        Recipe(9, 'Pancakes', 20, 5),
        Recipe(10, 'Chocolate Cake', 90, 5),
    ]

"""
When calling the find() method with a given recipe id
Returns only a single instance of Recipe mathcing that id
"""
def test_find_method_returns_single_correct_instance(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.find(1)
    assert result == Recipe(1, 'Lasagna', 60, 5)