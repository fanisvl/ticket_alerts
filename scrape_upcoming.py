from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def main():
    op = webdriver.ChromeOptions()
    op.add_argument('headless') 

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/el/tainies/prosehos/')

# Scrape data of upcoming movies
# Data needed:
# - Movie title in english
# - Poster image link
# - Release date