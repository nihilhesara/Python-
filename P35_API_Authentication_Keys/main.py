import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "58f83b5a48ee141fb8a923235d729c17"
# https://api.openweathermap.org/data/2.5/weather?q=Colombo&appid=58f83b5a48ee141fb8a923235d729c17

weather_param = {
    "lat":6.9319,
    "lon":79.8478,
    "appid": api_key,
}

response = requests.get(OWM_ENDPOINT,params=weather_param)
print(response.json())