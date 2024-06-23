##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = "lajosteszt5@gmail.com"
password = "neeagooemttjyrvw"


def write_letter(name, email):
    letter_number = random.randint(1, 3)
    #path = f"day32/Birthday Wisher (Day 32) start/letter_templates/letter_{letter_number}.txt"
    path = f"letter_templates/letter_{letter_number}.txt"
    
    with open(path, "r") as file:
        content = file.read()
        
    named_content = content.replace("[NAME]", name)
    print(named_content)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # TLS titkosítás indítása
        connection.login(user=my_email, password=password)  # Bejelentkezés

        # Az üzenet formátuma
        subject = "Boldog születésnapot, spanifer"
        #msg = f"Subject: {subject}\n\n{named_content}"

        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(named_content, 'plain', 'utf-8'))


        # E-mail küldése
        connection.sendmail(from_addr=my_email, 
                            to_addrs=email, 
                            msg=msg.as_string())
        print("E-mail sikeresen elkuldve")
    
#column_names = ["name","email","year","month","day"]
#df = pd.read_csv("day32/Birthday Wisher (Day 32) start/birthdays.csv")
df = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
print(f"a mai nap: {now.month} : {now.day}")

for i, row in df.iterrows():
    if row["month"] == now.month and row["day"] == now.day:
        #print(row)
        print(row["name"])
        write_letter(row["name"], row["email"])
         
