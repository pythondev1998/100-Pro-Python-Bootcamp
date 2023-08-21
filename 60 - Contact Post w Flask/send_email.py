from flask import Flask, render_template, request
from email.message import EmailMessage
import ssl, smtplib

app = Flask(__name__)

MY_EMAIL = "pythondevelopcode@gmail.com"
MY_PASSWORD = "" 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/send', methods=["POST"])
def send_data():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    email_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    em = EmailMessage()
    em["From"] = MY_EMAIL
    em["To"] = email
    em["Subject"] = "Test"
    em.set_content(email_content)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
            smtp.login(MY_EMAIL, MY_PASSWORD)
            smtp.sendmail(MY_EMAIL, email, em.as_string())

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
