import smtplib

my_email = "lajosteszt5@gmail.com"
password = "neeagooemttjyrvw"

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
    subject = "Teszt uzenet"
    body = "Ez egy teszt uzenet"
    msg = f"Subject: {subject}\n\n{body}"

    # E-mail küldése
    connection.sendmail(from_addr=my_email, to_addrs="bozo.balint.vid@gmail.com", msg=msg)
    print("E-mail sikeresen elküldve")
except Exception as e:
    print(f"Hiba történt: {e}")
finally:
    connection.quit()  # Kapcsolat bezárása