import smtplib  # Import the smtplib module to handle sending emails
import datetime as dt  # Import the datetime module for handling date and time
import random  # Import the random module to select a random quote
import os  # Import the os module for file and directory handling

# Email credentials
EMAIL = "hi@gmail.com"  # Your email address
PASSWORD = "123@abc"  # Your email password

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get the current date and time
now = dt.datetime.now()
weekday = now.weekday()  # Get the current day of the week (0 is Monday, 6 is Sunday)

# If it's Monday (weekday == 0), send a motivational quote via email
if weekday == 0:
    # Open the file containing quotes and read all lines
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()  # Read all quotes into a list
        quote = random.choice(all_quotes)  # Select a random quote from the list
    print(quote)  # Print the selected quote to the console (optional)

    # Set up the email server and send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection with TLS encryption
        connection.login(EMAIL, PASSWORD)  # Log in to your email account
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,  # Send the email to yourself
            msg=f"Subject:Monday motivation\n\n{quote}"  # Email subject and body
        )
