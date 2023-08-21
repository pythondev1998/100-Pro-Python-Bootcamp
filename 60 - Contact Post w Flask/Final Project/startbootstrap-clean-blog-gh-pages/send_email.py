from flask import Flask, render_template, request
from email.message import EmailMessage
import ssl, smtplib

app = Flask(__name__)

MY_EMAIL = "pythondevelopcode@gmail.com"
MY_PASSWORD = "" 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)

