import os
from fastapi import FastAPI

v = os.environ.get("MODEL_VERSION", "v1.0.0")
app = FastAPI()


@app.get("/health")
def h():
    return {"status": "ok", "version": v}


@app.post("/predict")
def p(d: dict):
    return {"status": "ok", "version": v, "pred": 0}
