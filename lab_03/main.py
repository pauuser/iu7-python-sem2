import tkinter as tk
import tkinter.messagebox as box
import math
import matplotlib.pyplot as plt
import numpy as np

def it_is_a_number(N):
    saw_e = False  # переменная "встречи" e
    saw_dot = False  # переменная "встречи" точки
    ans = True  # ответ
    if N == '':
        ans = False
    if N == 'e':
        return False
    for i in range(len(N)):
        temp = ord(N[i])  # текущий символ проверяемого элемента
        if (temp < 48 or temp > 57) and (temp != 101 and temp != 46
                                         and temp != 45 and temp != 43):
            # Если не число, не точка, минус, плюс или e
            ans = False
            break
        elif temp == 101:
            if i == 0 or saw_e:
                # Выход, если e стоит первая или уже встречалось е
                ans = False
                break
            saw_e = True
        elif temp == 46:
            if i == 0 or saw_e or saw_dot:
                # Выход, если запятая на первом месте или встречалось e
                ans = False
                break
            saw_dot = True
        elif (temp == 45) or (temp == 43):
            # Минус может быть только в начале или сразу после e
            if i == 0:
                continue
            elif N[i - 1] == 'e':
                continue
            else:
                ans = False
                break
    return ans

def function(x):
    return x + math.sin(x)

def iter_root_1(x0, eps, a, b):
    if (a - function(a)) * (b - function(b)) > 0:
        return None, 0, None
    else:
        x1 = function(x0)
        count = 0
        err = 'OK'
        while abs(x1 - x0) > eps:
            x0 = x1
            x1 = function(x0)
            count += 1
            if count > 10000:
                err = "ITER_ERR"
                break
        if not(a - 1e-5 < x1 < b + 1e-5):
            x1 = '?'
            err = "DIV_ERR"
        return x1, count, err

def iter_root_2(x0, eps, a, b):
    x1 = function(x0)
    count = 0
    while abs(x1 - function(x1)) > eps:
        x0 = x1
        x1 = function(x0)
        count += 1
        if count > 10000:
            break
    if not(a - 1e-5 < x1 < b + 1e-5):
        x1 = None
    return x1, count

def iter_main(x0, eps, a, b, choice):
    if choice == 1:
        return iter_root_1(x0, eps, a, b)
    else:
        return iter_root_2(x0, eps, a, b)


def main_process(check1, check2):
    a = a_entry.get()
    b = b_entry.get()
    h = h_entry.get()
    eps = eps_entry.get()
    data = dict()
    if check1 == check2:
        box.showerror(title='Ошибка', message='Необходимо выбрать только одну опцию вида уточнения!')
        rb_abs_subtract.deselect()
        rb_abs_value.deselect()
    elif (not(it_is_a_number(a)) or  not(it_is_a_number(b)) or not(it_is_a_number(h)) or not(it_is_a_number(eps))):
        box.showerror(title='Ошибка', message='Ошибка ввода! Вводится могут только числа.')
    elif (float(a) > float(b)):
        box.showerror(title='Ошибка', message='Неверно задан интервал!')
    elif (float(h) > abs(float(b) - float(a))):
        box.showerror(title='Ошибка', message='Вы задали слишком большой шаг!')
    elif (float(eps) <= 0):
        box.showerror(title='Ошибка', message='Точность не может быть отрицательной!')
    else:
        record = 1
        a, b, h, eps = float(a), float(b), float(h), float(eps)
        choice = 1 if check1 == 1 else 2
        while a < b:
            middle = (2 * a + h) / 2
            root, iter_count, err = iter_main(middle, eps, a, a + h, choice)
            print(iter_main(middle, eps, a, a+h, choice), 'in', a, a + h)
            if root != None:
                data[record] = dict()
                data[record]["Номер корня"] = record
                data[record]["Отрезок"] = str('[ ' + "{:^.3f}".format(a) + " : " + "{:^.3f}".format(a + h) + ' ]')
                data[record]["x"] = "{:^.6f}".format(root) if root != '?' else 'N/A'
                data[record]["f(x)"] = "{:^1.2e}".format(root - function(root)) if root != '?' else 'N/A'
                data[record]["Количество итераций:"] = iter_count if root != '?' else 'N/A'
                data[record]["Код ошибки"] = err
                record += 1
            a += h
    # Create the header
    for column, header in enumerate(data[1]):
        tk.Label(text=header).grid(row=9, column=0+column)
    # Fill in the values
    for row, element in enumerate(data.values()):
        for column, (header, value) in enumerate(element.items()):
            tk.Label(text=value).grid(row=10+row, column=0+column)

    tk.Label(text='Значения кодов ошибок:').grid(columnspan=8)
    tk.Label(text='OK - успешное выполнение').grid(columnspan=8)
    tk.Label(text='ITER_ERR - превышено число итераций').grid(columnspan=8)
    tk.Label(text='DIV_ERR - метод расходится на участке').grid(columnspan=8)

