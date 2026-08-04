from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import json
import os

app = FastAPI(title="House Price Prediction API")

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "house_price_model.pkl")
METADATA_PATH = os.path.join(BASE_DIR, "models", "metadata.json")

# Load Model & Metadata
try:
    model = joblib.load(MODEL_PATH)
    with open(METADATA_PATH, "r") as f:
        metadata = json.load(f)
except Exception as e:
    model = None
    metadata = {"locations": []}
    print(f"Error loading model/metadata: {e}")

class HouseInput(BaseModel):
    carpet_area_sqft: float
    floor_num: int
    location: str

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

@app.get("/locations")
def get_locations():
    return {"locations": metadata.get("locations", [])}

@app.post("/predict")
def predict_price(data: HouseInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded properly.")
    
    # Process location
    loc = data.location if data.location in metadata.get("locations", []) else "other"
    
    input_data = pd.DataFrame([{
        "carpet_area_sqft": data.carpet_area_sqft,
        "floor_num": data.floor_num,
        "location_grouped": loc
    }])
    
    try:
        prediction = model.predict(input_data)[0]
        return {
            "predicted_price": round(float(prediction), 2),
            "currency": "INR"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))