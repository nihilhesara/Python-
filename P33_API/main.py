import requests # pip install requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code) # To get only the status code

response.raise_for_status() # raise a exception with the error code

# If API runs correctlyit gives a json output like below
data = response.json()
print(data)

# To print only the longitude using json
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)
print(iss_position) # using this iss_position we can see where is the iss right now in a world map using the website link below
                    # https://www.latlong.net/
                    
# API response code types (https://www.webfx.com/web-development/glossary/http-status-codes/)

# 1XX: Hold on 
# 2XX: Here you go (good stage)
# 3XX: Go away
# 4XX: You screwed up
# 5XX: I screwed up (Server)