
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from typing import Literal


from transformers import CombinedAttributesAdder


model = joblib.load("models/model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

app = FastAPI(title="HESlegacy Housing API")

OCEAN_PROXIMITY = Literal["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]

class HouseInput(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: OCEAN_PROXIMITY



@app.post("/predict")
def predict(data: HouseInput):
    df = pd.DataFrame([data.dict()])
    X = preprocessor.transform(df)
    price = model.predict(X)[0]
    return {"predicted_price_usd": round(float(price), 2)}
