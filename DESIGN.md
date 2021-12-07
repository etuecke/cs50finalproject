# Design

## Back-end

### Initial Databasing
All of the data from this project draws from the movies.db database, containing information on the movies themselves, the directors, the stars, the ratings for the movies, etc. In addition, we set up several more tables in this database that are continuously updated and modified as the user interacts with our website. See the description of these tables below:
1. homepageMovies
    - Fields: movie_title (text), user_id (integer), type (text)
    - This data table is used to populate the homepage information that displays the user's to-watch list and the movies that the user has already watched
    - This table is populated when the user uses the "search" function to search up a movie or series of movies. On the search results page (searched.html), the user can choose to add movies to their watch list or to the list of movies they have already watched. Doing so will store that information in the homepageMovies table. 
    - The 'movie_title' field is set to whatever movie the user selected, the 'user_id' field is the id for the current session, and the 'type' field is set either to "toWatch" or "haveWatched." This "toWatch" or "haveWatched" determines where the movie is displayed on the home page, which accesses the data in this table.
2. quizTempData:
    - Fields: value (text), question (integer)
    - This table is used to temporarily store data on how the user answers questions for the quiz. 
    - At the beginning of taking the quiz, all data in this data is completely cleared out. This is because this data does not need to be stored long term: it only needs to be stored for the duration of the quiz until the movie recommendations are provided to the user. 
    - After answering every question, the question number (question field) and the user's answer to the question (value) is stored in this table.
    - This data is then accessed in the algorithm that makes movie recommendations to the user at the end of the quiz. 
3. users:
    - The users table tracks information on various users that login to the platform. This particular table works similarly as the login implementation for the 'Finance' PSet worked
4. INCLUDE THE NEW TABLE FOR THE REVIEWS PAGE
    - DESCRIPTION FOR THIS PAGE

### Web scraping / API usage
It took a significantly longer time to gather the news data from Google News than we had anticipated. Initially, we attempted to web scrape with Jupyter Notebook and CoLab but struggled with installing Selenium. When we finally got Selenium to work properly with the webdriver in Jupyter, we found it very difficult to pull information from Google News. Thus, we opted to use the New York Times Dev Portal, which allowed us to access movie reviews through its API. By using the NYT API, we were able to pull data dynamically from the website, so our website updates autonomically when the NYT posts a new review. Furthermore, we also used the IMDB API to pull movie posters from the IMDB database, which are displayed along with movie information on the homepage, the quiz, the movie reviews page, and the "I'm Feeling Lucky Page." 

### The Flask App
Let us go through the pages and the design choices and considerations that went into each function:
1. Index ("~/"): 
    - This homepage uses the homepageMovies table in the movies.db database to populate onto the page that the user has watched already and movies that the user wants to watch. It also uses the helper function get_details() to get details (directors, year, rating, and stars) of each movie and displays them to the user. The function also uses the helper function get_poster_url() to pull the movie poster image from the IMDB database. 
2. Login ("~/login"), Logout ("~/logout"), and Register ("~/register")
    - The implementation of these are similar to the Finance pset. These functions work with the users table in movies.db to log different users in and out of the application.
3. Quiz pages ("~/quiz", "~/quizQuestion1", "~/quizQuestion2", "~/quizQuestion3", "~/quizQuestion4")
    - Quiz: This page has a simple 'Start quiz' button that routes the user to the first page of the quiz.
    - Question 1: This function retrieves the title of the movie that the user picks for this question and adds it to the quizTempData table in movies.db. It then generates another series of random movies based on selection criteria defined in helpers.py and sends those movies to the quizQuestion2 html page. 
    - Question 2: This sends a randomly generated year to the next page, quizQuestion3.
    - Question 3: This page takes a random list of movies and chooses a random word out of their titles. It then takes the original list of movie titles and the random words taken from those tables and send that information to quizQuestion4, where the user will pick their favorite word out of the options provided. 
    - Question 4: The actual algorithm for computing the movie recommendations is housed in this function, which ends with the list of movie recommendations being sent to the quizResults.html page. 
    - Movie recommendations algorithm: through querying the quizTempData table in movies.db, we pick movies from the database with similar directors or that were made in the same year as the movies that the user chose. Based on the director/year, we then choose a random movie from the database given these constrained parameters. 
    - Display: We use the IMDB API here to get the images of the movie posters, which are displayed along with the title on each page of the quiz.
    - Design Rationale: We chose to split this quiz up into individual html pages per question because this made it easy to store the data from each page in the movies.db database. Having each html page lead to the next question in the quiz fit the aesthetic design that we wanted to create with the quiz. 
4. Search ("~/search")
    - The search page allows for two different ways of searching for movies: simply searching by title and searching in a more complicated way by factors like director or who is starring in the movie. 
    - Implementation Details: The movies database is queried to assemble a list of movies that fits the search criteria. The titles of these movies and various details associated with them are then passed onto the searched.html page, where the search results are actually displayed in table format. 
