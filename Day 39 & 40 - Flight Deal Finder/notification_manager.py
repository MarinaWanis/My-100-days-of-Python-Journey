from twilio.rest import Client
import smtplib
import os

sender_email= os.environ['SENDER_EMAIL']
sender_passowrd = os.environ['SENDER_PASSWORD']

class NotificationManager:
    def __init__(self, text):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ["ACCOUNT_SID"]
        auth_token = os.environ["AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:*************',
            body=text,
            to='whatsapp:*************'
        )
        print(message.status)

    def sendEmail(self, to_email, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_passowrd)
            connection.sendmail(from_addr=sender_email,to_addrs=to_email,msg=message)
