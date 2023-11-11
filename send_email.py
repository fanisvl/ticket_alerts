import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

def send_email(to_email, movie_data):
    load_dotenv()
    sg = SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    mail = Mail("fanis.vlahogiannis@gmail.com", To(to_email))
    mail.dynamic_template_data = {
        'title': movie_data["title"],
        'poster_url': movie_data["poster"]
    }
    mail.template_id = "d-fbe233faec3f497980238d7fab9cca7e"
    try:
        response = sg.send(mail)
        if response.status_code == 202:
            print
    except Exception as e:
        print(e)