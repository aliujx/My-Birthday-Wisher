import datetime as dt
import pandas as pd
from random import choice
import smtplib
import config

today = dt.datetime.today()
today_month = today.month
today_day = today.day

birthdays = pd.read_csv("birthdays.csv")
pd.DataFrame(birthdays)
birthdays_dict = birthdays.to_dict(orient="records")

letters_to_send = ["letter_templates\letter_1.txt", "letter_templates\letter_2.txt", "letter_templates\letter_3.txt"]
for date in birthdays_dict:
    if date["month"] == today_month and date["day"] == today_day:
        with open(choice(letters_to_send)) as letter:
            to_send = letter.read().replace("[NAME]", date["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=config.my_email, password=config.password)
            connection.sendmail(
                from_addr=config.my_email,
                to_addrs=date["email"],
                msg=f"Subject:Happy Birthday!\n\n{to_send}"
            )
