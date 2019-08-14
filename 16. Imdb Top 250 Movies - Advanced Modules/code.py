import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

movie_names = soup.find_all("td", {"class" : "titleColumn"})

ratings = soup.find_all("td", {"class" : "ratingColumn imdbRating"})

rating_level = float(input("Enter rating:"))

for movie, rating in zip(movie_names, ratings):
    
    movie = movie.text
    rating = rating.text
    
    movie = movie.strip()
    movie = movie.replace("\n", "")
    
    rating = rating.strip()
    rating = rating.replace("\n", "")
    
    if(float(rating) > rating_level):
        print("Movie : {}, Rating : {}".format(movie, rating))