def extremum_find(x, y):
    before = y[0]
    now = y[1]
    extr_x = []
    extr_y = []
    for i in range(2, len(y)):
        after = y[i]
        if (now > before and now > after) or (now < before and now < after):
            extr_y.append(now)
            extr_x.append(x[i - 1])
        before = now
        now = after
    return extr_x, extr_y

def graph_builder():
    a = float(a_entry.get())
    b = float(b_entry.get())
    eps = 0.01

    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')

    x = np.arange(a, b, eps)
    y = [z - function(z) for z in x]
    plt.plot(x, y)

    x_ex, y_ex = extremum_find(x, y)
    print(x_ex, y_ex)
    plt.plot(x_ex, y_ex, 'o')
    plt.show()


window = tk.Tk()  # создание окна
window.geometry("800x600")
window.title("Уточнение корней")

title_lbl = tk.Label(text="Уточнение корней (Лабораторная работа №3)")
title_lbl.grid(columnspan = 2)

a_lbl = tk.Label(text="Введите a - начало отрезка: ")
a_lbl.grid(row=2, column=0)

a_entry = tk.Entry(width=30)
a_entry.grid(row=2, column=1)

b_lbl = tk.Label(text="Введите b - конец отрезка: ")
b_lbl.grid(row=3, column=0)

b_entry = tk.Entry(width=30)
b_entry.grid(row=3, column=1)

h_lbl = tk.Label(text="Введите h - шаг: ")
h_lbl.grid(row=4, column=0)

h_entry = tk.Entry(width=30)
h_entry.grid(row=4, column=1)

eps_lbl = tk.Label(text="Введите eps - точность: ")
eps_lbl.grid(row=5, column=0)

eps_entry = tk.Entry(width=30)
eps_entry.grid(row=5, column=1)

lbl_choose = tk.Label(text="Выберите способ рассчёта: ")
lbl_choose.grid(columnspan=2)

rb1_var = tk.IntVar()
rb1_var.set(0)
rb2_var = tk.IntVar()
rb2_var.set(0)

rb_abs_subtract = tk.Checkbutton(text="Пока абсолютное значение разности больше eps", variable=rb1_var, onvalue=1, offvalue=0)
rb_abs_subtract.grid(row=7, column=0, columnspan=3)

rb_abs_value = tk.Checkbutton(text="Пока значение в точке корня больше eps", variable = rb2_var, onvalue=1, offvalue=0)
rb_abs_value.grid(row=7, column=3, columnspan=3)

start_button = tk.Button(text="Начать вычисления", command=lambda:main_process(rb1_var.get(), rb2_var.get()))
start_button.grid(row = 8, columnspan=3)

graph_button = tk.Button(text="Построить график", command=lambda:graph_builder())
graph_button.grid(row = 8, column = 4, columnspan = 3)

window.mainloop()
