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
    driver.get('https://www.villagecinemas.gr/el/tainies/prosehos/?pg=0')

    # Grab first page movie links
    movie_links = find_movie_links()

    # Grab second page links
    # Assuming that when there's no second page, there is no '02' page link
    # Assuming no more than 2 pages (40 upcoming movies)
    try:
        go_to_second_page = driver.find_element(By.CSS_SELECTOR,
                                                "#ContentPlaceHolderDefault_ContentPlaceHolder1_movies_comingsoon_Pager_lvPager_hnum_1")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to bottom
        go_to_second_page.click()

        # Grab second page movie links
        movie_links.extend(find_movie_links())
    except:
        pass  # No second page

    count = 1  # For terminal info
    movie_data = []
    for link in movie_links:

        # Terminal info
        clear()
        print(f"Collecting data... {count}/{len(movie_links)}")
        count += 1

        # Collect data
        print(link)
        print()
        driver.get(link)
        current_movie = {}
        try:
            current_movie["title"] = driver.find_element(By.CSS_SELECTOR,
                                                         "#movie_container > div.title2 > h2").accessible_name
        except:
            current_movie["title"] = ""

        try:
            current_movie["poster"] = driver.find_element(By.CSS_SELECTOR,
                                                          "#ContentPlaceHolderDefault_ContentPlaceHolder1_movie_3_MainImage").get_attribute(
                "src")
        except:
            current_movie["poster"] = ""

        try:
            current_movie["premier"] = driver.find_element(By.CSS_SELECTOR,
                                                           "#movie_container > div.details > div.dtls.FloatLeft > div.info > div.info_txt > table > tbody > tr:nth-child(5) > td:nth-child(2)").accessible_name
        except:
            current_movie["premier"] = ""

        try:
            current_movie["trailer"] = driver.find_element(By.CSS_SELECTOR,
                                                           "#movie_container > div.video > iframe").get_attribute("src")
        except:
            current_movie["trailer"] = ""

        try:
            current_movie["description"] = driver.find_element(By.CSS_SELECTOR,
                                                               ".summary > div:nth-child(2)").text.replace('\n', ' ')
        except:
            current_movie["description"] = ""

        try:
            current_movie["genre"] = driver.find_element(By.CSS_SELECTOR,
                                                         ".info_txt > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2)").accessible_name
        except:
            current_movie["genre"] = ""
        movie_data.append(current_movie)
    update_upcoming(movie_data)


def find_movie_links():
    """Returns list of movie links movie_links"""
    movie_links = []
    find_movies = driver.find_elements(By.CSS_SELECTOR, "div[class='box_title'] > h2 > a")

    for movie in find_movies:
        link = movie.get_attribute("href")
        movie_links.append(link)

    return movie_links


def clear():
    """"Clear terminal screen"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


if __name__ == "__main__":
    scrape_upcoming()
