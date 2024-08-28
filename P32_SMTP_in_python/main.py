import smtplib

my_email = "abc@gmail.com"
password = "123@abc"

# to do this we have to create a password from google accounts 
with smtplib.SMTP("smtp.gmail.com") as connection: # each email type has a deferent smtp type search for it and put it in the ()
    connection.starttls()   # Encript the message (secure the connection)
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addr="xyz@gmail.com", msg="Subject:This is subject \n\n Hello")
    # In msg Subject is This is subject and the mail body is hello
    connection.close()