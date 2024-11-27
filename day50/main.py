from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

url = "https://tinder.com/app/profile"
USERNAME = ""
PASSWORD = ""


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("geo.prompt.testing", True)
firefox_profile.set_preference("geo.prompt.testing.allow", True)

firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = firefox_profile

driver = webdriver.Firefox(options=firefox_options)
driver.get(url)

time.sleep(2)

login_btn = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div")
login_btn.click()
time.sleep(3)

facebook_btn = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div")
facebook_btn.click()
time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

username_inp = driver.find_element(By.CSS_SELECTOR, value="#email")
pw_inp = driver.find_element(By.CSS_SELECTOR, value="#pass")

username_inp.send_keys(USERNAME)
pw_inp.send_keys(PASSWORD, Keys.ENTER)

time.sleep(8)
cont_btn = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div/div/div")
print("gomb megvans")
cont_btn.click()
print("gombra ranyomva")
driver.switch_to.window(base_window)
time.sleep(8)

location_allow_btn = driver.find_element(By.CSS_SELECTOR, value="div.Bgc\(\$c-ds-background-primary\):nth-child(3) > button:nth-child(1) > div:nth-child(2) > div:nth-child(3)")
location_allow_btn.click()
time.sleep(2)

no_notif_btn = driver.find_element(By.CSS_SELECTOR, value="button.c1p6lbu0:nth-child(2) > div:nth-child(2) > div:nth-child(3)")
no_notif_btn.click()

# Készíts ActionChains objektumot
actions = ActionChains(driver)

while True:
    time.sleep(2)
    try:
        # Nyomd meg a jobbra nyilat
        actions.send_keys(Keys.ARROW_RIGHT).perform()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        # For "Tinder Gold" pop-up
        except NoSuchElementException:
            close_tinder_gold = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div[2]/div[2]/button")
            close_tinder_gold.click()
    


time.sleep(300)



driver.quit