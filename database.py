import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv("DB_PASS"),
    database="ticket_availability"
)

cursor = db.cursor()


def post_upcoming(movies):
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

def movie_exists(title):
    query = "SELECT COUNT(*) FROM upcoming_movies WHERE title = %s"
    cursor.execute(query, (title,))
    count = cursor.fetchone()[0]
    return count > 0

def get_upcoming_titles():
    query = """SELECT title FROM upcoming_movies"""
    cursor.execute(query)
    upcoming_movies = []
    for movie in cursor:
        upcoming_movies.append(movie)

    return upcoming_movies

def get_id_by_title(title):
    query = f"SELECT id FROM upcoming_movies WHERE title='{title}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        id = result[0]
        return id
    else:
        return None