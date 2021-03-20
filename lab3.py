import tkinter as tk

window = tk.Tk() # создание окна
window.geometry("600x600")
window.title("Уточнение корней")

title_lbl = tk.Label(text="Уточнение корней (лабораторная работа №3)")
title_lbl.grid(columnspan = 2)

a_lbl = tk.Label(text="Введите a - начало отрезка: ")
a_lbl.grid(row=2, column=0)

a_entry = tk.Entry(width=30)
a_entry.grid(row=2, column=1)

b_lbl = tk.Label(text="Введите b - конец отрезка: ")
b_lbl.grid(row=3, column=0)

a_entry = tk.Entry(width=30)
a_entry.grid(row=3, column=1)

h_lbl = tk.Label(text="Введите b - конец отрезка: ")
h_lbl.grid(row=3, column=0)

h_entry = tk.Entry(width=30)
h_entry.grid(row=3, column=1)

window.mainloop()
