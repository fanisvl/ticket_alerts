# Ticket Availability
When Oppenheimer (2023) released it was quite hard to obtain good seats so I needed a way to receive email notifications the moment new tickets became available.
I'm expanding this project to create a web application that allows users to select any upcoming movie on Village Cinemas, enter their email & be notified when tickets become available.

## Components

1. **Upcoming Movies Scraper**:
    - Scrapes upcoming movies data from the Village Cinemas website.
    - Stores the scraped data in a database.
      
2. **API to Get Upcoming Movies**:
    - Provides an API endpoint to retrieve data for upcoming movies.
      
3. **User Interface**:
    - User selects a movie and enters their email to be notified.
    - Store the user's email and the selected movie in the database.
      
4. **Availability Check Script**:
    - Runs a script at regular intervals to check ticket availability of **tracked** movies.
    - Sends email notifications to users if tickets are available.

## Learning Objectives

- Utilize a headless browser with the Selenium library to gather information from a dynamic website.
- Use the SendGrid API to send email notifications.
- Employ environmental variables to protect secret API keys.
- Utilize a virtual environment and publish a requirements.txt file to achieve reproducible results.
- Run the code on an AWS EC2 instance.
