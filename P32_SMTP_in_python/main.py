import smtplib
import datetime as dt
import random
import os

EMAIL = "hi@gmail.com"
PASSWORD = "123@abc"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Monday motivation\n\n{quote}")
