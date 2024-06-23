import tkinter

def button_clicked():
    text = input.get()
    my_label.config(text=text)

window = tkinter.Tk()
window.title("kutyamanó")
window.minsize(500,300)


#Label

my_label = tkinter.Label(text="ez egy labélia", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="kutyafarok")

button = tkinter.Button(text="kolbász", command=button_clicked)
button.grid(column=1, row=1)

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

button_2 = tkinter.Button(text="manókalóz")
button_2.grid(column=2, row=0)






window.mainloop()