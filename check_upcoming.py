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


    titles = driver.find_elements(By.CSS_SELECTOR, "h5.media-heading")
    titles = [title.accessible_name for title in titles]

    #TODO:  Read upcoming_titles from a json file format (produced by scrape_upcoming)

    #TODO: Use pick library to search 
    find_movie = input("Search for movie: ")

    attempt = 0
    movieFound = False
    while True:
        attempt += 1
        for title in titles:
            if title.__contains__(find_movie.upper()):
                movieFound = True

        if movieFound:
            print(find_movie.capitalize() + " found")
            send_email("fanis.vlahogiannis@gmail.com", "New dates found!", "New dates available")
            break
        else:
            wait(10, attempt)
            driver.refresh()

if __name__ == "__main__":
    main()