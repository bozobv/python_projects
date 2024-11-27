from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.instagram.com/accounts/login/"
TARGET_URL = "https://www.instagram.com/rubiconmagazin/"
USERNAME = ""
PASSWORD = ""

class InstaFollower():

    def __init__(self):
        firefox_profile = webdriver.FirefoxProfile()

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.profile = firefox_profile

        self.driver = webdriver.Firefox(options=firefox_options)

    def login(self):
        self.driver.get(URL)

        deny_cookie_css = 'button._a9--:nth-child(3)'
        email_css = "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        pw_css = "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        login_btn_css = "._acap"
        skip_save_btn_css = "div.x1i10hfl"
        skip_notif_btn_css = "button._a9--:nth-child(2)"

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, deny_cookie_css))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, email_css))).send_keys(USERNAME)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, pw_css))).send_keys(PASSWORD)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_btn_css))).click()
        #time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_save_btn_css))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, skip_notif_btn_css))).click()

        print("login done")
        


    def find_followers(self):
        self.driver.get(TARGET_URL)
        followers_css = "li.xl565be:nth-child(2) > div:nth-child(1) > a:nth-child(1)"
        num_of_followers_css = "li.xl565be:nth-child(2) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)"
        
        # getting the num of followers
        # wait for display
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,num_of_followers_css )))
        
        # catch the element
        num_of_followers_element = self.driver.find_element(By.CSS_SELECTOR, value=num_of_followers_css)  
        print(num_of_followers_element)     
        
        # get the title, witch is littered with space 
        title_text = num_of_followers_element.get_attribute("title")
        print(title_text)
        # strip to a number
        num_of_followers = int(title_text.replace("\u00a0", "").strip())
        print(num_of_followers)

        # click on followers
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, followers_css))).click()
        # wait for display
        time.sleep(2)

        # if following is unsuccsesful, not skipping profile
        succes = True
        # scroll by every 3 users
        for i in range(1, num_of_followers, 3):
            if i <= num_of_followers - 3:
                scroll_follow_button = self.driver.find_element(By.CSS_SELECTOR, f'div.x1dm5mii:nth-child({i}) button')
                self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_follow_button)
                #go through every follow btn
                j = i
                while j < j+3:
                    time.sleep(1)

                    succes = self.follow(j)
                    print(succes)
                    if succes == True:
                        j += 1
                    
            else:
                 print("ide nem kéne eljutni most")
                 #TODO lekezelni
                 pass 
        time.sleep()
        
        print("finding")

    def follow(self, num_to_follow):
        print(num_to_follow)
        try:
            btn_to_follow = self.driver.find_element(By.CSS_SELECTOR, f'div.x1dm5mii:nth-child({num_to_follow}) button')
            btn_to_follow.click()
            print("follow done")
            return True
        except ElementClickInterceptedException:
            btn_to_press = self.driver.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(2)")
            btn_to_press.click()
            print("follow shit happened")
            return False

instabot = InstaFollower()
    
instabot.login()
instabot.find_followers()
instabot.follow()

#
#time.sleep(500)
#driver.quit()
#