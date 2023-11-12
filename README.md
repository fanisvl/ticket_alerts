# Ticket Alerts
When Oppenheimer (2023) was released it was quite hard to obtain good seats so I needed a way to receive email notifications the moment new tickets became available.
I'm expanding this project to create a web application that allows users to select any upcoming movie on Village Cinemas, enter their email & be notified when tickets become available.

# Components
![graph](https://github.com/fanisvl/ticket_availability/assets/82032857/9c1b9564-b42b-4e2f-a0e0-06b2a81505c9)

## 1. Interval Scripts:

### 1a. scrape_upcoming.py
1. Scrape upcoming movie data from [villagecinemas.com/prosehos](http://villagecinemas.com/prosehos)
2. Store to database → UPCOMING_MOVIES table

### 1b. check_all.py
Check ticket availability of all Upcoming Movies, including movies that do not have alerts set up for them.
Separate from check_alerts.py, in order to be run on a longer interval to save resources.

### 1c. check_alerts.py:
1. Scrape available_titles (tickets available) from https://www.villagecinemas.gr/WebTicketing/
3. Check if any available_titles have alerts → from ALERTS table
4. If a match is found send a notification.
5. Delete alert → from ALERTS table

## 2. Database:
1. Upcoming Movies table (id, title, poster, premiere, trailer)
2. Alerts table (alert_id, email, movie_id)

## 3. Website / Terminal UI
1. Terminal/Website displays upcoming movie FROM → UPCOMING_MOVIES table
2. The user selects a movie, enters email
3. Store alert (email, selected_movie) TO → ALERTS table
