from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact Me")
    else:
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        print(f'<h1>Successfully sent your message.</h1>'
              f'Name: {name}<br>'
              f'Email: {email}<br>'
              f'Phone: {phone}<br>'
              f'Message: {message}<br>')
        return render_template("contact.html", title="Successfully sent your message.")

if __name__ == '__main__':
    app.run()