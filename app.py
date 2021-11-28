from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#TODO: implement homepage
@app.route("/")
def index():
    """Show movies I've seen and recommended movies"""
    return render_template("index.html")

#TODO: implement login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

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
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return redirect("/")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

#TODO: handle quiz 
@app.route("/quiz")
def quiz():
    """Get movie recommendations."""
    return render_template("quiz.html")

#TODO handle searching movies (use quote() from Finance as a template)
@app.route("/search")
def search():
    """Get search results."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return render_template("searched.html")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else: 
        return render_template("quote.html")
