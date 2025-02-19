from lib.recipe import Recipe

"""
Class instantiates with correct properties
"""
def test_recipe_class_instatiates_correctly():
    recipe = Recipe(1, "Test recipe", 100, 4)
    assert isinstance(recipe, Recipe)
    assert recipe.id == 1
    assert recipe.name == "Test recipe"
    assert recipe.average_cooking_time == 100
    assert recipe.rating == 4

"""
Recipes are represented nicely as strings
"""
def test_recipe_string_representation():
    recipe = Recipe(1, "Test recipe", 100, 4)
    assert str(recipe) == "Recipe(1, Test recipe, 100, 4)"

"""
Recipes with identical properties
Are compared as equal
"""
def test_recipes_equal_if_properties_identical():
    recipe1 = Recipe(1, "Test recipe", 100, 4)
    recipe2 = Recipe(1, "Test recipe", 100, 4)
    assert recipe1 == recipe2

