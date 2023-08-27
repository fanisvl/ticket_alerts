from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.villagecinemas.gr/WebTicketing/')

print(driver.title)

cinema = driver.find_element(By.XPATH, "//*[@id=\"cinemaSelection\"]/div/div/div[1]/a")
cinema.click()

movie = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]")
movie.click()

try_dates = ["0831", "0901", "0902", "0903", "0904",
              "0905", "0906", "0907", "0908", "0909",
              "0910","0911","0912","0913","0914","0915",]

new_date_available = False
for try_date in try_dates:
    find = "#date2023" + try_date
    try:
        datepicks = driver.find_element(By.CSS_SELECTOR, find)
        new_date_available = True

    except:
        print("date: " + find + ", was not found.")

print()

if new_date_available:
    print("New date found!")
else:
    print("No new dates yet.")