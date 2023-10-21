from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os 
from post_upcoming import post_upcoming

def scrape_upcoming():
    op = webdriver.ChromeOptions()
    #op.add_argument('headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/el/tainies/prosehos/')


    find_movies = driver.find_elements(By.CSS_SELECTOR, "div[class='box_title'] > h2 > a")
    movie_links = []

    # Grab movie links
    for movie in find_movies:
        link = movie.get_attribute("href")
        movie_links.append(link)


    count = 1 # For terminal info
    total_links = len(movie_links)
    movies = []
    for link in movie_links:
        
        # Terminal info
        clear()
        print("Collecting data... " + str(count) + "/" + str(total_links))
        count += 1

        # Collect data
        print(link)
        print()
        driver.get(link)
        movie_data = {}
        try: 
            movie_data["title"] = driver.find_element(By.CSS_SELECTOR, "#movie_container > div.title2 > h2").accessible_name
            movie_data["poster"] = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolderDefault_ContentPlaceHolder1_movie_3_MainImage").get_attribute("src")
            movie_data["premier"] = driver.find_element(By.CSS_SELECTOR, "#movie_container > div.details > div.dtls.FloatLeft > div.info > div.info_txt > table > tbody > tr:nth-child(5) > td:nth-child(2)").accessible_name
            movie_data["trailer"] = driver.find_element(By.CSS_SELECTOR, "#movie_container > div.video > iframe").get_attribute("src")
        except:
            warning_log = open("scrape_upcoming_warning_log.txt", "a")
            warning_log.write(f"{movie_data['title']} - Could not collect all data for this movie")
        movies.append(movie_data)

    post_upcoming(movies)


def clear():
    """"Clear terminal screen"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

if __name__ == "__main__":
    scrape_upcoming()