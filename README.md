# Ticket Alerts
When Oppenheimer was released, finding good seats was quite challenging, so I needed a way to receive email notifications when new tickets became available.
This project provides a solution by allowing users to select any upcoming movie from the Village Cinemas website, enter their email & be notified when tickets become available.


# Components
![graph](https://github.com/fanisvl/ticket_alerts/assets/82032857/84d29eb0-e016-4903-a343-56e495df530e)

## 1. Interval Scripts:
### 1a. scrape_upcoming.py
1. Scrape upcoming movie data from [villagecinemas.com/prosehos](http://villagecinemas.com/prosehos)
2. Store to database → UPCOMING_MOVIES table

### 1b. alert_system.py:
1. Scrape available_titles (tickets available) from https://www.villagecinemas.gr/WebTicketing/
2. If a title from upcoming_movies (database) is in available titles set ticketsAvailable to true (update_availability)
3. Check if any alerts have ticketsAvailable true. If so, send an email notification and delete the alert.  

## 2. Database:
1. Upcoming Movies table (id, title, poster, premiere, trailer)
2. Alerts table (alert_id, email, movie_id)

## 3. Website / Terminal UI
1. Terminal/Website displays upcoming movies from the database.
2. The user selects a movie and enters an email.
3. Store the alert (email, selected_movie) in the database.
