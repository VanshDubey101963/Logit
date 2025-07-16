from fastapi import FastAPI
from model import Dummy
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from ml.model import logit_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def predict(x1,x2):
    prediction = logit_model.predict([[x1, x2]])
    return int(prediction[0][0])


@app.get("/")
def main():
    return "Hello World"

@app.post("/")
def main(dummy: Dummy):
    x1 = dummy.x1
    x2 = dummy.x2

    prediction = predict(x1,x2)

    return {
        "prediction": prediction
    }


if __name__ == "__main__":
    run(app=app,host="127.0.0.1", port=5000)