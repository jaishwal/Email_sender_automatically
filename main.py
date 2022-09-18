"""Project - Send Email Automatically
Author = Dheeraj Kumar
"""
# Liberaries
from datetime import datetime # built in module
import random   # built in module
import pandas  # pip install pandas
import smtplib # built in module

# users data
My_email = "dheerajjaiswal3333@gmail.com"
My_password = "abc1234()"
# present time
today = datetime.now()
today_tuple = (today.month, today.day)

# using pandas open csv file
data = pandas.read_csv("birthdays.csv")

# dictionary comprehension
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"  # using random module
    with open(file_path) as file_letter:
        contents = file_letter.read()
        contents = contents.replace(["Name"], birthday_person["Name"])  # replace with taker name

        # using smtplib liberary send mail
        #SMTP- Simple Mail Transfer Protocol
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(My_email, My_password)

        # Message for birthday person
        connection.sendmail(
            from_addr=My_email,
            to_addrs=birthday_person["email"],  # taker email stored in csv file
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
# if you have give some error then set your email privacy in less mode through the link in result section
# for more information please visit smtplib python doccumentation