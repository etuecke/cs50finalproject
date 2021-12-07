# Design
PROMPT: Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, 
consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

## Back-end

### Initial Databasing
Discuss implementation of SQL databases

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
In the implementation of the design, we 
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
