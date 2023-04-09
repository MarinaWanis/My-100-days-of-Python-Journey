from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html_page = response.text

soup = BeautifulSoup(html_page, 'html.parser')
movie_titles = [movie_name.getText() for movie_name in soup.find_all(name="h3", class_="title")]
movie_list = movie_titles[::-1]
print(movie_list)

with open("movies_list.txt", "w",encoding="utf-8") as file:
    for movie in movie_list:
        print(movie)
        file.write(f"{str(movie)}\n")
