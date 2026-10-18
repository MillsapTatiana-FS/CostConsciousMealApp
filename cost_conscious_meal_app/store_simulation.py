import pandas as pd
from nrf_engine import compute_nrf_score, convert_to_star_rating

def load_store_data():
    df = pd.read_csv("data/all_stores_items.csv")
    
    # Compute NRF9.3 score
    df["nrf_score"] = df.apply(compute_nrf_score, axis=1)
    
    # Convert to star rating
    df["star_rating"] = df["nrf_score"].apply(convert_to_star_rating)
    
    # Health per penny calculation
    df["health_per_penny"] = df["nrf_score"] / df["price"]
    
    return df

def get_store_items(store_name):