import streamlit as st
import pandas as pd
from nrf_engine import NRFEngine

st.title("Nutritional Cost-Conscious Meal App — Week 2 Expanded")

# Load full dataset
df = pd.read_csv("data/all_stores_items.csv")

engine = NRFEngine()

# Compute scores
df["nrf_raw"] = df.apply(engine.compute_nrf_score, axis=1)
df["stars"] = df["nrf_raw"].apply(engine.normalize_score)
df["health_per_penny"] = df["nrf_raw"] / df["price"]

# Store selector
store_choice = st.selectbox("Select a Store", df["store"].unique())

filtered = df[df["store"] == store_choice]

# Highlight nutritional winners
def highlight_row(row):
    if row["stars"] >= 4:
        return "background-color: #c8e6c9"  # green
    elif row["stars"] == 3:
        return "background-color: #fff9c4"  # yellow
    else:
        return "background-color: #ffcdd2"  # red

styled_table = filtered.style.apply(
    lambda row: [highlight_row(row)] * len(row),
    axis=1
)

st.subheader(f"Nutritional Rankings — {store_choice}")
st.dataframe(styled_table)

# Ingredient mapping for staple meals
st.subheader("Staple Meal Ingredient Mapping")

meals = {
    "Bean-Based Tacos": ["Black Beans (canned)", "Tortillas", "Spinach (bag)"],
    "Vegetable Pasta": ["Pasta", "Frozen Broccoli", "Tomato Sauce"],
    "Egg Protein Bowl": ["Eggs (dozen)", "Spinach (bag)", "Peanut Butter"]
}

meal_choice = st.selectbox("Select a Meal", meals.keys())

meal_items = df[df["item"].isin(meals[meal_choice])]

st.write(f"Ingredients for **{meal_choice}**:")
st.dataframe(meal_items[["item", "store", "price", "stars", "health_per_penny"]])
