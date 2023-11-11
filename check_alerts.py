from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from send_email import send_email
import os
from database import get_alerts, delete_alert, set_tickets_available_true

def main():

    """
    Check if any movies with alerts have tickets available.
    If so, send an email notification and delete the alert.

    Less resource intensive than update_availability.py
    Runs on a small interval to send notifications quickly 
    """

    alerts = get_alerts() # returns a list of tuples: (alert_id, email, movie_title)
    if (len(alerts) == 0): exit()

    # Initialize browser
    op = webdriver.ChromeOptions()
    op.add_argument('headless') 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/WebTicketing/')
    
    # The h5.media-heading selector includes titles in both english & greek
    available_title_elements = driver.find_elements(By.CSS_SELECTOR, "h5.media-heading")
    available_titles = [title.accessible_name for title in available_title_elements]

    for (alert_id, email, title) in alerts:
        if title in available_titles:
            send_email(email, f"Tickets available for {title.capitalize()}", "Tickets now available!")
            set_tickets_available_true(title)
            delete_alert(alert_id)
    driver.close()

def clear():
    """Clear terminal scren"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

if __name__ == "__main__":
    main()
