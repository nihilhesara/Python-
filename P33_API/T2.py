import requests
import datetime

MY_LAT = 7.873054
MY_LNG = 80.771797  

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0  
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # Check for HTTP errors
data = response.json()  # Parse the response as JSON
print(data)  # Print the data

# Getting the sunrise and sunset data
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.datetime.now()
print(time_now.hour)