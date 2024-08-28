# import smtplib

# my_email = "abc@gmail.com"
# password = "123@abc"

# # to do this we have to create a password from google accounts 
# with smtplib.SMTP("smtp.gmail.com") as connection: # each email type has a deferent smtp type search for it and put it in the ()
#     connection.starttls()   # Encript the message (secure the connection)
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addr="xyz@gmail.com", msg="Subject:This is subject \n\n Hello")
#     # In msg Subject is This is subject and the mail body is hello
#     connection.close()

#____________________________________________________________________________________________________________________________

import datetime as dt

now = dt.datetime.now()   # get the current date and time
print(now)
year = now.year
print(year) # there is hour month date everrything as a method ex:- .month
day_of_the_week = now.weekday() # this print 0 for monday and so on
print(day_of_the_week)

date_of_birth = dt.datetime(year=2003, month=8, day=6)
print(date_of_birth)