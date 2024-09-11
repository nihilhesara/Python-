import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "58f83b5a48ee141fb8a923235d729c17"
# https://api.openweathermap.org/data/2.5/weather?q=Colombo&appid=58f83b5a48ee141fb8a923235d729c17
# https://api.openweathermap.org/data/2.5/forecast?lat=6.9319&lon=79.8478&appid=58f83b5a48ee141fb8a923235d729c17

weather_param = {
    "lat":6.9319,
    "lon":79.8478,
    "appid": api_key,
    "cnt":4,
}

response = requests.get(OWM_ENDPOINT,params=weather_param)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")