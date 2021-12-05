import os
import requests
import urllib.parse

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

########## Function to get details from database ###################################################
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

########## Functions to get movie news ###################################################
def get_reviews():
    """Look up details for reviews."""
    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.nytimes.com/svc/movies/v2/reviews/search.json?&api-key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        print("there")
        return None

    # Parse response
    try:
        reviews = response.json()
        return reviews["results"]
    except (KeyError, TypeError, ValueError):
        print("here")
        return None

def get_review_details(review):
    return {
        "headline": review["headline"],
        "byline": review["byline"],
        "summary": review["summary_short"],
        "date": review["publication_date"],
        "link": review["link"]["url"], 
        "image_url": review["multimedia"]["src"]
    }

########## Functions to get movie posters ###################################################
def get_poster_url(title):
    """Look up poster url for movie."""
    # Contact API
    try:
        api_key = os.environ.get("IMDB_KEY")
        url = f"https://imdb-api.com/en/API/SearchMovie/{api_key}/{title}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        print("there")
        return None

    # Parse response
    try:
        reviews = response.json()
        print (reviews["results"][0]["image"])
        return reviews["results"][0]["image"]
    except (KeyError, TypeError, ValueError):
        print("here")
        return None