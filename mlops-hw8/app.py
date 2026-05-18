import os
import time
import random
from fastapi import FastAPI
from prometheus_client import Histogram, Counter, make_asgi_app

app = FastAPI()

LAT = Histogram("request_latency_seconds", "Request latency")
REQS = Counter("request_total", "Total requests", ["status"])

app.mount("/metrics", make_asgi_app())


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: dict):
    t0 = time.time()
    # типа делаем предсказание — иногда тормозим чтоб алерт сработал
    if os.environ.get("SLOW") == "1":
        time.sleep(2)
    else:
        time.sleep(random.uniform(0.05, 0.2))
    LAT.observe(time.time() - t0)
    REQS.labels(status="ok").inc()
    return {"pred": 0}
