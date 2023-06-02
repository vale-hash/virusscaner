import os
from dateutil.relativedelta import relativedelta
import requests
from flask import Flask, render_template

global url
url = "https://www.virustotal.com/api/v3/urls"

print('hello world')
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
global api_key
api_key = os.getenv("API_KEY")
app.secret_key = os.getenv("SECRET_KEY")


@app.route('/')
def check_url():
    payload = "url=google.com"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key,
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    return render_template('index.html')
