from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import os

#url = "https://hu.wikipedia.org/wiki/Kezd%C5%91lap"
url = "http://secure-retreat-92358.herokuapp.com/"

chrome_option = webdriver.FirefoxOptions()
#temp_dir = "day48_selenium/temp"
#os.makedirs(temp_dir, exist_ok=True)
#chrome_option.add_argument(f"--user-data-dir={temp_dir}")
driver = webdriver.Firefox(options=chrome_option)
driver.get(url)

def click_stats():
    stats = driver.find_element(By.CSS_SELECTOR, value="#mw-content-text > div.mw-content-ltr.mw-parser-output > table.mainpage-welcome > tbody > tr > td.welcometext > p > a:nth-child(4)")
    stats.click()

def click_directly():
    link = driver.find_element(By.LINK_TEXT, value="Wikidézet")
    link.click()

def use_search():
    fake_btn = driver.find_element(By.CSS_SELECTOR, value="#p-search > a")
    fake_btn.click()
    time.sleep(1)

    search = driver.find_element(By.NAME, value="search")
    #print(search)
    search.send_keys("Python", Keys.ENTER )
    #search.send_keys(Keys.ENTER)

def registrate():

    fname = driver.find_element(By.NAME, value="fName")
    lname = driver.find_element(By.NAME, value="lName")
    email = driver.find_element(By.NAME, value="email")

    fname.send_keys("Aladár")
    lname.send_keys("Kolbász")
    email.send_keys("kolbaszhuszar89@hurka.hu", Keys.ENTER)
    time.sleep(1)
    

registrate()

time.sleep(5)
driver.quit()


