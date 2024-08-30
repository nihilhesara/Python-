import requests  # Import the requests module to make HTTP requests
from datetime import datetime  # Import datetime for handling date and time
import smtplib  # Import smtplib to handle sending emails
import time  # Import time for adding delays in the loop

# Set your latitude and longitude
MY_LAT = 51.507351  # Your latitude (example: London)
MY_LONG = -0.127758  # Your longitude (example: London)
# Set your email and password for sending notifications
MY_EMAIL = "YOUR EMAIL"  # Your email address
MY_PASSWORD = "YOUR PASSWORD"  # Your email password

def is_iss_overhead():
    # Function to check if the ISS is currently overhead

    # Make a request to the ISS location API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()  # Parse the response as JSON

    # Extract the ISS latitude and longitude from the API response
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if the ISS is within +5 or -5 degrees of your position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True  # Return True if the ISS is overhead

def is_night():
    # Function to check if it's currently night time at your location

    # Define the parameters for the sunrise-sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # Get the time in ISO 8601 format
    }

    # Make a request to the sunrise-sunset API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()  # Parse the response as JSON

    # Extract sunrise and sunset times from the API response
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour in your local time
    time_now = datetime.now().hour

    # Check if the current time is before sunrise or after sunset
    if time_now >= sunset or time_now <= sunrise:
        return True  # Return True if it's night time

# Continuous loop to check the ISS position and time of day
while True:
    time.sleep(60)  # Wait for 60 seconds before checking again
    if is_iss_overhead() and is_night():  # If the ISS is overhead and it's night time
        # Set up the email server and send the notification email
        connection = smtplib.SMTP("smtp.gmail.com")  # Connect to the Gmail SMTP server
        connection.starttls()  # Secure the connection with TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD)  # Log in to your email account
        connection.sendmail(
            from_addr=MY_EMAIL,  # Your email address
            to_addrs=MY_EMAIL,  # Send the email to yourself
            msg="Subject:Look up\n\nThe ISS is above you in the sky."  # Email subject and body
        )
