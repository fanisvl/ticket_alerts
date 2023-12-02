from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from database import get_upcoming_movies, set_tickets_available_true, has_tickets_available, \
    get_movie_data, get_alerts, delete_alert
from send_email import send_email


def main():
    """"update_availability and send_alerts are in the same file since they are executed consecutively"""
    update_availability()
    send_alerts()


def update_availability():
    """Scrapes the cinema website to update ticket availability in the database."""

    # Initialize browser
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/WebTicketing/')

    # The h5.media-heading selector includes titles in both english & greek
    available_title_elements = driver.find_elements(By.CSS_SELECTOR, "h5.media-heading")
    available_titles = [title.accessible_name for title in available_title_elements]
    driver.close()

    # Update database ticketAvailability of all upcoming movies
    for movie in get_upcoming_movies():
        if movie["title"] in available_titles:
            set_tickets_available_true(movie["title"])


def send_alerts():
    """Sends alerts for available tickets and deletes them from the database."""

    alerts = get_alerts()  # returns a list of tuples: (alert_id, email, movie_title)
    for alert in alerts:
        if has_tickets_available(alert["movie_title"]):
            movie_data = get_movie_data(alert["movie_title"])
            send_email(alert["email"], movie_data)
            delete_alert(alert["alert_id"])


if __name__ == "__main__":
    main()
