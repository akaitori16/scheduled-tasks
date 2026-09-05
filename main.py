import requests
import os

api_key = os.environ.get("API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
bot_id = os.environ.get("BOT_ID")

parameters = {
    "lat": 33.9528,
    "lon": -84.5499,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()

def rain_expected():
    for i in range(0,4):
        cond_code = data["list"][i]["weather"][0]["id"]
        if int(cond_code) < 700:
            return True
    return False


if rain_expected():
    message = "It will rain today. It would be advisable to remain indoors."
    url = f"https://api.telegram.org/{bot_id}/sendMessage?chat_id=8976361824&text={message}"
    r = requests.get(url=url)
    r.raise_for_status()
    d = r.json()

if not rain_expected():
    message = "It will not rain today. Brainstorm excuses to not go anywhere."
    url = f"https://api.telegram.org/{bot_id}/sendMessage?chat_id=8976361824&text={message}"
    r = requests.get(url=url)
    r.raise_for_status()
    d = r.json()

if str(d["ok"]).lower() == "true":
    print("Message sent.")
