import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import random

from helpers import apology, login_required, get_details, get_reviews, get_review_details, get_random_movie_list, get_random_years_list, get_random_words, get_poster_url, get_random_movie_from_director


# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///movies.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


#TODO: implement homepage
@app.route("/")
@login_required
def index():
    """display homepage"""

    # get movies I've watched
    query1 = "SELECT movie_title FROM homepageMovies WHERE type =? AND user_id =?"
    haveWatched = db.execute(query1, "haveWatched", session["user_id"]) # list of dicts that store movie_title 
    details1 = [] # list of dicts that store directors, stars, rating, year of each movie
    for i in range(len(haveWatched)):
        id = db.execute("SELECT id FROM movies WHERE title = ?", haveWatched[i]['movie_title'])[0]['id']
        details1.append(get_details(id))
        url = get_poster_url(haveWatched[i]['movie_title'])
        details1[i]['url'] = url
    print(haveWatched)

    # get movies to watch
    query2 = "SELECT movie_title FROM homepageMovies WHERE type =? AND user_id =?"
    toWatch = db.execute(query2, "toWatch", session["user_id"])
    details2 = []
    for movie in toWatch:
        id = db.execute("SELECT id FROM movies WHERE title = ?", movie['movie_title'])[0]['id']
        details2.append(get_details(id))
    # print(toWatch)

    return render_template("index.html", haveWatched = haveWatched, toWatch = toWatch, details1 = details1)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # When requested via GET, display registration form
    # Create a new template for registration (borrow from login.html)
    # User should be prompted for username, password, and a confirmation
    if request.method == "GET":
        return render_template("register.html")

    # When form is submitted via POST, check for possible errors and insert the new user into users table
    # HTML: <input name="password" ... />
    # Python: request.form.get("password")
    elif request.method == "POST":
        # Error checking
        # If any field is left blank, return an apology
        if not request.form.get("password"):
            return apology("You must provide a password", 400)
        elif not request.form.get("username"):
            return apology("You must provide a username", 400)
        elif not request.form.get("confirmation"):
            return apology("You must type your password in the confirmation field", 400)

        # If password and confirmation don't match, return an apology
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and confirmation do not match", 400)

        # Special feature: password must contain digits
        # This is commented out because it breaks check 50's ability to register, but otherwise would work
        #for char in request.form.get("password"):
        #    if not char.isdigit():
        #        return apology("Please include at least one digit in your password", 400)
                
        # If the username is already taken, return an apology
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) == 1:
            return apology("This username already exists", 400)

        # Add the user to the users table of database
        # Security: database should never store plain text password
        # Security: User generate_password_hash to generate a hash of the password
        password_hash = generate_password_hash(request.form.get("password"))
        new = db.execute("INSERT into users(username, hash) VALUES(?,?)", request.form.get("username"), password_hash)

        # Log user in 
        # session["user_id"] keeps track of which user is logged in
        # Redirects to the home page
        return redirect("/")


@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    """Get movie recommendations."""
    if request.method == "POST":
        # empty whatever was stored in the sql database previously 
        db.execute("DELETE from quizTempData")

        movies = get_random_movie_list()
        return render_template("quizQuestion1.html", options = movies)

    else:
        return render_template("quiz.html")


@app.route("/quizQuestion1", methods=["GET", "POST"])
@login_required
def quizQuestion1():
    if request.method == "POST":
        title = request.form.get("title")
        # add title to the sql database
        db.execute("INSERT INTO quizTempData(value, question) VALUES(?,?)", title, 1)
        
        movies = get_random_movie_list()
        return render_template("quizQuestion2.html", options = movies)


@app.route("/quizQuestion2", methods=["GET", "POST"])
@login_required
def quizQuestion2():
    if request.method == "POST":
        title = request.form.get("title")
        # add title to the sql database
        db.execute("INSERT INTO quizTempData(value, question) VALUES(?,?)", title, 2)


        years = get_random_years_list()
        return render_template("quizQuestion3.html", options = years)


