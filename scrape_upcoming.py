from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def main():
    op = webdriver.ChromeOptions()
    # op.add_argument('headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/el/tainies/prosehos/')

    movies = []

    movie = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolderDefault_ContentPlaceHolder1_movies_comingsoon_lvItems_ctrl0_box_mov_titlegr_0")
    movie.click()  
    movie_data = {}
    movie_data["title"] = driver.find_element(By.CSS_SELECTOR, "#movie_container > div.title2 > h2").accessible_name
    movie_data["poster"] = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolderDefault_ContentPlaceHolder1_movie_3_MainImage").get_attribute("src")
    movie_data["premier"] = driver.find_element(By.CSS_SELECTOR, "#movie_container > div.details > div.dtls.FloatLeft > div.info > div.info_txt > table > tbody > tr:nth-child(5) > td:nth-child(2)").accessible_name
    movies.append(movie_data)

    print(movies)


if __name__ == "__main__":
    main()