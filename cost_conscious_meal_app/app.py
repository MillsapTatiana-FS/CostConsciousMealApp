import streamlit as st
import pandas as pd
from nrf_engine import NRFEngine

st.title("Nutritional Cost-Conscious Meal App — Week 1 Prototype")

# Load data
df = pd.read_csv("data/sample_items.csv")

engine = NRFEngine()

# Compute scores
df["nrf_raw"] = df.apply(engine.compute_nrf_score, axis=1)
df["stars"] = df["nrf_raw"].apply(engine.normalize_score)
df["health_per_penny"] = df["nrf_raw"] / df["price"]

# Display
st.subheader("Item Rankings")
st.dataframe(df[["item", "store", "price", "nrf_raw", "stars", "health_per_penny"]])
