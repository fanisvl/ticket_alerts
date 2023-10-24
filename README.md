# Ticket Availability
When Oppenheimer (2023) released it was quite hard to obtain good seats so I needed a way to receive email notifications the moment new tickets became available.
I'm expanding this project to create a web application that allows users to select any upcoming movie on Village Cinemas, enter their email & be notified when tickets become available.

# Components

## A. scrape_upcoming.py:

1. Scrape upcoming movie data from [villagecinemas.com/prosehos](http://villagecinemas.com/prosehos) **:** *Title, Poster URL, Premier Date, Trailer URL
2. Store data to database → UPCOMING_MOVIES table 

## B. Terminal UI:

1. User selects an upcoming movie FROM → UPCOMING_MOVIES table
2. User enters email
3. Store email & selected movie TO → ALERTS table

## C. check_availability.py:

1. Scrape available_titles
2. Check if available_titles contain titles with alerts → from ALERTS table
3. If a match is found send notification.
4. Delete alert → from ALERTS table