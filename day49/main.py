from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

USERNAME = ""
PW = ""

def login(login_name, user_inp_name, pw_inp_name):
    try:
        print("egy")
        login_with_email_btn = driver.find_element(By.CSS_SELECTOR, value=login_name)
        login_with_email_btn.click()
        print("kettő")
        time.sleep(0.1)

        email_input = driver.find_element(By.CSS_SELECTOR, value=user_inp_name)
        pw_input = driver.find_element(By.CSS_SELECTOR, value=pw_inp_name)

        email_input.send_keys(USERNAME)
        pw_input.send_keys(PW, Keys.ENTER)
        return False
    except:
        print("három")
        return True


url = "https://www.linkedin.com/jobs/search/?currentJobId=4028427455&f_AL=true&geoId=106079947&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_option = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=chrome_option)
driver.get(url)

if login(".sign-in-modal__outlet-btn", "#base-sign-in-modal_session_key", "#base-sign-in-modal_session_password"): 
    time.sleep(2)
    login(".sign-in-form__sign-in-cta", "#username", "#password" )
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4028427455&distance=25&f_AL=true&geoId=106079947&keywords=python%20developer&origin=JOBS_HOME_SEARCH_CARDS")   

time.sleep(5)
#ember176
#ember176.ember-view.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item

joblist = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
print(joblist)

easy_apply_btn = driver.find_element(By.CSS_SELECTOR, value='button.jobs-apply-button.artdeco-button')

for job in joblist:

    easy_apply_btn.click()
    try:
        time.sleep(3)
        telephone_input = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        telephone_input.send_keys("12345678")
        time.sleep(3)
      
        next_btn = driver.find_element(By.CSS_SELECTOR, value="button[aria-label*=Continue]")
        next_btn.click()
        time.sleep(3)

        next_btn.click()
        time.sleep(3)
        
        next_btn.click()
    except Exception:
        exit_btn = driver.find_element(By.CSS_SELECTOR, value="button[aria-label*=Elvetés]")
        exit_btn.click()
        time.sleep(3)
        discard_btn = driver.find_element(By.CSS_SELECTOR, value="button.artdeco-modal__confirm-dialog-btn:first-of-type")
        discard_btn.click()
    
    job.click()




time.sleep(200)
driver.quit()