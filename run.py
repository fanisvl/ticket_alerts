import json
from pick import pick


def main():
    # Read upcoming_movies.json (created by scrape_upcoming.py)
    upcoming_movies = json.load(open("upcoming_movies.json"))
    upcoming_titles = []
    for movie in upcoming_movies:
        upcoming_titles.append(movie["title"])

    upcoming_titles.append("Oppenheimer") # for testing

    # Select from upcoming_titles using pick 
    title = 'Select an upcoming movie to track: '
    track_movie = pick(upcoming_titles, title)[0] # returns tuple (option_picked, index)

    email = input("Enter your email to be notified: ") or "fanis.vlahogiannis@gmail.com" # if no input is entered
    return (track_movie, email)


if __name__ == "__main__":
    main()