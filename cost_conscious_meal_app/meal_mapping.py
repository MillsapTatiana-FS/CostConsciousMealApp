meal_ingredients = {
    "Bean Tacos": [
        "Black Beans (canned)",
        "Tortillas (pack)",
        "Tomato Sauce",
        "Frozen Mixed Veggies"
    ],
    "Vegetable Pasta": [
        "Pasta",
        "Tomato Sauce",
        "Frozen Mixed Veggies"
    ],
    "Egg Protein Bowl": [
        "Eggs (dozen)",
        "Spinach (bag)",
        "Tomatoes"
    ]
}

def get_ingredients(meal_name):
    return meal_ingredients.get(meal_name, [])