5. Searched ("~searched")
    - The challenge of this page was collecting the movies selected by the user to be added to the homepageMovies table in the database.
    - The corresponding html file uses JavaScript to determine which movies are selected, and the flask app then inserts that information into the correct table. 
    - We make sure not to allow duplicate movies to be added into this table for any given user, since this would not make sense when using this table to populate the homepage if there were multiple copies of the movies being displayed.
    - We redirect directly to the home page.
6. News ("~/news"): 
    - This function uses the helper functions get_reviews() and get_review_details() to pull recent movie reviews from the New York Times. 
7. I'm Feeling Lucky ("/lucky")
    - This is a feature that allows the user to be presented with a randomly chosen movie to watch. The function randomly sorts all the movies in the movies table in the database and selects the first item to display to the user. 
8. Reviews ("~/reviews"):
** KRISHAAAAAAAAA **

### Helpers.py
1. get_details():
    - We included this helper function to make it easy to assemble all relevant information about a movie, without having to copy and paste the queries required to do so over and over. 
    - This helper function retrieves information about the directors, the stars, the movie rating, the year the movie was made, etc. using SQL queries.
2. get_reviews() and get_review_details(): 
    - get_reviews(): this function contacts the New York Times API to retrieve a json that contains data on the most recent movie reviews published by the NYT. The function then parses the results to return a list of all reviews and their details (movie_title, byline, headline, mpaa_rating, etc.). 
    - get_review_details(): this function picks relevant details (headline, byline, summary, date, and link to the image) from the list of reviews. 
3. Helper functions for the quiz: 
    - get_random_movie_list()
    - get_random_years_list()
    - get_random_words()
    - get_random_movie_from_director()
    - The quiz requires multiple queries to get random movie titles/random years/random words out of movie titles. To prevent code duplication, we placed all of these SQL queries in the helper functions file. 
4. get_poster_url(): 
    - This function contacts the IMDB API, searches for the movie title, and parses the results to return the poster url. 
    - The url is then used in the src attribute of the image of the relevant html pages to display the image to the user.  
    - This helper function is called frequently in our application any time we need to display a poster image for a movie along with the title of the movie 

## Front-end

### Design Decisions for HTML Templates 
Along with the web scraping part of this project, designing the front end and getting the template files to properly interface with our flask app took the most time. In particular, we spent a fair amount of time on correctly passing information between pages and interfacing with the database, since we had not done much of this in class. 
See below the list of design decisions made with respect to the more complicated of these templates.
1. index.html
    - We used jinja to iterate through the user's haveWatched and toWatch lists, ultimately displaying 
2. layout.html
    - ANY BOOTSTRAP STUFF?
3. news.html
    - KELSEY FILL IN
4. quiz.html, quizQuestion1, quizQuestion2, quizQuestion3, quizQuestion4, quizResults  
    - We used bootstrap to display the different options for these quiz pages in a flex container, with each option displayed on a different card that included a movie title and a movie poster image
    - Jinja was used to prevent code duplication, as we used for loops to populate the flex containers
    - Hidden input fields were used to send information back to the flask app, where it could be added to the correct table(s) in the database
5. search.html
    - We wanted to design a search page with multiple search options for the user to take advantage of 
6. searched.html
    - This was one of the most complicated pages of the templates that we did. 
    - Using the search results, this html page populates the search data into a table that displays information like the movie title, the director(s), and the stars of the movie. It also adds a checkbox next to every row, which can be used to select multiple movies at once and add them to the watch list of have watched list (populated on the home page)
    - We used JavaScript to determine which movies had been selected and which button had been clicked (which determines which list to add the selected movies to)
    - We also learned some JQuery to make this section work
    - For ease-of-design, we also used hidden input fields to store information about which movies the user selects, since these can easily be read in the flask app using request.form.get("[input field name]")
    - When the user selects a list of movies and then clicks the "Add to Watch List" or "Have Watched" button, the value of thes hidden input fields is changed to the list of selected movies. Similarly, another input field is used to track if the "Add to Watch List" or "Have Watched" button was clicked. 
7. reviews.html
    - We wanted to design a reviews page where users could both leave a review for a movie they've watched before, and read those of others (once they've left at least one review). 
    - This feature allows users to see content from other users and interact with other users

### Design Process 
We spent a significant amount of time in the ideation process and underwent several brainstorming sessions to discuss how the website would look and how we planned to structure the code. We created a couple low-fidelity prototypes to visualize the page layouts, ultimately choosing the one we implemented. 

### Implementation 
In the implementation of the design, we took advantage of the flex containers and cards in Bootstrap. By wrapping content in flex containers, we were able to size the content of our webpages to fit any screen size. Thus, users can interact with Cinema Central on computer, tablet, or mobile. We also used Bootstrap's card and grid containers to display content in an easily digestible format. Since we used flexbox with our grid, we were able to wrap cards in the grid to accomodate any screen size.  


# Built With
* CS50 IDE
* VSCode 
* Sublime Text + Terminal
* Bootstrap
* NYT and IMDB 
* Tableau Public 
* GitHub


# References and Resources
* https://developer.nytimes.com/apis
* https://imdb-api.com/
* https://www.w3schools.com/ 
* https://jsonformatter.curiousconcept.com/# JSON formatting website used to format the result of the API request from the NYT website. 
