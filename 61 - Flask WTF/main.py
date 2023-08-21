from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.validators import Email as EmailValidator
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "a-secure-secret-key"  # Secret key for CSRF protection
Bootstrap(app)

class LoginForm(FlaskForm):
    email = StringField(label='Email', render_kw={"size": 30}, validators=[DataRequired(), EmailValidator()])
    password = PasswordField(label='Password', render_kw={"size": 30}, validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
