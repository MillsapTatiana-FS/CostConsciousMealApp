import pandas as pd
from store_simulation import load_store_data
from meal_mapping import get_ingredients

# Manual basket: chooses the cheapest item for each ingredient
def generate_manual_basket():
    df = load_store_data()
    basket_items = []

    for meal in ["Bean Tacos", "Vegetable Pasta", "Egg Protein Bowl"]:
        ingredients = get_ingredients(meal)
        for ingredient in ingredients:
            item_df = df[df["item"] == ingredient]
            if not item_df.empty:
                cheapest = item_df.sort_values("price").iloc[0]
                basket_items.append(cheapest)

    manual_df = pd.DataFrame(basket_items)
    return manual_df


# App-assisted basket: chooses highest star rating, then best health-per-penny
def generate_app_basket():
    df = load_store_data()
    basket_items = []

    for meal in ["Bean Tacos", "Vegetable Pasta", "Egg Protein Bowl"]:
        ingredients = get_ingredients(meal)
        for ingredient in ingredients:
            item_df = df[df["item"] == ingredient]
            if not item_df.empty:
                best_item = (
                    item_df.sort_values(
                        ["star_rating", "health_per_penny"],
                        ascending=[False, False]
                    ).iloc[0]
                )
                basket_items.append(best_item)

    app_df = pd.DataFrame(basket_items)
    return app_df


# Summary calculations for Week 3 dataset
def summarize_basket(df):
    return {
        "total_cost": df["price"].sum(),
        "total_nrf_score": df["nrf_score"].sum(),
        "average_star_rating": df["star_rating"].mean()
    }