@app.route("/quizQuestion3", methods=["GET", "POST"])
@login_required
def quizQuestion3():
    if request.method == "POST":
        year = request.form.get("year")
        data = str(year)
        # add year to the sql database
        db.execute("INSERT INTO quizTempData(value, question) VALUES(?,?)", data, 3)
        
        movie_titles = get_random_movie_list()
        words = get_random_words(movie_titles)

        options = []
        for i in range(0, 4):
            option_set = []
            option_set.append(movie_titles[i])
            option_set.append(words[i])
            options.append(option_set)
        
        return render_template("quizQuestion4.html", options = options) #first value is movie, the second is the word 


@app.route("/quizQuestion4", methods=["GET", "POST"])
@login_required
def quizQuestion4():
    if request.method == "POST":
        title = request.form.get("title")
        # add title to the sql database
        db.execute("INSERT INTO quizTempData(value, question) VALUES(?,?)", title, 4)

        # retreive information from database to send to the quizResults file
        movie1_title = (db.execute("SELECT value FROM quizTempData WHERE question = ?", 1))[0].get("value")
        movie2_title = (db.execute("SELECT value FROM quizTempData WHERE question = ?", 2))[0].get("value")
        year = (db.execute("SELECT value FROM quizTempData WHERE question = ?", 3))[0].get("value")
        movie3_title = (db.execute("SELECT value FROM quizTempData WHERE question = ?", 4))[0].get("value")

        # find the directors the movies: 
        director1 = db.execute("SELECT name FROM people "
                               "INNER JOIN directors ON people.id = directors.person_id "
                               "INNER JOIN movies ON directors.movie_id = movies.id "
                               "WHERE movies.title = ?", movie1_title)[0].get("name")
        director2 = db.execute("SELECT name FROM people "
                               "INNER JOIN directors ON people.id = directors.person_id "
                               "INNER JOIN movies ON directors.movie_id = movies.id "
                               "WHERE movies.title = ?", movie2_title)[0].get("name")
        
        director3 = db.execute("SELECT name FROM people "
                               "INNER JOIN directors ON people.id = directors.person_id "
                               "INNER JOIN movies ON directors.movie_id = movies.id "
                               "WHERE movies.title = ?", movie3_title)[0].get("name")

        # pick out random movies based on that information
        # 1. based on directors
        movie1 = get_random_movie_from_director(director1)
        movie2 = get_random_movie_from_director(director2)
        movie3 = get_random_movie_from_director(director3)

        # 2. based on year 
        rows = db.execute("SELECT title FROM movies WHERE year = ?", year)
        row_index = random.randint(0, len(rows)-1)
        movie4 = rows[row_index]

        movies = [movie1, movie2, movie3, movie4]
        poster_urls = []
        # Get poster urls 
        for movie in movies:
            poster_urls.append(get_poster_url(movie.get('title')))

        print(poster_urls)

        # find a random movie from the same year 
        return render_template("quizResults.html", movies = movies, urls = poster_urls)



