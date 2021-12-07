# Cinema Central
Kelsey Chen, Krisha Patel, Eva Tuecke

Welcome to Cinema Central! This website and web application offers movie suggestions, displays real-time reviews on movies, and allows users to search and save movies on their watchlist. 

# Getting Started

## Pre-requisites
This web app was made with Python, Jinja, Flask, HTML, CSS for use on computer and mobile.

## Installing
1. Upload the files downloaded from Gradescope in the CS50 IDE or your preferred development environment or clone this github repository at https://github.com/etuecke/cs50finalproject.

2. Use the command line and enter the main directory of the root folder of the project, "cd csfinalproject".

3. Export the api keys in the key.txt file by using the command line. Enter "export API_KEY=pk_126ad0f16a4440abbd2524ec7f394a03" and "export NYT_KEY=UdslRxWT1wfX4mt8zWgpX7v5gOADWTos" in the main directory of the root folder. 

4. Use "flask run" to view a local version of the file.

# The Directory 

## Templates Directory
* apology.html: 
    - an HTML page that displays whatever error the user may run into.
* details.html: 
    - [REMOVE THIS IF WE DON'T END UP USING IT!!!!]
* index.html: 
    - the landing page that links users to other pages and log in.
* layout.html: 
    - the base HTML page used as a template for the rest of the HTML pages
* login.html: 
    - similar to finance
* lucky.html:
    - random movie presented to user
* news.html:
    - uses webscraping to give user recent movie news /recommendations from the New York Times 
* quiz.html: 
    - starter page for quiz
* quizQuestion1 
* quizQuestion2
* quizQuestion3
* quizQuestion4
* quizResults:
* recommendations.html: 
    - [REMOVE THIS IF WE DON'T END UP USING]
* register.html:
    - similar to finance
* search.html: 
    - page where the user can input searching criteria 
* searched.html: 
    - displays the results from the search page
    - allows users to select movies and add them to the homepageMovies database under various categories
* reviews.html:
    - allows users to write reviews and also view the reviews written by other users

## Root Directory
* helpers.py: 
    - a helper file that contains python functions that used in app.py. Methods include the apology function, getting movie reviews, and pulling poster images. 
* app.py: 
    - the main python file containing routes to all pages of the web application. 
* key.txt: 
    - a text file that contains the API keys needed for the New York Times movie reviews and the IMDB movie posters. 
* movies.db: 
    - SQLite database containing [EVA TALK ABOUT ALL THESE TABLES!!!!!!!!!!!!!!!!!!!!] tables from which the main functionality of the app draws from.  

## Design Documentation
DESIGN.md includes documentation on how we implemented our project and why we made the design decisions we did. 

# Using the Website 
To receive movie recommendations, search for movies, add movies to their personal lists, or read movie reviews, users must be logged in. Upon first opening the website, the user will see the login page, in which they need to log in or register for an account. After successfully registrating for an account, a user will be redirected to the login page, where they can then log into their account using the username and password that they created. 
After logging in, users will be able to view the landing page, which displays the movies they have watched and the movies they want to watch. 

## Recieving Movie Recommendations
The user can recieve movie recommendations through both the quiz button and the "I'm Feeling Lucky!" button in the top left hand corners. The quiz will have four questions. The first two ask the user to select a movie, the third question will ask the user to select a year, and the last question asks the user to select a word (which is selected randomly from the movie titles). Then, the user will recieve movie recommendations based on their selections. We have filtered the movie options that the quiz will recommend to the user movies that were released after 2010, have over 1000 ratings, and have over 7 stars in the rating. These filters were implemented with the purpose of quality control in the movie recommendations.
The "I'm Feeling Lucky!" button generates a random movie recommendation from all the movies in the database. 

## Searching for Movies
The user can search for movies  

## Adding Movies to "Movies I've Seen" and "My Watchlist" 
this should be easy and if you can't figure it out without this documentation u dumb

## Writing Movie Reviews and Interacting With Other Users
add details here 
this should be about the reviews page where users can write their own reviews/read reviews

## Getting Movie News and Reviews (Webscraped)
add details here about news page
