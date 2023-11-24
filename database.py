import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(buffered=True, dictionary=True)


# Upcoming
def update_upcoming(scraped_movies):
    # Movies that are no longer upcoming should be removed.
    delete_old_upcoming_movies(scraped_movies)
    insert_query = """
                INSERT INTO upcoming_movies (title, poster, premier, trailer, description, genre)
                VALUES (%s, %s, %s, %s, %s, %s)"""
    for movie in scraped_movies:
        if not movie_exists(movie["poster"]):
            data_to_insert = (
                movie["title"],
                movie["poster"],
                movie["premier"],
                movie.get("trailer", None),
                movie["description"],
                movie["genre"]
            )
            cursor.execute(insert_query, data_to_insert)

    db.commit()


def delete_old_upcoming_movies(scraped_movies):
    """ INPUT: scraped_movies from scrape_upcoming.py

        If a title is stored in upcoming_movies database, 
        but not found by scrape_upcoming then it has been released and must be deleted.

    """
    scraped_titles = [movie["title"] for movie in scraped_movies]
    upcoming_titles = get_upcoming_titles()

    movies_to_remove = [title for title in upcoming_titles if title not in scraped_titles]
    for title in movies_to_remove:
        delete_query = "DELETE FROM upcoming_movies WHERE title = %s"
        cursor.execute(delete_query, (title,))
        db.commit()


def movie_exists(poster_url):
    """Returns true if a movie with the same title or a variation (ENG, 3D, DOLBY ATMOS) exists
       by checking for equal post_urls
    """

    query = "SELECT COUNT(*) FROM upcoming_movies WHERE poster = %s"
    cursor.execute(query, (poster_url,))
    count = cursor.fetchone()["count(*)"]
    return count > 0


def get_upcoming_titles():
    return [movie["title"] for movie in get_upcoming_movies()]


def get_upcoming_movies():
    cursor.execute("SELECT * FROM upcoming_movies")
    return cursor.fetchall()


def get_movie_data(title):
    query = "SELECT * FROM upcoming_movies WHERE title = %s"
    cursor.execute(query, (title,))
    return cursor.fetchone()


def set_tickets_available_true(title):
    query = "UPDATE upcoming_movies SET ticketsAvailable = 1 WHERE title = %s"
    cursor.execute(query, (title,))
    db.commit()


def has_tickets_available(title):
    query = "SELECT (ticketsAvailable) FROM upcoming_movies WHERE title = %s"
    cursor.execute(query, (title,))
    return cursor.fetchone()["ticketsAvailable"]


# Alerts
def post_alert(email, title):
    insert_query = "INSERT INTO alerts (email, movie_title) VALUES (%s, %s)"
    cursor.execute(insert_query, (email, title))
    db.commit()



def delete_alert(id):
    query = "DELETE FROM alerts WHERE alert_id = %s"
    cursor.execute(query, (id,))
    db.commit()


def get_alerts():
    """Returns tuple of alerts table rows. Format: (alert_id, email, movie_id)"""

    query = "SELECT * FROM alerts"
    cursor.execute(query)
    alerts = []
    for alert in cursor:
        alerts.append(alert)
    return alerts


#  Movie Title <> Movie ID
def get_movie_id_by_title(title):
    query = "SELECT id FROM upcoming_movies WHERE title = %s"
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    if result:
        id = result["id"]
        return id
    else:
        return None


def get_movie_title_by_id(id):
    query = "SELECT title FROM upcoming_movies WHERE id= %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result:
        title = result["title"]
        return title
    else:
        return None
