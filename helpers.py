from flask import redirect, render_template, request, session
from functools import wraps
from cs50 import SQL
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///movies.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def get_details(movie_id):
    """Get directors (array), stars (array), ratings (float), year of a movie (int)"""
    details= {}

    # get directors of a movie 
    directors = []
    director_ids = db.execute("SELECT person_id FROM directors WHERE movie_id = ?", movie_id)
    for x in director_ids:
        director = db.execute("SELECT name FROM people WHERE id = ?", x['person_id'])
        directors.append(director[0]["name"])
    details["directors"] = directors 

    # get stars of a movie
    stars = []
    star_ids = db.execute("SELECT person_id FROM stars WHERE movie_id = ?", movie_id)
    for x in star_ids:
        star = db.execute("SELECT name FROM people WHERE id = ?", x['person_id'])
        stars.append(star[0]["name"])
    details["stars"] = stars 

    # get ratings of a movie
    rating = db.execute("SELECT rating FROM ratings WHERE movie_id = ?", movie_id)
    details["rating"] = rating

    # get year of a movie
    year = db.execute("SELECT year FROM movies WHERE id = ?", movie_id)
    details["year"] = year

    return details
    
