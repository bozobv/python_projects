from os import supports_bytes_environ
import smtplib
import datetime as dt
import pandas as pd

def email_example():
    my_email = "lajosteszt5@gmail.com"
    password = "neeagooemttjyrvw"
    
    # Csatlakozás az SMTP szerverhez a 587-es porton 
    # Az 587-es port ami az email
    print("asd")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # TLS titkosítás indítása
        connection.login(user=my_email, password=password)  # Bejelentkezés

        # Az üzenet formátuma
        subject = "Teszt üzenet"
        body = "Ez egy teszt üzenet"
        msg = f"Subject: {subject}\n\n{body}"

        # E-mail küldése
        connection.sendmail(from_addr=my_email, 
                            to_addrs="bozo.balint.vid@gmail.com", 
                            msg=msg)
        print("E-mail sikeresen elküldve")

def datetime_example():
    now = dt.datetime.now()
    year = now.year
    print(year)
    
    date_of_birth = dt.datetime(year=1999, month=12, day=11)
    print(date_of_birth)

def motivational_email_sender():
    current_weekday = dt.datetime.now().weekday()
    print(current_weekday)
    
    df = pd.read_csv("day32\Birthday Wisher (Day 32) start\quotes.txt", header=None, names=["quote"])
    
    random_quote = df["quote"].sample(n=1).iloc[0]
    print(random_quote)
    #with open("day32\Birthday Wisher (Day 32) start\quotes.txt") as fl:
        
    my_email = "lajosteszt5@gmail.com"
    password = "neeagooemttjyrvw"
    
    with smtplib.SMTP("smtp.gamil.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        
        subject = "Quote of  the week"
        body = random_quote
        msg = f"Subject: {subject}\n\n{body}"
        
        connection.sendmail(from_addr=my_email, 
                            to_addrs="bozo.balint.vid@gmail.com", 
                            msg=msg)
        
motivational_email_sender()
    