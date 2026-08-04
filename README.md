#  House Price Prediction Project

**Project Team:**
- [Arwa Essam Ramadan Al_Ayouti]
- [Aya Gamal Talaat Gamal Ragab]

#  Project Overview
This project is an end-to-end Machine Learning web application that predicts house prices in India based on carpet area, floor number, and location.

We cleaned the dataset, trained regression models, built a backend REST API using **FastAPI**, and created an interactive web interface using **HTML/CSS/JS** for real-time predictions.


##  Tech Stack

- **Machine Learning & Data:** Python, Pandas, NumPy, Scikit-learn, Joblib
- **Backend API:** FastAPI, Uvicorn, Pydantic
- **Frontend UI:** HTML5, CSS3, JavaScript (Fetch API)


##  Dataset & Model Performance

- **Dataset:** `house_prices.csv`
- **Features Used:** `carpet_area_sqft`, `floor_num`, `location_grouped`
- **Models Evaluated:**
  1. Linear Regression
  2. **Random Forest Regressor** *(Selected as the best model and saved)*


## Project Structure

```text
house-price-project/
├── backend/
│   ├── models/
│   │   ├── house_price_model.pkl
│   │   └── metadata.json
│   └── main.py
├── frontend/
│   └── index.html
├── notebooks/
│   ├── data/
│   └── house_price_model.ipynb
├── .gitignore
└── README.md

How to Run the Project Locally
1. Run the Backend
Navigate to the backend directory and start the server:
1-cd backend
2-python -m uvicorn main:app --reload



2. Run the Frontend
Open frontend/index.html directly in any web browser to test the application.