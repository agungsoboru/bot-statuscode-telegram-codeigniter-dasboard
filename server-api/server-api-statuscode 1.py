from fastapi import FastAPI
import requests
import json
from datetime import datetime
import random
import subprocess

current_time = datetime.now()
app = FastAPI()

@app.get("/status/{domain}/")
def status_code(domain):
    try:
        request = requests.get(f"https://{domain}").status_code
        if request == 200:
            return {"status code": request }
        else:
            re = requests.get(f"http://api.domain:11119/status/{domain}").json()

            data = re
            status_code2 = data.get('status code')
            #print(status_code2)
            print("Current Date and Time: ", current_time)
            print (re)

            return {"status code": status_code2 }
    except :
        return {"status code": "internall error" }




@app.get("/api/")
def api():
    phrases = ["API is online and running smoothly","All systems are operational","API is responding normally","API is available and healthy","API connectivity is confirmed","API is up and running","API is accessible and performing well","API is functioning as expected","API is accessible and responding","API is reachable and operational"]

    return (random.choice(phrases))





@app.get("/tmux")
def tmux():
    capture = subprocess.run(["tmux", "capture-pane", "-t", "1"], capture_output=True, text=True)
    show = subprocess.run(["tmux", "show-buffer"], capture_output=True, text=True)
    return show.stdout
