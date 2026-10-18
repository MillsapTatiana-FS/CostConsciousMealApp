import streamlit as st
from store_simulation import load_store_data, get_store_items
from meal_mapping import get_ingredients

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
