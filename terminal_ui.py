from pick import pick
from database import get_upcoming_titles, get_id_by_title, post_tracked


def main():

    upcoming_titles = get_upcoming_titles()
    prompt = 'Select an upcoming movie to track: '
    # pick returns tuple (option_picked, index)
    selected_title = pick(upcoming_titles, prompt)[0] 

    email = input("Enter your email to be notified: ") or "fanis.vlahogiannis@gmail.com" # default

    # Post (email, tracked_movie_id) to tracked table in db
    selected_id = get_id_by_title(selected_title)
    post_tracked(email, selected_id)

    print(f"\n Success! You are now tracking {selected_title}.")
    


if __name__ == "__main__":
    main()