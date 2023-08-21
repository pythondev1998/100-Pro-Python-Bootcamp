from flask import Flask, render_template, request
import requests, smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)

MY_EMAIL = "pythondevelopcode@gmail.com"
MY_PASSWORD = "" 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def get_blog_data():
    npoint_api_endpoint = 'https://api.npoint.io/eb975062e4a520acb7cb'
    response = requests.get(url=npoint_api_endpoint)
    response.raise_for_status()
    return response.json()


@app.route('/')
@app.route('/home')
def home():
    blogs = get_blog_data()
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<blog_id>')
def post(blog_id):
    blogs = get_blog_data()
    id_int = int(blog_id) - 1
    return render_template("post.html", blog=blogs[id_int])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(data):

    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]
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
    


if __name__ == '__main__':
    app.run(debug=True)

