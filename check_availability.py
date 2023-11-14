from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from database import get_upcoming_movies, set_tickets_available_true, has_tickets_available, get_movie_data, get_alerts, delete_alert
from send_email import send_email

def main():

    """
    Checks ticket availability of all Upcoming Movies, including movies that do not have alerts set up for them. 
    Seperate from check_alerts.py, in order to be ran on a longer interval to save resources.

    Check if any upcoming_movies have tickets available.
    If so, update ticketsAvailable attribute to true.
    """

    # Initialize browser
    op = webdriver.ChromeOptions()
    op.add_argument('headless') 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/WebTicketing/')
    
    # The h5.media-heading selector includes titles in both english & greek
    available_title_elements = driver.find_elements(By.CSS_SELECTOR, "h5.media-heading")
    available_titles = [title.accessible_name for title in available_title_elements]

    # update ticket availability of all upcoming movies
    # *_ is used to ignore the rest of the values inside of each tuple, we only need id, title
    for id, title, *_ in get_upcoming_movies():
        if title in available_titles:
            set_tickets_available_true(title)
    driver.close()

    alerts = get_alerts() # returns a list of tuples: (alert_id, email, movie_title)
    
    for alert in alerts:
        if has_tickets_available(alert["movie_title"]):
            movie_data = get_movie_data(alert["movie_title"])
            send_email(alert["email"], movie_data)
            delete_alert(alert["alert_id"])
            
def clear():
    """Clear terminal scren"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

if __name__ == "__main__":
    main()
