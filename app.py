from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# For email notifications
import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

def main():

    op = webdriver.ChromeOptions()
    op.add_argument('headless') 

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)
    driver.get('https://www.villagecinemas.gr/WebTicketing/')

    cinema = driver.find_element(By.XPATH, "//*[@id=\"cinemaSelection\"]/div/div/div[1]/a")
    cinema.click()

    movie = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]")
    movie.click()

    try_dates = ["0830", "0831", "0901", "0902", "0903", "0904",
                "0905", "0906", "0907", "0908", "0909",
                "0910","0911","0912","0913","0914","0915"]

    new_date_found = False
    for try_date in try_dates:
        find = "#date2023" + try_date
        try:
            find_try_date = driver.find_element(By.CSS_SELECTOR, find)
            new_date_found = True

        except:
            pass

    driver.quit()

    if new_date_found:
        print("== New date found! ==")
        send_email()
    else:
        print("== No new dates yet. == ")

    return new_date_found

def send_email():
    load_dotenv()
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    
    from_email = Email("fanis.vlahogiannis@gmail.com")
    to_email = To("fanis.vlahogiannis@gmail.com")
    subject = "New dates available for Oppenheimer!"
    content = Content("text/plain", "New dates available!")
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    if response.status_code == 202:
        print("Email notification sent!")

if __name__ == "__main__":
    main()