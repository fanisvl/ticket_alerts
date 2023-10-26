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

cursor = db.cursor(buffered=True)

# Upcoming
def update_upcoming(movies):
    # Movies that are no longer upcoming should be removed.
    delete_released_movies(movies)
    insert_query = """
                INSERT INTO upcoming_movies (title, poster, premier, trailer)
                VALUES (%s, %s, %s, %s)"""
    for movie in movies:
        if not movie_exists(movie["title"]):
            data_to_insert = (
                movie["title"],
                movie["poster"],
                movie["premier"],
                movie.get("trailer", None)
            )
            cursor.execute(insert_query, data_to_insert)

    db.commit()

def delete_released_movies(movies):
    
    upcoming_titles = [movie["title"] for movie in movies]
    cursor.execute("SELECT title FROM upcoming_movies")
    stored_titles = [row[0] for row in cursor.fetchall()]
    movies_to_remove = [title for title in stored_titles if title not in upcoming_titles]
    for title in movies_to_remove:
        delete_query = f"DELETE FROM upcoming_movies WHERE title = {title}"
        cursor.execute(delete_query)
        db.commit()

def movie_exists(title):
    query = "SELECT COUNT(*) FROM upcoming_movies WHERE title = %s"
    cursor.execute(query, (title,))
    count = cursor.fetchone()[0]
    return count > 0

def get_upcoming_titles():
    query = """SELECT title FROM upcoming_movies"""
    cursor.execute(query)
    upcoming_titles = []
    for movie in cursor:
        upcoming_titles.append(movie[0])

    return upcoming_titles

# Alerts
def post_alert(email, id):
    insert_query =  "INSERT INTO alerts (email, movie_id) VALUES (%s, %s)"
    cursor.execute(insert_query, (email, id))
    db.commit()

def delete_alert(id):
    query = f"DELETE FROM alerts WHERE alert_id = {id}"
    cursor.execute(query)
    db.commit()

def get_alerts():
    """Returns tuple of alerts table rows. Format: (alert_id, email, movie_id)"""

    query = "SELECT * FROM alerts"
    cursor.execute(query)
    alerts = []
    for alert in cursor:
        alerts.append(alert)
    return alerts

#  Title <> ID
def get_id_by_title(title):
    query = f"SELECT id FROM upcoming_movies WHERE title='{title}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        id = result[0]
        return id
    else:
        return None
    
def get_title_by_id(id):
    query = f"SELECT title FROM upcoming_movies WHERE id='{id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        title = result[0]
        return title
    else:
        return None
