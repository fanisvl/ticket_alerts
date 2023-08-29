from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
driver.get('https://www.villagecinemas.gr/WebTicketing/')

available_movies = driver.find_elements(By.CLASS_NAME, "media-heading")
for movie in available_movies:
    print(movie.accessible_name)
