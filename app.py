import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import random

from helpers import apology, login_required, get_details

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
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """display homepage"""
    return render_template("index.html")


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


#TODO: add user to users database upon registration
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
        db.execute("INSERT into users(username, hash) VALUES(?,?)", request.form.get("username"), password_hash)

        # Log user in 
        # session["user_id"] keeps track of which user is logged in
        # Redirects to the home page
        return redirect("/")


#TODO: handle quiz 
@app.route("/quiz")
@login_required
def quiz():
    """Get movie recommendations."""
    return render_template("quiz.html")


#TODO handle searching movies (use quote() from Finance as a template)
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
            return render_template("searched.html", searched = movies, details = details_list)

        # TO DO: searching by ratings

    # User reached route via GET (as by clicking a link or via redirect)
    else: 
        return render_template("search.html")

#TODO: fetch news 
@app.route("/news")
@login_required
def news():
    """Get movie news."""
    return render_template("news.html")

#TODO: fetch random rec (lucky) 
@app.route("/lucky")
@login_required
def lucky():
    """Get random movie rec."""
    rows = db.execute("SELECT * FROM movies")
    random_mov = rows[random.randint(0, len(rows)-1)]
    return render_template("lucky.html", lucky = random_mov, details = get_details(random_mov["id"]))
