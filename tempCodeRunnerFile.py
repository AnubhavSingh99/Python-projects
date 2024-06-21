import tkinter as tk
from tkinter import Tk, Label, Entry, Radiobutton, Checkbutton

win = Tk()
win.geometry('600x400')
win.resizable(0, 0)
win.title('My project')

lbl1 = Label(win, text="roll no", font=("Arial", 20))
lbl1.config(fg='blue', bg="yellow")
lbl1.grid(row=0, column=0, padx=10, pady=10)
lbl2 = Label(win, text="Name", font=("Arial", 20))
lbl2.config(fg='blue', bg="yellow")
lbl2.grid(row=2, column=0, padx=10, pady=10)

ent1 = Entry(win, font=("Arial", 20))
ent1.grid(row=0, column=1, padx=10, pady=10)
ent2 = Entry(win, font=("Arial", 20))
ent2.grid(row=2, column=1, padx=10, pady=10)

# Radio buttons
radio_var = tk.StringVar()
radio_var.set("Male")
radio_btn1 = Radiobutton(win, text="Male", variable=radio_var, value="Male", font=("Arial", 16))
radio_btn1.grid(row=4, column=0, padx=10, pady=10)
radio_btn2 = Radiobutton(win, text="Female", variable=radio_var, value="Female", font=("Arial", 16))
radio_btn2.grid(row=4, column=1, padx=10, pady=10)
radio_btn2 = Radiobutton(win, text="Helicopter", variable=radio_var, value="Female", font=("Arial", 16))
radio_btn2.grid(row=4, column=2, padx=10, pady=10)

# Checkboxes
checkbox_var1 = tk.IntVar()
checkbox_var2 = tk.IntVar()
checkbox1 = Checkbutton(win, text="Python", variable=checkbox_var1, font=("Arial", 16))
checkbox1.grid(row=6, column=0, padx=10, pady=10)
checkbox2 = Checkbutton(win, text="Java", variable=checkbox_var2, font=("Arial", 16))
checkbox2.grid(row=6, column=1, padx=10, pady=10)

# Checkbutton
checkbutton_var = tk.IntVar()
checkbutton = Checkbutton(win, text="Agree to terms", variable=checkbutton_var, font=("Arial", 16))
checkbutton.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

win.mainloop()