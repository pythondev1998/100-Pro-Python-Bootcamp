from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)
year = datetime.datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", year=year)

@app.route('/guess/<string:name>')
def guess(name):
    # Obtener género
    url_gender = f"https://api.genderize.io/?name={name}"
    json_gender = requests.get(url_gender).json()
    gender = json_gender.get('gender')
    print(gender)

    # Obtener edad
    url_age= f"https://api.agify.io/?name={name}"
    json_age = requests.get(url_age).json()
    age = json_age.get('age')
    print(age)

    return render_template("guess.html", name=name, gender=gender, age=age, year=year)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
