from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('/app/models/california_housing_model.joblib')

class Features(BaseModel):
    features: list

@app.post("/predict/")
def predict(data: Features):
    try:
        prediction = model.predict(np.array(data.features).reshape(1, -1))
        return {"prediction": prediction[0]}
    except Exception as e:
        return {"error": str(e)}
