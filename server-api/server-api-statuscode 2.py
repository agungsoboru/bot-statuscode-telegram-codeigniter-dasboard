#!/usr/bin/env python3
import random
from fastapi import FastAPI
import requests
import subprocess

app = FastAPI()

@app.get("/status/{domain}/")
def status_code(domain):
    return {"status code": requests.get(f"https://{domain}").status_code}

@app.get("/api/")
def api():
    phrases = ["API is online and running smoothly","All systems are operational","API is responding normally","API is available and healthy","API connectivity is confirmed","API is up and running","API is accessible and performing well","API is functioning as expected","API is accessible and responding","API is reachable and operational"]

    return (random.choice(phrases))


@app.get("/tmux")
def tmux():
    capture = subprocess.run(["tmux", "capture-pane", "-t", "0"], capture_output=True, text=True)
    show = subprocess.run(["tmux", "show-buffer"], capture_output=True, text=True)
    return show.stdout