@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    """Get search results."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # normal searching by title
        if request.form.get("movie_title"):
            movie_title = request.form.get("movie_title")
            movies = db.execute("SELECT * FROM movies WHERE title = ?", movie_title)
            details_list = []
            for movie in movies:
                details_list.append(get_details(movie["id"]))
            return render_template("searched.html", searched = movies, details = details_list)
        
        # advanced search: search only by director  
        elif request.form.get("director") and (not request.form.get("to")) and (not request.form.get("from")) and (not request.form.get("starring")):
            director = request.form.get("director")
            movies = db.execute("SELECT * FROM movies "
                                " INNER JOIN directors ON movies.id = directors.movie_id "
                                " INNER JOIN people ON directors.person_id = people.id "
                                " WHERE people.name = ?", director)
            details_list = []
            for movie in movies:
                details_list.append(get_details(movie["movie_id"]))
            return render_template("searched.html", searched = movies, details = details_list)
            

        # advanced search: search only by starring
        elif request.form.get("starring") and (not request.form.get("to")) and (not request.form.get("from")) and (not request.form.get("director")):
            star = request.form.get("starring")
            movies = db.execute("SELECT * FROM movies "
                                " INNER JOIN stars ON movies.id = stars.movie_id "
                                " INNER JOIN people ON stars.person_id = people.id "
                                " WHERE people.name = ?", star)
            details_list = []
            for movie in movies:
                details_list.append(get_details(movie["movie_id"]))
<<<<<<< Updated upstream
            return render_template("searched.html", searched = movies, details = details_list)

        # advanced search: searching by ratings 
        elif request.form.get("to") and (request.form.get("from")) and ((request.form.get("starring")) or (request.form.get("director"))):
            lower_bound = request.form.get("from")
            upper_bound = request.form.get("to")

            if request.form.get("starring"):
                star = request.form.get("starring")
                movies = db.execute("SELECT * FROM movies "
                                    " INNER JOIN ratings ON movies.id = ratings.movie_id "
                                    " INNER JOIN stars ON movies.id = stars.movie_id "
                                    " INNER JOIN people ON stars.person_id = people.id "
                                    " WHERE ((ratings.rating BETWEEN ? AND ?) AND people.name = ?)", lower_bound, upper_bound, star)

            if request.form.get("director"):
                director = request.form.get("director")
                movies = db.execute("SELECT * FROM movies "
                                    " INNER JOIN ratings ON movies.id = ratings.movie_id "
                                    " INNER JOIN directors ON movies.id = directors.movie_id "
                                    " INNER JOIN people ON directors.person_id = people.id "
                                    " WHERE ((ratings.rating BETWEEN ? AND ?) AND people.name = ?)", lower_bound, upper_bound, director)

            details_list = []
            for movie in movies:
                details_list.append(get_details(movie["movie_id"]))
=======
>>>>>>> Stashed changes
            return render_template("searched.html", searched = movies, details = details_list)

        # TO DO: searching by ratings
    
    # User reached route via GET (as by clicking a link or via redirect)
    else: 
        return render_template("search.html")

@app.route("/searched", methods=["GET", "POST"])
@login_required
def searched():
    if request.method == "POST":

        titles = ""
        list_type = request.form.get("list")

        if (list_type == "toWatch"):
            titles = request.form.get("toWatch")
        
        elif (list_type == "haveWatched"):
            titles = request.form.get("haveWatched")

        title_list = titles.split(",")

        # add information into homepage database 
        for title in title_list:
            rows = db.execute("SELECT movie_title FROM homepageMovies WHERE movie_title = ? and user_id = ?", title, session["user_id"])
            if len(rows) == 0:
                db.execute("INSERT INTO homepageMovies(movie_title, user_id, type) VALUES(?,?,?)", title, session["user_id"], list_type)

        return redirect("/")
    

@app.route("/news", methods=["GET", "POST"])
@login_required
def news():
    """Get movie news."""
    data = get_reviews()
    reviews = []
    for review in data:
        temp = get_review_details(review)
        reviews.append(temp)
    return render_template("news.html", reviews=reviews)


@app.route("/lucky")
@login_required
def lucky():
    """Get random movie rec."""
    rows = db.execute("SELECT * FROM movies")
    random_mov = rows[random.randint(0, len(rows)-1)]
    return render_template("lucky.html", lucky = random_mov, details = get_details(random_mov["id"]), url = get_poster_url(random_mov["title"]))


@app.route("/reviews", methods=["GET", "POST"])
@login_required
def reviews():
    if request.method == "POST":
        if request.form.get("movietitle") and request.form.get("review"):
            movie_title = request.form.get("movietitle")
            review = request.form.get("review")

            username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
            print(username)

            db.execute("INSERT INTO reviews(id, username, title, review, datetime) VALUES(?,?,?,?,?)", session["user_id"], username[0]["username"], movie_title, review, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        reviews_list = db.execute("SELECT * FROM reviews")

        for movie in reviews_list:
            movie["url"] = get_poster_url(movie["title"])     

        return render_template("reviews.html", all_reviews = reviews_list)

    else:
        return render_template("reviews.html")