import tkinter as tk

MILE_TO_KM_FACTOR = 1.60934

def convert():
    miles = int(mile_entry.get())
    km = miles * MILE_TO_KM_FACTOR
    num_km_label.config(text=km)

window = tk.Tk()
window.title("Mérföldből valós hosszúsággá konvertátor")
window.minsize(120,60)

miles_label = tk.Label(text="Mérföld")
equ_label = tk.Label(text="egyenlő")
km_label = tk.Label(text="Km")
num_km_label = tk.Label(text=0)

mile_entry = tk.Entry(width=10, )
mile_entry.insert(0, "0")

calc_bt = tk.Button(text="Kalkulálj", command=convert)


miles_label.grid(column=2, row=0)
equ_label.grid(column=0, row=1)
km_label.grid(column=2, row=1)
num_km_label.grid(column=1, row=1)

mile_entry.grid(column=1, row=0)

calc_bt.grid(column=1, row=2)



window.mainloop()


