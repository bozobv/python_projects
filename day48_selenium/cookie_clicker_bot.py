from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

url = "https://orteil.dashnet.org/cookieclicker/"

chrome_option = webdriver.FirefoxOptions()
chrome_option.add_argument("--incognito")
chrome_option.add_argument("--disable-application-cache")
chrome_option.add_argument("--disable-cache")
driver = webdriver.Firefox(options=chrome_option)

driver.get(url)

consent_cookie = driver.find_element(By.CSS_SELECTOR, value="body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button")
consent_cookie.click()
time.sleep(1)
english_button = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
english_button.click()

time.sleep(2)
cookie_button = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

#product0
time.sleep(2)

while(True):
    for i in range(50):
        cookie_button.click()
    elements = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    try:
        btn = driver.find_element(By.ID, value="upgrade0")
        btn.click()
        elements[-1].click()
    except:
        print(elements)
        continue

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cookiesPerSecond").text
        print(cookie_per_s)
        break

print(cookie_per_s)
    

time.sleep(4)
driver.quit()