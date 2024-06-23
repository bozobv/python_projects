import FCView as fcv
import FCModell as fcm 
import FCController as fcc
import tkinter as tk

window = tk.Tk()

view = fcv.FCView(window)
model = fcm.FCModell("day31/data/words_to_learn.csv")
control = fcc.FCController(model=model, view=view)

view.set_controller(control)

window.mainloop()