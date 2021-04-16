import tkinter as tk

def mmove(event):
    print(event.x, event.y)
    if rb1_var.get() == 1 and rb2_var.get() == 1:
        pass
    elif rb1_var.get() == 1:
        canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill="SteelBlue1")
    elif rb2_var.get() == 1:
        canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill="Red")
    else:
        pass

window = tk.Tk()
window.geometry("750x700")

mas = []

header_label = tk.Label(text="Программа определяет треугольник с вершинами из первого множества, такой, что внутри него \n находится одинаковое число точек и из первого, и из второго множества. Точки вводятся через запятую в порядке \"x, y\"")
header_label.grid(row=0, column=0, rowspan=2, columnspan=6)

lbl_input1 = tk.Label(text="Введите точку первого множества: ").grid(row=2, column=0)

entry_input1 = tk.Entry(width=15)
entry_input1.grid(row=2, column=1)

add_button1 = tk.Button(text="Добавить", bd=0.5)
add_button1.grid(row=2, column=2)

lbl_input2 = tk.Label(text="Введите точку второго множества: ").grid(row=2, column=3)

entry_input2 = tk.Entry(width=15)
entry_input2.grid(row=2, column=4)

add_button2 = tk.Button(text="Добавить", bd=0.5)
add_button2.grid(row=2, column=5)

lbl_quantity1 = tk.Label(text="Введено элементов: ").grid(row=3, column=0)
entry1_quantity1 = tk.Label(text="0")
entry1_quantity1.grid(row=3, column=1)

lbl_quantity2 = tk.Label(text="Введено элементов: ").grid(row=3, column=3)
entry1_quantity2 = tk.Label(text="0")
entry1_quantity2.grid(row=3, column=4)

invitation_point = tk.Label(text="Вы можете ввести точки левой кнопкой мыши. Выберите, какое множество вы отмечаете: ").grid(row=4, columnspan=6)

rb1_var = tk.IntVar()
rb1_var.set(0)
rb2_var = tk.IntVar()
rb2_var.set(0)

first_check = tk.Checkbutton(text="Первое множество ", variable=rb1_var, onvalue=1, offvalue=0)
first_check.grid(row=5, column=0, columnspan=3)

second_check = tk.Checkbutton(text="Второе множество ", variable=rb2_var, onvalue=1, offvalue=0)
second_check.grid(row=5, column=3, columnspan=3)

canvas = tk.Canvas(height=600, width=600, bg="floral white")
canvas.grid(columnspan=6)


canvas.bind("<Button-1>", mmove)

window.mainloop()

