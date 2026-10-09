
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "age": 48,
    "bp": 80,
    "sg": 1.02,
    "al": 1,
    "su": 0,
    "rbc": "normal",
    "pc": "normal",
    "pcc": "notpresent",
    "ba": "notpresent",
    "bgr": 121,
    "bu": 36,
    "sc": 1.2,
    "sod": 138,
    "pot": 4.5,
    "hemo": 15.4,
    "pcv": "44",
    "wc": "7800",
    "rc": "5.2",
    "htn": "no",
    "dm": "no",
    "cad": "no",
    "appet": "good",
    "pe": "no",
    "ane": "no"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
