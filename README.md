# Ticket Availability
When Oppenheimer (2023) released it was quite hard to obtain good seats so I needed a way to receive email notifications the moment new tickets became available.
I'm expanding this project to create a web application that allows users to select any upcoming movie on Village Cinemas, enter their email & be notified when tickets become available.

# Components

![IMG_20231028_135454](https://github.com/fanisvl/ticket_availability/assets/82032857/ab6de861-bbd7-4f2e-9865-d6215ad30a6d)

## 1. Server Scripts:

### 1a. scrape_upcoming.py
1. Scrape upcoming movie data from [villagecinemas.com/prosehos](http://villagecinemas.com/prosehos)
2. Store to database → UPCOMING_MOVIES table

### 1b. check_availability.py:

1. Scrape available_titles (tickets available) from https://www.villagecinemas.gr/WebTicketing/
3. Check if any available_titles have alerts → from ALERTS table
4. If a match is found send notification.
5. Delete alert → from ALERTS table

## 2. Database:
1. Upcoming Movies table (id, title, poster, premier, trailer)
2. Alerts table (alert_id, email, movie_id)

## 3. Terminal UI / Website
1. User selects an upcoming movie FROM → UPCOMING_MOVIES table
2. User enters email
3. Store alert (email, selected_movie) TO → ALERTS table
