import tkinter as tk
from tkinter import messagebox
import math
import random
import pyperclip
import json

def save():

    web_name = ent_web.get()
    email = ent_emailname.get()
    pw = ent_pw.get()
    new_data = {
        web_name: {
            "email": email,
            "password": pw
        }
    }
    
    if web_name =="" or email == "" or pw =="":
        messagebox.showwarning(title="ez így nem jó, teshow", message="valamelyiket üresen hagytad, kérlek minden mezőt töltsds ki!")
        return

    #is_ok = messagebox.askokcancel(title=web_name, message=f"ez-e jó lesz?\nemail: {email}\npassword: {pw}")

    #if is_ok:

    try:
        with open("day29/secrets.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
    finally:
        with open("day29/secrets.json", "w") as file:
            json.dump(data, file, indent=4)

            #file.write(f"{web_name} | {email} | {pw}\n")
            ent_web.delete(0, tk.END)
            ent_emailname.delete(0, tk.END)
            ent_pw.delete(0, tk.END)

def find_password():

    web_name = ent_web.get()
    try:
        with open("day29/secrets.json", "r") as file:
            data = json.load(file)
            
            if web_name in data:
                messagebox.showinfo(web_name, message=f"Email/Username: {data[web_name]['email']}, Password: {data[web_name]['password']}")
            else:
                messagebox.showerror(web_name, "Nincs ilyen bejegyzés eddig")
    except FileNotFoundError:
        messagebox.showerror(web_name, "Nincs bejegyzés eddig")

def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]    

    random.shuffle(password_list)

    password = "".join(password_list)
    
    pyperclip.copy(password)

    return password

def generate_pw():
    ent_pw.delete(0, tk.END)
    ent_pw.insert(0, string=pw_generator())
    
def are_you_sure():
    # Create a top-level window
    popup = tk.Toplevel(window)
    popup.title("Biztos?")
    popup.geometry("300x100")  # Width x Height

    # Add a label
    msg = tk.Label(popup, text="Biztos vagyol benne testwérem?")
    msg.grid(pady=10, column=0, row=0, columnspan=3,)  # Add some padding

    close_button = tk.Button(popup, text="Igen", command=popup.destroy)
    close_button.grid(pady=5, column=0, row=1)

    close_button = tk.Button(popup, text="Nem", command=popup.destroy)
    close_button.grid(pady=5, column=1, row=1)

    return True

window = tk.Tk()
window.title("Jelszó generátor")
window.config(padx=20, pady=20)

#Canvas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
lb_web = tk.Label(text="Website:")
lb_web.grid(column=0, row=1)
lb_emailname = tk.Label(text="Email/Username:")
lb_emailname.grid(column=0, row=2)
lb_pw = tk.Label(text="Password")
lb_pw.grid(column=0, row=3)

#Entries
ent_web = tk.Entry(width=35)
ent_web.grid(column=1, row=1, columnspan=1, sticky="ew")
ent_emailname = tk.Entry(width=35)
ent_emailname.insert(0, "kolbasz@asd.com")
ent_emailname.grid(column=1, row=2, columnspan=2, sticky="ew")
ent_pw = tk.Entry(width=25)
ent_pw.grid(column=1, row=3, columnspan=1, sticky="ew")

#Buttons
bt_pw = tk.Button(text="Generate Password", command=generate_pw)
bt_pw.grid(column=2, row=3)
bt_add = tk.Button(text="Add", width=36, command=save)
bt_add.grid(column=1, row=4, columnspan=2, sticky="ew")
bt_search = tk.Button(text="Search", command=find_password)
bt_search.grid(column=2, row=1, sticky="ew")

print(ent_web.cget("text"))

window.mainloop()