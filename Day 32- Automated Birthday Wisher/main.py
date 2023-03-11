##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import os
import random

SENDER_EMAIL= "********@gmail.com"
SENDER_PASSWORD ="****************"

#------------------- Check if today matches a birthday in the birthdays.csv------------------------

todays_date = dt.datetime.now()
todays_day =todays_date.day
todays_month = todays_date.month
# print(todays_month)

with open("birthdays.csv") as file:
    birthdays = pandas.read_csv(file)
    dict = {(data["month"],data["day"]): data for (index,data) in birthdays.iterrows() }
    print(dict)
    # name_list = birthdays.query("month == 3 & day == 11")["name"].to_list()
    # email_list= birthdays.query("month == 3 & day == 11")["email"].to_list()

    name_email_dict = birthdays.query(f"month == {todays_month} & day == {todays_day}").get(["name","email"]).to_dict()

#--------------------Check if there are any bithdays today---------------------------------------------
    if name_email_dict["name"] == {}:
        print("No Birthdays")
    else:
        # putting all the letter files in a list
        files_list = os.listdir("letter_templates")
        with open(f"letter_templates/{random.choice(files_list)}", mode="r") as letter_file:
            letter = letter_file.read()
            for index in range(0,len(name_email_dict)+1):
                # print(index)
                # print(name_email_dict['email'][index])

                customized_letter =letter.replace("[NAME]",f"{name_email_dict['name'][index]}")

                #Send birthday email
                with smtplib.SMTP("smtp.gmail.com",587) as connection:
                    connection.starttls()
                    connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
                    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs= f"{name_email_dict['email'][index]}",
                                        msg=f"Subject:Happy Birthday!\n\n{customized_letter}")
