from fastapi import FastAPI
import boto3
import json

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy", "version": "v1.0"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.post("/predict")
def predict(data: dict):
    return {"message": "prediction received", "input": data}
