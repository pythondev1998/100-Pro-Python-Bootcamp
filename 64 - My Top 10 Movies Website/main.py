from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6' #letra...
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    # Retrieve all movies from the database
    movies = Movie.query.all()

    # Sort movies by rating in descending order
    movies = sorted(movies, key=lambda movie: movie.rating or 0, reverse=True)

    # Assign rankings to the movies
    for i, movie in enumerate(movies, start=1):
        movie.ranking = i

    # Commit the changes to the database
    db.session.commit()
    return render_template("index.html", movies=movies)


####
def search_movies(title):
    api_key = 'd01317db04149d9a8b84f610da473b75'  # Reemplaza esto con tu propia API key de TMDB
    base_url = 'https://api.themoviedb.org/3/search/movie'

    # Parámetros de la consulta
    params = {
        'api_key': api_key,
        'query': title
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta

        # Obtenemos los resultados de la búsqueda
        results = response.json()['results']

        # Extraemos la información requerida de cada película
        movies = []
        for result in results:
            movie = {
                'title': result['title'],
                'img_url': result['poster_path'],
                'year': result['release_date'][:4],  # Obtenemos solo el año de la fecha de lanzamiento
                'description': result['overview']
            }
            movies.append(movie)

        return movies
    except requests.exceptions.RequestException as e:
            print('Error en la solicitud:', e)
####

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        search_results = search_movies(movie_title)
        session["search_results"] = search_results  # Almacenar los resultados de búsqueda en la sesión
        print("search_results:", search_results)
        print("session:", session)
        return render_template("select.html", options=search_results, form=form)
    return render_template("add.html", form=form)


@app.route("/select", methods=["POST"])
def select_movie():
    selected_movie = request.form.get("selected_movie")
    title, year = selected_movie.split(" - ")
    search_results = search_movies(title)
  
    # Buscar la película seleccionada en la lista de resultados de búsqueda
    selected_movie = None
    for movie in search_results:
        if movie['title'] == title and movie['year'] == year:
            selected_movie = movie
            break

    if not selected_movie:
        # Manejar el caso en que la película seleccionada no se encuentre en los resultados de búsqueda
        return redirect(url_for("add_movie"))

    # Crear un nuevo objeto Movie y asignar los valores de los campos
    movie = Movie(
        title=selected_movie['title'],
        img_url='https://image.tmdb.org/t/p/w500' + selected_movie['img_url'],
        year=int(selected_movie['year']),
        description=selected_movie['description']
    )
    # Guardar la película en la base de datos
    db.session.add(movie)
    db.session.commit()

    # Eliminar los resultados de búsqueda de la sesión
    session.pop("search_results", None)

    return redirect(url_for("rate_movie", id=movie.id))



# Adding the Update functionality
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))
   

if __name__ == '__main__':
    app.run(debug=True)