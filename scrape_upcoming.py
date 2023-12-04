from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from database import update_upcoming

# Setup webdriver
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opt)


def scrape_upcoming():
    """
    Scrape upcoming movies from Village Cinema's upcoming movies page and update database.
    """

    upcoming_movie_links = get_upcoming_movie_links('https://www.villagecinemas.gr/el/tainies/prosehos/?pg=0')

    count = 1  # Terminal info
    upcoming_movies = []
    for link in upcoming_movie_links:

        # Terminal info
        clear()
        print(f"Collecting data... {count}/{len(upcoming_movie_links)}")
        print(link + "\n")
        count += 1

        # Get movie data
        upcoming_movies.append(collect_movie_data(link))

    update_upcoming(upcoming_movies)


def get_upcoming_movie_links(url):
    """
    Return a list of movie page links from the provided URL.

    Args:
    url (str): The URL of the page containing movie links.

    Returns:
    List of movie links.
    """

    driver.get(url)
    movie_links = []
    movie_elements = driver.find_elements(By.CSS_SELECTOR, "div[class='box_title'] > h2 > a")
    for movie in movie_elements:
        link = movie.get_attribute("href")
        movie_links.append(link)
    return movie_links


def collect_movie_data(link):
    """
    Collect movie data from the given movie page link.

    Args:
    link (str): Movie page link.

    Returns:
    Dictionary with title, poster, premier, description, genre, and trailer (if found) of the movie."""

    driver.get(link)
    current_movie = {
        "title": driver.find_element(By.CSS_SELECTOR, "#movie_container > div.title2 > h2").accessible_name,
        "poster": driver.find_element(By.CSS_SELECTOR,"#ContentPlaceHolderDefault_ContentPlaceHolder1_movie_3_MainImage").get_attribute("src"),
        "premier": driver.find_element(By.CSS_SELECTOR,"#movie_container > div.details > div.dtls.FloatLeft > div.info > div.info_txt > table > tbody > tr:nth-child(5) > td:nth-child(2)").accessible_name,
        "description": driver.find_element(By.CSS_SELECTOR, ".summary > div:nth-child(2)").text.replace('\n', ' '),
        "genre": driver.find_element(By.CSS_SELECTOR,".info_txt > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2)").accessible_name
    }
    try:
        current_movie["trailer"] = driver.find_element(By.CSS_SELECTOR,"#movie_container > div.video > iframe").get_attribute("src")
    except:
        current_movie["trailer"] = ""

    return current_movie


def clear():
    """"Clear terminal screen"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


if __name__ == "__main__":
    scrape_upcoming()
