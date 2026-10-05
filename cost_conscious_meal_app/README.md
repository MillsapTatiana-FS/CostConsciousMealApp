# CostConsciousMealApp

Nutritional Cost‑Conscious Meal App (Week 1 Prototype)
This project is the first implementation stage of the Nutritional Cost‑Conscious Meal App, developed for the Human–Computer Interaction course at Full Sail University. The goal of the app is to help families identify affordable, nutrient‑dense grocery items using the NRF9.3 nutritional scoring model and real‑world pricing. By automating the “health‑per‑penny” calculation, the system aims to reduce cognitive load and make healthier shopping decisions more accessible.

This Week‑1 prototype demonstrates the core functionality of the NRF9.3 scoring engine and a simple interface for viewing item rankings across multiple store types.

---

Week 1 Deliverables
This prototype includes:

A functional NRF9.3 scoring engine

A small dataset of grocery items from multiple store types

A simple Streamlit interface that displays:

Item name

Store

Price

Raw NRF9.3 score

Normalized 1–5 star rating

Health‑per‑penny value

A clean project structure ready for expansion in Week 2

---

Project Structure
cost_conscious_meal_app/
│
├── data/
│   └── sample_items.csv
│
├── nrf_engine.py
├── app.py
└── README.md

---

Installation

1. Clone the repository:
   git clone https://github.com/<your-username>/cost_conscious_meal_app.git

2. Navigate into the project folder:
cd cost_conscious_meal_app

3. Install Dependencies:
pip install streamlit pandas numpy

---

Running the Prototype

Launch the Streamlit interface:
streamlit run app.py

This will open a browser window displaying the Week‑1 prototype, including NRF9.3 scores, star ratings, and health‑per‑penny values for each item.

---

About the NRF9.3 Model

NRF9.3 is a scientifically validated nutritional scoring system that evaluates foods based on:

Beneficial nutrients (protein, fiber, vitamin C, calcium)

Limiting nutrients (sugar, sodium, saturated fat)

The app calculates a raw score and converts it into a simplified 1–5 star rating to reduce cognitive load and support quick decision‑making.