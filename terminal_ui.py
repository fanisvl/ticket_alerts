from pick import pick
from database import get_upcoming_titles, post_alert


def main():

    upcoming_titles = get_upcoming_titles()
    prompt = 'Select an upcoming movie to track: '
    # pick returns tuple (option_picked, index)
    selected_title = pick(upcoming_titles, prompt)[0] 
    print(f"You selected {selected_title}.")

    email = input("Enter your email to be notified: ") or "fanis.vlahogiannis@gmail.com" # default

    # Post (email, tracked_movie_id) to tracked table in db
    post_alert(email, selected_title)

    print(f"\nSuccess! You are now tracking {selected_title}.")

if __name__ == "__main__":
    main()