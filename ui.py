import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pick import pick

op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
driver.get('https://www.villagecinemas.gr/WebTicketing/')

# Available movies are objects
available_movies = driver.find_elements(By.CLASS_NAME, "media-heading")

# Titles are strings
titles = []
for movie in available_movies:
    titles.append(movie.accessible_name)

selected_title = pick(titles, "Select a movie: ")


# Search for movie object that matches selected_title
selected_movie = available_movies[0]
for movie in available_movies:
    if movie.accessible_name == selected_title:
        selected_movie = movie
        break

selected_movie.click()

time.sleep(5)


