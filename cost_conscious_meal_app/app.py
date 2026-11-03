import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from store_simulation import load_store_data, get_store_items
from meal_mapping import get_ingredients
from shopping_simulation import (
    generate_manual_basket,
    generate_app_basket,
    summarize_basket,
    compare_baskets
)

st.title("Nutritional Cost-Conscious Meal App")

# Load full dataset
df = load_store_data()

st.subheader("Star-Rated Grocery Items Across All Stores")

stores = df["store"].unique()
selected_store = st.selectbox("Choose a store:", stores)

store_df = get_store_items(selected_store)

st.write(f"Items at {selected_store}")
st.dataframe(store_df[["item", "price", "star_rating", "health_per_penny"]])

# Meal Mapping Section
st.subheader("Ingredient Mapping for Staple Meals")

meal = st.selectbox("Choose a meal:", ["Bean Tacos", "Vegetable Pasta", "Egg Protein Bowl"])
ingredients = get_ingredients(meal)

meal_items = []

for ingredient in ingredients:
    matches = df[
        df["item"].str.contains(
            ingredient,
            case=False,
            na=False
        )
    ]
    meal_items.append(matches)

meal_df = pd.concat(meal_items)

st.write(f"Ingredients for {meal}")
st.dataframe(meal_df[["item", "price", "star_rating", "health_per_penny"]])

st.success("Functionality loaded successfully!")

st.header("Comparative Shopping Simulation")

# Generate baskets

manual_df = generate_manual_basket()
app_df = generate_app_basket()

comparison = compare_baskets(
    manual_df,
    app_df
)
st.subheader("Basket Comparison")

comparison_df = pd.DataFrame({
    "Metric": [
        "Cost",
        "NRF Score"
    ],
    "Manual Basket": [
        comparison["manual_cost"],
        comparison["manual_score"]
    ],
    "App Basket": [
        comparison["app_cost"],
        comparison["app_score"]
    ]
})

st.table(comparison_df)


st.subheader("NRF Score Comparison")

fig, ax = plt.subplots(figsize=(8,4))

scores = [
    comparison["manual_score"],
    comparison["app_score"]
]

labels = [
    "Manual Basket",
    "App Basket"
]

ax.bar(labels, scores)

ax.set_ylabel("NRF Score")
ax.set_title("Manual vs App-Assisted Shopping")

st.pyplot(fig)

# Summaries
manual_summary = summarize_basket(manual_df)
app_summary = summarize_basket(app_df)
comparison = compare_baskets(manual_df, app_df)

st.write("Comparison Dictionary:")
st.write(comparison)

st.subheader("Detailed Metrics")

st.write(f"Manual Basket Cost: ${comparison['manual_cost']:.2f}")
st.write(f"App Basket Cost: ${comparison['app_cost']:.2f}")
st.write(f"Cost Difference: {comparison['cost_difference_percent']:.2f}%")

st.write(f"Manual NRF Score: {comparison['manual_score']:.2f}")
st.write(f"App NRF Score: {comparison['app_score']:.2f}")
st.write(f"Nutritional Improvement: {comparison['improvement_percent']:.2f}%")
