# Design
PROMPT: Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, 
consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

## Back-end

### Initial Databasing
All of the data from this project draws from the movies.db database, containing information on the movies themselves, the directors, the stars, the ratings for the movies, etc. In addition, we set up several more tables in this database that are continuously updated and modified as the user interacts with our website. See the description of these database below:
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
1. Index ("~/"): discuss function here
2. second function here
3. third function here
4. fourth function here
5. News ("~/news"): 

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
* Bootstrap
* NYT and IMDB 

# References and Resources
* https://developer.nytimes.com/apis
* https://imdb-api.com/
* https://www.w3schools.com/ 
