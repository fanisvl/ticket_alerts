from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from send_email import send_email

from terminal_ui import wait

def main():
    # Initialize browser
    op = webdriver.ChromeOptions()
    # op.add_argument('headless') 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)

    driver.get('https://www.villagecinemas.gr/WebTicketing/')

    #TODO:  Receive upcoming titles from scrape_upcoming

    titles = driver.find_elements(By.CSS_SELECTOR, "h5.media-heading")
    titles = [title.accessible_name for title in titles]
    find_movie = input("Search for movie: ")
    for title in titles:
        if (title.__contains__(find_movie.upper())):
            print(title)
            print("Found!")

if __name__ == "__main__":
    main()