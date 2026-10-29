import streamlit as st
from store_simulation import load_store_data, get_store_items
from meal_mapping import get_ingredients
from shopping_simulation import (
    generate_manual_basket,
    generate_app_basket,
    summarize_basket,
    compare_baskets
)

st.title("Nutritional Cost-Conscious Meal App — Week 2")

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

meal_df = df[df["item"].isin(ingredients)]

st.write(f"Ingredients for {meal}")
st.dataframe(meal_df[["item", "price", "star_rating", "health_per_penny"]])

st.success("Week 2 functionality loaded successfully!")

st.header("Week 3 — Comparative Shopping Simulation")

# Generate baskets

manual_df = generate_manual_basket()
app_df = generate_app_basket()

comparison = compare_baskets(manual_df, app_df)

# Summaries
manual_summary = summarize_basket(manual_df)
app_summary = summarize_basket(app_df)
comparison = compare_baskets(manual_df, app_df)

st.write("Comparison Dictionary:")
st.write(comparison)

st.subheader("Comparison Results")

st.write(f"Manual Basket Cost: ${comparison['manual_cost']:.2f}")
st.write(f"App Basket Cost: ${comparison['app_cost']:.2f}")
st.write(f"Cost Difference: {comparison['cost_difference_percent']:.2f}%")

st.write(f"Manual NRF Score: {comparison['manual_score']:.2f}")
st.write(f"App NRF Score: {comparison['app_score']:.2f}")
st.write(f"Nutritional Improvement: {comparison['improvement_percent']:.2f}%")
