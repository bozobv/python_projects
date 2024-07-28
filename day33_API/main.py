import datetime
import requests
import smtplib

MY_LAT = 47.503850
MY_LNG = 19.072120

def iss_position_near():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    
    print(longitude)
    print(latitude)

    if (abs(longitude - MY_LNG) < 12 and abs(latitude - MY_LAT) < 12):
        return True
    return False

def my_sunset_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0 
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = datetime.datetime.now().hour

    if time_now < sunrise or time_now > sunset:
        return True
    return False

def send_mail():

    my_email = "lajosteszt5@gmail.com"
    password = ""

    try:
        print("kezdődik")
        # Csatlakozás az SMTP szerverhez a 587-es porton
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        print("connection")
        connection.starttls()  # TLS titkosítás indítása
        print("tls")

        connection.login(user=my_email, password=password)  # Bejelentkezés
        print("login")
        # Az üzenet formátuma
        subject = "Urallomas"
        body = "Jelenleg lathato az egen a nemzetkozi urallomas :)"
        msg = f"Subject: {subject}\n\n{body}"

        # E-mail küldése
        connection.sendmail(from_addr=my_email, to_addrs="bozo.balint.vid@gmail.com", msg=msg)
        print("E-mail sikeresen elküldve")
    except Exception as e:
        print(f"Hiba történt: {e}")
    finally:
        connection.quit()  # Kapcsolat bezárása


if iss_position_near():
    if my_sunset_time():
        send_mail()
        print("yes")
    print("halfyes")
print("no")
