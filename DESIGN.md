# Design
PROMPT: Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, 
consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

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

### Web scraping / API usage (Kelsey)
It took a significantly longer time to gather the news data from Google News than I had anticipated. Initially, I attempted to web scrape with Jupyter Notebook and CoLab but struggled with installing Selenium. When I finally got Selenium to work properly with the webdriver in Jupyter, I found it very difficult to pull information from Google News. Thus, I opted to use the New York Times Dev Portal, which allowed me to access movie reviews through its API. Furthermore, I also used the IMDB API to pull movie posters from the IMDB database, which are displayed along with movie information on the homepage, the quiz, and the "I'm Feeling Lucky Page." 

### The Flask App
Let us go through the pages and the design choices and considerations that went into each function:
1. Index ("~/"): 
    - This homepage uses the homepageMovies table in the movies.db database to populate onto the page that the user has watched already and movies that the user wants to watch
2. Login ("~/login"), Logout ("~/logout"), and Register ("~/register")
    - Similar implementation to Finance pset. These functions work with the users table in movies.db to log different users in and out of the application
3. Quiz pages ("~/quiz", "~/quizQuestion1", "~/quizQuestion2", "~/quizQuestion3", "~/quizQuestion4")
    - Quiz: This page has a simple 'Start quiz' button that routes the user to the first page of the quiz
    - Question 1: This function retrieves the title of the movie that the user picks for this question and adds it to the quizTempData table in movies.db. It then generates another series of random movies based on selection criteria defined in helpers.py and sends those movies to the quizQuestion2 html page. 
    - Question 2: This sends a randomly generated year to the next page, quizQuestion3
    - Question 3: This page takes a random list of movies and chooses a random word out of their titles. It then takes the original list of movie titles and the random words taken from those tables and send that information to quizQuestion4, where the user will pick their favorite word out of the options provided. 
    - Question 4: The actual algorithm for computing the movie recommendations is housed in this function, which ends with the list of movie recommendations being sent to the quizResults.html page. 
    - Movie recommendations algorithm: through querying the quizTempData table in movies.db, we pick movies from the database with similar directors or that were made in the same year as the movies that the user chose. Based on the director/year, we then choose a random movie from the database given these constrained parameters. 
    - Display: We use web scraping here to get the images of the movie posters, which are displayed along with the title on each page of the quiz
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
    - Displaying the recent movie news/movie reviews from the New York Times
7. I'm Feeling Lucky ("/lucky")
    - This is a simple feature that allows the user to be presented with a randomly chosen movie to watch
8. Reviews ("~/reviews"):

### Helpers.py
1. get_details(): 
2. get_reviews() and get_review_details: 
3. DISCUSS HELPER FUNCTIONS FOR QUIZ HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
4. get_poster_url(): this function contacts the IMDB API, searches for the movie title using the API key, and parses the results to return the poster url. The url is then used in the src attribute of the image of the relevant html pages to display the image to the user.   

## Front-end

### Design Process 
We spent a significant amount of time in the ideation process and underwent several brainstorming sessions to discuss how the website would look and how we planned to structure the code. We created a couple low-fidelity prototypes to visualize the page layouts, ultimately choosing the one we implemented. 

### Implementation 
In the implementation of the design, we took advantage of the flex containers and cards in Bootstrap. 
Discuss flex and how it works w a bunch of different screen sizes
Talk about card + grid as well 
Jinja

# Built With
* CS50 IDE
* VSCode 
* Sublime + Terminal
* GitHub
* Bootstrap
* NYT and IMDB 

# References and Resources
* https://developer.nytimes.com/apis
* https://imdb-api.com/
* https://www.w3schools.com/ 
