from bs4 import BeautifulSoup
#import lxmls   
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")

movies = []

for title in reversed(titles):
    movies.append(title.text)
    # print(title.text.split(" ", 1)[1]) #ha csak a szöveg kéne

with open("day45_soup/top_100_movies.txt", "w") as file:
    for item in movies:
        file.write(item + "\n")
