# Cinema Central
Kelsey Chen, Krisha Patel, Eva Tuecke

Welcome to Cinema Central! This website and web application offers movie suggestions, displays real-time reviews on movies, lets users write movie reviews, and allows users to search and save movies on their watchlist.

**See the video walk-through of our website here:** https://youtu.be/rMg5qKb0IM4

# Getting Started

## Pre-requisites
This web app was made with Python, Jinja, Flask, HTML, CSS, and Javascript for use on computer and mobile.

## Installing
1. Upload the files downloaded from Gradescope in the CS50 IDE or your preferred development environment or clone this github repository at https://github.com/etuecke/cs50finalproject.

2. Use the command line and enter the main directory of the root folder of the project, "cd cs50finalproject".

3. Export the api keys in the key.txt file by using the command line. Enter "export API_KEY=UdslRxWT1wfX4mt8zWgpX7v5gOADWTos" and "export IMDB_KEY=k_54zd2ctl" in the main directory of the root folder. 

4. Use "flask run" to view a local version of the file.

# The Directory 

## Templates Directory
* apology.html: 
    - An HTML page that displays whatever error the user may run into
* index.html: 
    - The landing page that links users to other pages
    - If a user is logged in, it displays movies the user has watched and the user's watchlist after they've added those from the search page results
* layout.html:
    - The base HTML page used as a template for the rest of the HTML pages
* login.html: 
    - The login page that allows users to log into their accounts
* lucky.html:
    - An HTML page that displays a random movie presented to user (movie details and poster)
* news.html:
    - An HTML page that reads from the New York Times API to give the user recent movie reviews from the New York Times 
* quiz.html: 
    - The landing page for quiz
* quizQuestion1, quizQuestion2, quizQuestion3, quizQuestion4
    - HTML pages that display the quiz questions
* quizResults:
    - An HTML page that displays movie recommendations based on the user's responses to the quiz
* register.html:
    - The registration page that allows a user to register for a new account
* search.html: 
    - An HTML page where the user can input search criteria to find movies
* searched.html: 
    - An HTML page that displays the results from the search page
    - Allows users to select movies and add them to movies they have watched or their watchlist
* reviews.html:
    - Allows users to write reviews and also view the reviews written by other users
* visualizations.html:
    - Displays interactive visualization for the number of movies each director has directed
* visualizations2.html:
    - Displays interactive visualization for the ratings and votes for each movie

## Root Directory
* helpers.py: 
    - A helper file that contains python functions that used in app.py. Methods amongst others include the apology function, getting movie reviews, and pulling poster images. 
* app.py: 
    - The main python file containing routes to all pages of the web application. 
* key.txt: 
    - A text file that contains the API keys needed for the New York Times movie reviews and the IMDB movie posters. 
* movies.db: 
    - SQLite database containing tables of basic movie details, director information, stars information, etc. from which the main functionality of the app draws from

## Design Documentation
DESIGN.md includes documentation on how we implemented our project and why we made the design decisions we did. 

# Using the Website 
To receive movie recommendations, search for movies, add movies to their personal lists, or read movie reviews, users must be logged in. Upon first opening the website, the user will see the login page, in which they need to log in or register for an account. After successfully registrating for an account, a user will be redirected to the login page, where they can then log into their account using the username and password that they created. 

After logging in, users will be able to view the landing page, which displays the movies they have watched and the movies they want to watch. If this is a user's first time on the website, then they will not see their "watched" movies or "want to watch" movies lists populated. In order to do so, they must navigate to other parts of the website and utilize the search function to add more information to their profile. 

## Recieving Movie Recommendations
The user can recieve movie recommendations through both the quiz button and the "I'm Feeling Lucky!" button in the top left hand corner. The quiz will have four questions. The first two ask the user to select a movie, the third question will ask the user to select a year, and the last question asks the user to select a word (which is selected randomly from the movie titles). Then, the user will recieve movie recommendations based on their selections. We have filtered the movie options that the quiz will recommend to the user movies that were released after 1990, have over 1000 ratings, and have a rating over 7 stars. These filters were implemented with the purpose of quality control in the movie recommendations.

The "I'm Feeling Lucky!" button generates a random movie recommendation from all the movies in the database. 

## Adding Movies to "Movies I've Seen" and "My Watchlist" 
To add movies to "Movies I've Seen" or "My Watchlist", users can find specific movies through the search page. The user can simply search a movie by the title or use the advanced search function. With advanced search, the user can search by title, star, or user rating (provided they also search a director or star when searching by user rating). When the results of their search comes up, users can select movies from the list by clicking the checkboxes and add them to "Movies I've Seen" or "My Watchlist." This will then populate the landing page with details of these movies. 

## Getting Movie Reviews
To view the most recent movie reviews from the New York Times, users can navigate to the News page. If the user would like to read the full review, they can click on the "Read More" button, which will direct them to the New York Times article itself.

## Viewing Movie-Related Data Visualizations
Users can interact with and view data visualizations of information encompassed in the movies database. We included two different visualizations: 
1. Number of movies directed by each director 
2. The ratings and number of votes that each movie recieved 

## Writing Movie Reviews and Interacting With Other Users
Users can read and write moview reviews on the Moview Reviews page. The user must first write and post a review to see reviews written by other users. To write a review, the user must fill out the form under "Add a New Review" and click the "Add New Review Button." After submitting the review, users will be able to see the Reviews Log, which displays the movie reviews written by all users. 

## Logging Out
To log out of the website, the user can click on "Log Out" on the navigation bar in the top right.
