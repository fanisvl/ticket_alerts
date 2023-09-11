import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

def send_email(to_email, subject, content):
    load_dotenv()
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    
    from_email = Email("fanis.vlahogiannis@gmail.com")
    mail = Mail(from_email, To(to_email), subject, Content("text/plain", content))

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    if response.status_code == 202:
        print("Email notification sent!")
    else:
        print("Error sending email: " + response.status_code)