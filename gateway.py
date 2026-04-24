from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

with open('services.json') as f:
    services = json.load(f)

@app.get("/validate/{field}")
def validate(field: str):
    url = f"{services['validation']}/validate/{field}"
    resp = requests.post(url, json={"field": field})
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()

@app.post("/etl/run")
def run_etl():
    url = f"{services['etl']}/run"
    resp = requests.post(url)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()

@app.post("/automation/backup")
def run_backup():
    url = f"{services['automation']}/backup"
    resp = requests.post(url)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()