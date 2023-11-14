from pick import pick
from database import get_upcoming_titles, post_alert, has_tickets_available


def main():

    upcoming_titles = get_upcoming_titles()
    unavailable_tickets = [title for title in upcoming_titles if not has_tickets_available(title)]
    prompt = 'Select an upcoming movie to track: '
    # pick returns tuple (option_picked, index)
    selected_title = pick(unavailable_tickets, prompt)[0] 
    print(f"You selected {selected_title}.")

    email = input("Enter your email to be notified: ") or "fanis.vlahogiannis@gmail.com" # default

    # Post (email, tracked_movie_id) to tracked table in db
    post_alert(email, selected_title)

    print(f"\nSuccess! You are now tracking {selected_title}.")

if __name__ == "__main__":
    main()