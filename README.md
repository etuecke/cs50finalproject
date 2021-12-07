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
* apology.html: an HTML page that displays whatever error the user may run into.
* details.html: [REMOVE THIS IF WE DON'T END UP USING IT!!!!]
* index.html: the landing page that links users to other pages and log in.
* layout.html: the base HTML page used as a template for the rest of the HTML pages
* login.html: 
* lucky.html:
* news.html:
* quiz.html: 
* quizQuestion1: 
* quizQuestion2: 
* quizQuestion3: 
* quizQuestion4: 
* quizResults:
* recommendations.html: 
* register.html:
* search.html:
* searched.html: 

## Root Directory
* helpers.py: a helper file that contains python functions that used in app.py. Methods include the apology function, getting movie reviews, and pulling poster images. 
* app.py: the main python file containing routes to all pages of the web application. 
* key.txt: a text file that contains the API keys needed for the New York Times movie reviews and the IMDB movie posters. 
* movies.db: SQLite database containing [EVA TALK ABOUT ALL THESE TABLES!!!!!!!!!!!!!!!!!!!!] tables from which the main functionality of the app draws from.  

## Design Documentation
DESIGN.md includes documentation on how we implemented our project and why we made the design decisions we did. 

# Using the website 
