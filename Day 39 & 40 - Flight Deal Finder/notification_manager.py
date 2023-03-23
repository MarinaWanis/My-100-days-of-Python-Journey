from twilio.rest import Client
import smtplib

sender_email= "marinacoding868@gmail.com"
sender_passowrd = "exzptbbyhkeaxmpt"

class NotificationManager:
    def __init__(self, text):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = "AC9c9da3a062b68035d62897b91f2a43cd"
        auth_token = "cbef068d444920a4ce6c58a27ec246f4"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=text,
            to='whatsapp:+971508964120'
        )
        print(message.status)

    def sendEmail(self, to_email, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_passowrd)
            connection.sendmail(from_addr=sender_email,to_addrs=to_email,msg=message)
