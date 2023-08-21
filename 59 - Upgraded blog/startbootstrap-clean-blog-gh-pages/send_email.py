import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os

import yagmail

GMAIL_USERNAME = "pythondevelopcode@gmail.com"
GMAIL_PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT= 587

def send_mail_gmail(subject, msg_body):

    # Crear una instancia de yagmail y enviar el correo electrónico
    yag = yagmail.SMTP(GMAIL_USERNAME, GMAIL_PASSWORD)
    yag.send(to='brianfortuna95@gmail.com', subject=subject, contents=msg_body)

send_mail_gmail("ASUNTO", "BODY")
