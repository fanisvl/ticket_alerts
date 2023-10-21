import mysql.connector
from dotenv import load_dotenv
import os
import json # temporary


def post_upcoming(movies):

    load_dotenv()
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv("DB_PASS"),
        database="ticket_availability"
    )

    cursor = db.cursor()

    insert_query = """
                INSERT INTO upcoming_movies (title, poster, premier, trailer)
                VALUES (%s, %s, %s, %s)"""

    for movie in movies:
        data_to_insert = (
            movie["title"],
            movie["poster"],
            movie["premier"],
            movie.get("trailer", None)
        )
        cursor.execute(insert_query, data_to_insert)

    db.commit()