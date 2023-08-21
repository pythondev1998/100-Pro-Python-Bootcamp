import smtplib
from twilio.rest import Client

MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""
smtp_server = "smtp.gmail.com"
smtp_port = 587

account_sid = "AC116c37b1987c3093664d726b1bbd2e3a"
auth_token = ""
client = Client(account_sid, auth_token)


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+12708133850",
            to="+1829721",
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
