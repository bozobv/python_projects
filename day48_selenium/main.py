from selenium import webdriver
from selenium.webdriver.common.by import By


book_url = "https://www.amazon.com/Thrones-Clash-Kings-Swords-Dragons/dp/1101965487/ref=tmm_hrd_swatch_0?_encoding=UTF8&dib_tag=se&dib=eyJ2IjoiMSJ9.2Dj5bEi2e71cp67yjuGvxyZOX_XYKaEvmS2UHDQwKCKUgHmBnx3-NPSYarQFuEI4fdU-pgVryfPhZ_haLCk9j-t2TGEaUS-oU0MWWTtVujhKujV4tifcIT-VEfnQGsmdy9gpajc8xn6a3t4X9rx20zo1v8iDY8SbYq4tLALo1TOh8W33DdSAIG_lE8bEatJRd_KzJkvKu6-sFURZ0289NsEssHtpC2DKJyxZ8SKgNlw.pWUCZ-zwHi1O4hiP1uzmgO0xg43Kb8HhXwz5WnOFXws&qid=1728589079&sr=8-1&language=en_US&currency=EUR"
python_url = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(python_url)
#driver.get(book_url)

#price_eur = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

#print(f"ennyibe kerül: {price_eur.text}.{price_cent.text}")

def learn():
    search_bar = driver.find_element(By.NAME, value="q")
    print(search_bar.tag_name)
    print(search_bar.get_attribute("placeholder"))

    button = driver.find_element(By.ID, value="submit")
    print(button.size)

    docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    print(docs_link.text)

    bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    print(bug_link.text)

def python_events():
    #content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1) > time > span
    dates = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time")
    events = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a")

    da_dict = {i:[{"date": dates[i].text, "event": events[i].text}] for i in range(len(dates))}

    print(da_dict)


python_events()


# close a page
#driver.close()
# quit the program
driver.quit()

