import tkinter as tk

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    pass
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Jelszókezelő")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200,)
da_logo = tk.PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=da_logo)
canvas.grid(column=1, row=0)

lb_website = tk.Label(window, text="Website:")
lb_website.grid(column=0, row=1)

lb_emailuser = tk.Label(window, text="Email/Username:")
lb_emailuser.grid(column=0, row=2)

lb_password = tk.Label( text="Password:")
lb_password.grid(column=0, row=3)



en_website = tk.Entry( width=35)
en_website.grid(column=1, row=1, columnspan=2)
en_email_pw = tk.Entry( width=35)
en_email_pw.grid(column=1, row=2, columnspan=2,)
en_pw = tk.Entry( width=21)
en_pw.grid(column=1, row=3)



bt_generate_pw = tk.Button( text="Generate Password", command=generate_pw)
bt_generate_pw.grid(column=2, row=3)
bt_add = tk.Button( text="Add", command=generate_pw, width=36)
bt_add.grid(column=1, row=4, columnspan=2)



window.mainloop()
