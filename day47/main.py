from datetime import datetime, time
from pprint import pprint
import requests
from bs4 import BeautifulSoup 
import smtplib
from dotenv import load_dotenv
import os

song_of_ice_and_fire = "https://www.amazon.com/Thrones-Clash-Kings-Swords-Dragons/dp/1101965487/ref=tmm_hrd_swatch_0?_encoding=UTF8&dib_tag=se&dib=eyJ2IjoiMSJ9.2Dj5bEi2e71cp67yjuGvxyZOX_XYKaEvmS2UHDQwKCKUgHmBnx3-NPSYarQFuEI4fdU-pgVryfPhZ_haLCk9j-t2TGEaUS-oU0MWWTtVujhKujV4tifcIT-VEfnQGsmdy9gpajc8xn6a3t4X9rx20zo1v8iDY8SbYq4tLALo1TOh8W33DdSAIG_lE8bEatJRd_KzJkvKu6-sFURZ0289NsEssHtpC2DKJyxZ8SKgNlw.pWUCZ-zwHi1O4hiP1uzmgO0xg43Kb8HhXwz5WnOFXws&qid=1728589079&sr=8-1&language=en_US&currency=EUR"
test = "https://appbrewery.github.io/instant_pot/"
product_name = "KONYVEK"
# ez lesz a class : a-price-whole
product_url = song_of_ice_and_fire

header = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept-Language" : "hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding" : "gzip, deflate, br",
    "upgrade-insecure-requests" : "1",
    "sec-fetch-dest" : "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "te": "trailers",
    "csm-hit": "",
    "i18n-prefs": "EUR",
    "lc-main": "en_US",
    "session-id": "",
    "session-id-time": "",
    "session-token":"",
    "sp-cdn": "\"L5Z9:HU\"" ,
    "ubid-main": ""
}

def get_price():

    response = requests.get(product_url, headers=header)
    web_page = response.text

    soup = BeautifulSoup(web_page, "html.parser")
    print(soup)
    price = soup.find(class_ = "a-price-whole")
    return int(price.text.strip("."))

def must_buy(actual_price, goto_price):
    if goto_price >= actual_price:
        return True
    return False

def send_mail(price, product):
    load_dotenv()

    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        print("connection")
        connection.starttls() 
        print("tls")

        connection.login(user=os.getenv("EMAIL"), password=os.getenv("PW"))  
        print("login")
        subject = "VEDD MEG"
        body = f"Teso, le van arazva a cucc, itt az ido, a(z) {product_name} ara most CSAK {price}!!!!!!"
        msg = f"Subject: {subject}\n\n{body}"

        # E-mail küldése
        connection.sendmail(from_addr=os.getenv("EMAIL"), to_addrs="bozo.balint.vid@gmail.com", msg=msg)
        print("E-mail sikeresen elküldve")
    except Exception as e:
        print(f"Hiba történt: {e}")
    finally:
        connection.quit()  # Kapcsolat bezárása


price = get_price()

if must_buy(actual_price=price, goto_price=100):
    send_mail(price=price, product=product_name)