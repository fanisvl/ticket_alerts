import mysql.connector
from dotenv import load_dotenv
import os
import json # temporary'


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
        title = movie["title"]
        if not movie_exists(title):
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