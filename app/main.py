from fastapi import FastAPI
from app.predict import make_prediction
from app.schemas import CarFeatures
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "API IS RUNNING HERE........."}


@app.get("/home")
def welcome():
    return {"message": "Welcome to Used Car Prediction"}


print("you are running the correct main.py!")


@app.post("/predict")
def predict_price(data: CarFeatures):
    input_dict = data.model_dump()
    result = make_prediction(input_dict)
    print("running")
    return {"Predicted Car Price": float(result['predicted_price']),
            "Confidence Range": f"${float(result['confidence_range'][0])} - ${float(result['confidence_range'][1])}"
            }
