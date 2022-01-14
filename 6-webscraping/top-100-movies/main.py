import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Requests html page and makes soup
response = requests.get(URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

# Finds movies names tags
movie_tags = soup.find_all(name="h3", class_="title")
# Creates list of movies
movies = [tag.text for tag in movie_tags]
# Reverses list, since it's upside down
movies.reverse()
print(movies)

# Creates txt file with movies, ads /n to creates new line in each movie on list
with open("movies.txt", "a") as file:
    for movie in movies:
        file.write(movie+"\n")
