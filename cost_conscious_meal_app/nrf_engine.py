import pandas as pd

class NRFEngine:
    def __init__(self):
        # Beneficial nutrients (NRF9)
        self.good_nutrients = ["protein", "fiber", "vitamin_c", "calcium"]
        
        # Limiting nutrients (NRF3)
        self.bad_nutrients = ["sugar", "sodium", "saturated_fat"]

    def compute_nrf_score(self, row):
        good_sum = sum([row[n] for n in self.good_nutrients])
        bad_sum = sum([row[n] for n in self.bad_nutrients])
        raw_score = good_sum - bad_sum
        return raw_score

    def normalize_score(self, raw_score):
        # Simple normalization to 1–5 stars
        if raw_score <= -10:
            return 1
        elif raw_score <= 0:
            return 2
        elif raw_score <= 10:
            return 3
        elif raw_score <= 20:
            return 4
        else:
            return 5
