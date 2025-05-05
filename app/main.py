from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os


# Load the model
current_path = os.path.dirname(__file__)
model_path = os.path.join(current_path, "..", "models", "prediction_model.pkl")
model = joblib.load(model_path)

app = FastAPI()

# Request schema
class StudyData(BaseModel):
    hours: float

# Prediction endpoint
@app.post("/predict")
def predict_score(data: StudyData):
    hours = [[data.hours]]  # Reshape input
    prediction = model.predict(hours)[0]
    return {"predicted_score": round(prediction, 2)}
