# Ticket Alerts
When Oppenheimer was released, obtaining good seats was quite challenging, so I needed a method to receive email notifications the moment new tickets became available.
This project provides a solution to that problem by allowing users to select any upcoming movie from the Village Cinemas website, enter their email & be notified when tickets become available.

# Components


## 1. Interval Scripts:
![IMG_20231114_183820](https://github.com/fanisvl/ticket_alerts/assets/82032857/6702c4f1-5740-44a8-bcc5-c76d12e1f013)


### 1a. scrape_upcoming.py
1. Scrape upcoming movie data from [villagecinemas.com/prosehos](http://villagecinemas.com/prosehos)
2. Store to database → UPCOMING_MOVIES table

### 1b. check_availability.py:
1. Scrape available_titles (tickets available) from https://www.villagecinemas.gr/WebTicketing/
2. If a title from upcoming_movies (database) is in available titles set ticketsAvailable to true.
5. Check if any alerts have ticketsAvailable true
6. If so, send an email notification and delete the alert.  

## 2. Database:
1. Upcoming Movies table (id, title, poster, premiere, trailer)
2. Alerts table (alert_id, email, movie_id)

## 3. Website / Terminal UI
1. Terminal/Website displays upcoming movie FROM → UPCOMING_MOVIES table
2. The user selects a movie, enters email
3. Store alert (email, selected_movie) TO → ALERTS table
