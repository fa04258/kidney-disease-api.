
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import joblib
import pandas as pd
from pathlib import Path

# Load the trained ML model
MODEL_FILE = Path(__file__).parent / "kidney_disease_model.pkl"
model = joblib.load(MODEL_FILE)

# Create FastAPI application
app = FastAPI(
    title="Kidney Disease Prediction API",
    description="ML model serving API for MLOps demonstration",
    version="1.0.0"
)

# Input schema
class KidneyDiseaseInput(BaseModel):
    age: Optional[float] = None
    bp: Optional[float] = None
    sg: Optional[float] = None
    al: Optional[float] = None
    su: Optional[float] = None
    rbc: Optional[str] = None
    pc: Optional[str] = None
    pcc: Optional[str] = None
    ba: Optional[str] = None
    bgr: Optional[float] = None
    bu: Optional[float] = None
    sc: Optional[float] = None
    sod: Optional[float] = None
    pot: Optional[float] = None
    hemo: Optional[float] = None
    pcv: Optional[str] = None
    wc: Optional[str] = None
    rc: Optional[str] = None
    htn: Optional[str] = None
    dm: Optional[str] = None
    cad: Optional[str] = None
    appet: Optional[str] = None
    pe: Optional[str] = None
    ane: Optional[str] = None

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Kidney Disease ML API is running",
        "version": "1.0.0"
    }

# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }

# Prediction endpoint
@app.post("/predict")
def predict(data: KidneyDiseaseInput):
    input_data = data.model_dump()
    input_df = pd.DataFrame([input_data])

    # Match the features used during model training
    input_df = input_df.reindex(
        columns=model.feature_names_in_,
        fill_value=None
    )

    prediction = model.predict(input_df)

    return {
        "prediction": str(prediction[0])
    }
