import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    "Hour": 19,
    "Temperature": 25,
    "Humidity": 20,
    "Wind_speed": 1.2,
    "Visibility": 2000,
    "Radiation": 0.0,
    "Rainfall": 0.0,
    "Snowfall": 0.0,
    "Day": 15,
    "Month": 6,
    "Week_day_Friday": 0,
    "Week_day_Monday": 0,
    "Week_day_Saturday": 0,
    "Week_day_Sunday": 0,
    "Week_day_Thursday": 0,
    "Week_day_Tuesday": 0,
    "Week_day_Wednesday": 1,
    "Holiday": 0
}

response = requests.post(url, json=data)
print(response.text)

#Sur un autre terminal, il faut entrer : python test.py