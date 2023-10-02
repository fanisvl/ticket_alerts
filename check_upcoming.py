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

    #TODO:  Receive upcoming titles from scrape_upcoming
    find_movie = input("Search for movie: ")

    attempt = 0
    while True:
        attempt += 1
        for title in titles:
            if (title.__contains__(find_movie.upper())):
                print(title)
                send_email("fanis.vlahogiannis@gmail.com", "New dates found!", "New dates available")
                print("Movie has been released!")
            else:
                print(" Movie has not released yet")
                wait(10, attempt)
                driver.refresh()

if __name__ == "__main__":
    main()