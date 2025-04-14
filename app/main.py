from fastapi import FastAPI

from app.predict import make_prediction
from app.schemas import CarFeatures

app = FastAPI(title="Used Car Price Prediction")


@app.get("/")
def root():
    return {"message": "API IS RUNNING........."}


@app.get('/home')
def welcome():
    return {"message": "Welcome to Used Car Prediction"}


@app.post('/predict')
def predict_price(data: CarFeatures):
    input_dict = data.model_dump()
    price = make_prediction(input_dict)
    print("running")
    return {"Predicted Car Price": price}
