from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from send_email import send_email

from time import sleep
from terminal_ui import wait



def main():


    # Initialize browser
    op = webdriver.ChromeOptions()
    # op.add_argument('headless') 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=op)

    driver.get('https://www.villagecinemas.gr/WebTicketing/')
    cinema = driver.find_element(By.XPATH, "//*[@id=\"cinemaSelection\"]/div/div/div[1]/a")
    cinema.click()
    try:
        movie = driver.find_element(By.CSS_SELECTOR, "div[data-vc-movie='HO00105706']")
        movie.click()
    except:
        print("Movie not found")
        exit()

    attempt = 0
    while True:
        attempt+=1
        # Should be implemented using dates library
        try_dates = ["1005"]
        new_date_found = False
        for try_date in try_dates:
            find = "#date2023" + try_date
            try:
                driver.find_element(By.CSS_SELECTOR, find)
                new_date_found = True
            except:
                pass

        if new_date_found:
            print("== New date found! ==")
            send_email("fanis.vlahogiannis@gmail.com", "New dates found!", "New dates available")
            break
        else:
            print("== No new dates yet. == ")
            wait(10, attempt)
            driver.refresh()


if __name__ == "__main__":
    main()