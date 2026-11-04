meal_ingredients = {
    "Bean Tacos": [
        "Black Beans",
        "Tortillas",
        "Tomato Sauce",
        "Broccoli"
    ],
    "Vegetable Pasta": [
        "Pasta",
        "Tomato Sauce",
        "Broccoli"
    ],
    "Egg Protein Bowl": [
        "Eggs",
        "Spinach",
        "Tomatoes"
    ]
}

def get_ingredients(meal_name):
    return meal_ingredients.get(meal_name, [])