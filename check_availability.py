from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from send_email import send_email
from terminal_ui import wait
import json
from pick import pick

def main():

    # Initialize browser
    op = webdriver.ChromeOptions()
    # op.add_argument('headless') 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)

    driver.get('https://www.villagecinemas.gr/WebTicketing/')


    available_title_elements = driver.find_elements(By.CSS_SELECTOR, "h5.media-heading")
    available_titles = [title.accessible_name for title in available_title_elements]

    attempt = 0
    movieFound = False

    # Replace with database logic
    while True:
        attempt += 1
        for title in available_titles:
            if title.__contains__(find_movie.upper()):
                movieFound = True

        if movieFound:
            print(find_movie.capitalize() + " found")
            send_email("fanis.vlahogiannis@gmail.com", f"Tickets available for {find_movie.capitalize()}", f"Tickets available for {find_movie.capitalize()}")
            break
        else:
            wait(10, attempt)
            driver.refresh()

if __name__ == "__main__":
    main()