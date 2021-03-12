import tkinter as tk
import tkinter.messagebox as box
import random, time


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


# сортировка пузырьком вниз
def bubble_sort(mas):
    for i in range(len(mas)):
        for j in range(len(mas) - 2, i - 1, -1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return mas


def intro_process():
    randout_small.delete('0', 'end')
    st = enter_small.get()
    if len(st) == 0:
        box.showerror(title="Ошибка", message="Вы не ввели размер массива!")
    else:
        st = int(st)
        if st > 10:
            box.showerror(title="Ошибка", message="Вы ввели слишком большой размер!")
        else:
            massive = rand_small.get().split(",")
            if len(massive) < st:
                box.showerror(title="Ошибка", message="Вы ввели слишком мало чисел!")
            elif len(massive) > st:
                box.showerror(title="Ошибка", message="Вы ввели слишком много чисел!")
            else:
                flag = 0
                print(massive)
                for i in massive:
                    if not (it_is_a_number(i.strip())):
                        flag = 1
                        break
                if flag:
                    box.showerror(title="Ошибка", message="Вы ввели не только числа!")
                else:
                    mas_s = bubble_sort([int(x) for x in massive])
                    randout_small.insert(0, ', '.join([str(mas_s[i]) for i in range(st)]))


# 1, 5, 7, 10, -2, 1, 1
print(bubble_sort([1, 5, 7, 10, -2, 1, 1]))


def callback(input):
    if input == '':  # пустая строка допустима
        return True
    elif '-' in input:  # наличие двух и более минусов недопустимо
        return False
    elif '.' in input:  # более двух точек недопустимы
        return False
    elif ' ' in input:
        return False
    elif input[0] == '0':
        return False
    elif letter_in_str(input):  # наличие букв недопустимо
        return False
    else:
        return True


def letter_in_str(inp):
    for i in inp:
        if 'a' <= i <= 'z' or 'A' <= inp <= 'Z' or 'а' <= i <= 'я' or 'А' <= inp <= 'Я':
            return True
    else:
        return False


def write_result(t1, t2, t3, i):
    formatting = "{:.3f}"
    if i == 0:
        Nord1_label.config(text=str(formatting.format(t1)))
        Nrand1_label.config(text=str(formatting.format(t2)))
        Nrev1_label.config(text=str(formatting.format(t3)))
    elif i == 1:
        Nord2_label.config(text=str(formatting.format(t1)))
        Nrand2_label.config(text=str(formatting.format(t2)))
        Nrev2_label.config(text=str(formatting.format(t3)))
    elif i == 2:
        Nord3_label.config(text=str(formatting.format(t1)))
        Nrand3_label.config(text=str(formatting.format(t2)))
        Nrev3_label.config(text=str(formatting.format(t3)))

# меню с информацией о разработчике
def dev_menu():
    dev_window = tk.Tk()  # создание окна
    dev_window.title("Информация о программе и авторе")  # заголовок окна
    dev_window.geometry('300x300')  # размер окна
    dev_window.config(bg='ghost white')  # цвет окна

    # заголовок окна
    hdr = tk.Label(dev_window, text='Информация о программе и авторе:', bg='light cyan')
    hdr.grid(rowspan=2)  # размещение заголовка, который занимает 2 столбца

    # Информация о программе
    info_txt = tk.Label(dev_window, text='Программа показывает скорость и правильность\n'
                                         'сортировки пузырьком.')
    info_txt.config(bg='ghost white')
    info_txt.grid()  # размещение информации

    # информация о разработчике
    developed_info = tk.Label(dev_window,
                              text='Выполнил студент группы ИУ7-25Б\nМГТУ им. Н.Э.Баумана для лабораторной\n'
                                   'работы №2 курса "Программирование"\nipa20u488@student.bmstu.ru')
    developed_info.config(bg='ghost white')
    developed_info.grid()  # размещение информации

    # информация о дате создания
    date_info = tk.Label(dev_window, text='Март 2021', bg='ghost white')
    date_info.grid()

    dev_window.mainloop()



def main_process():
    if len(ent_N1.get().strip()) == 0 or len(ent_N2.get().strip()) == 0 or len(ent_N3.get().strip()) == 0:
        box.showerror(title="Ошибка", message="Вы ввели не все размеры!")
    else:
        sizes = [int(ent_N1.get()), int(ent_N2.get()), int(ent_N3.get())]
        for i in range(3):
            ordered_mas = [x for x in range(1, sizes[i] + 1)]
            random_mas = [random.randint(-10000, 10000) for x in range(sizes[i])]
            reversed_mas = [x for x in range(sizes[i] + 1, 1, -1)]

            start_time = time.time() * 1000
            ord_sorted = bubble_sort(ordered_mas)
            ordered_time = time.time() * 1000 - start_time

            start_time = time.time() * 1000
            rand_sorted = bubble_sort(random_mas)
            random_time = time.time() * 1000 - start_time

            start_time = time.time() * 1000
            rev_sorted = bubble_sort(reversed_mas)
            reversed_time = time.time() * 1000 - start_time

            write_result(ordered_time, random_time, reversed_time, i)


window = tk.Tk()
window.geometry("400x400")
window.title("Измерение времени сортировок")

header = tk.Label(text="Измерение времени сортировки пузырьком")
header.grid(columnspan=4)

intro = tk.Label(text="Вы можете попробовать метод на маленьком массиве")
intro.grid(column=0, columnspan=4)

choose_size_small = tk.Label(text="Введите размер массива (до 10):")
choose_size_small.grid(column=0, row=2)

enter_small = tk.Entry(width=30)
enter_small.grid(column=1, row=2, columnspan=4)
enter_small.config(validate='key', validatecommand=(window.register(callback), '%P'))

input_small = tk.Label(text="Введите массив чисел через запятую:")
input_small.grid(columnspan=4)

rand_small = tk.Entry(width=60)
rand_small.grid(columnspan=4)

btn1 = tk.Button(text="Попробовать метод на маленьком массиве", command=lambda: intro_process())
btn1.grid(columnspan=4)
btn1.config(bd=1)

output_small = tk.Label(text="Отсортированный массив:")
output_small.grid(columnspan=4)

randout_small = tk.Entry(width=60)
randout_small.grid(columnspan=4)

blank_label = tk.Label(text="")
blank_label.grid(row=8, column=0)

N1_label = tk.Label(text="N1")
N1_label.grid(row=8, column=1)

N2_label = tk.Label(text="N2")
N2_label.grid(row=8, column=2)

N3_label = tk.Label(text="N3")
N3_label.grid(row=8, column=3)

ordered_label = tk.Label(text="Упорядоченный массив")
ordered_label.grid(row=9, column=0)

Nord1_label = tk.Label(text="")
Nord1_label.grid(row=9, column=1)

Nord2_label = tk.Label(text="")
Nord2_label.grid(row=9, column=2)

Nord3_label = tk.Label(text="")
Nord3_label.grid(row=9, column=3)

random_label = tk.Label(text="Случайный массив")
random_label.grid(row=10, column=0)

Nrand1_label = tk.Label(text="")
Nrand1_label.grid(row=10, column=1)

Nrand2_label = tk.Label(text="")
Nrand2_label.grid(row=10, column=2)

Nrand3_label = tk.Label(text="")
Nrand3_label.grid(row=10, column=3)

reversed_label = tk.Label(text="Обратно упорядоченный массив")
reversed_label.grid(row=11, column=0)

Nrev1_label = tk.Label(text="")
Nrev1_label.grid(row=11, column=1)

Nrev2_label = tk.Label(text="")
Nrev2_label.grid(row=11, column=2)

Nrev3_label = tk.Label(text="")
Nrev3_label.grid(row=11, column=3)

reversed_label = tk.Label(text="Введите размеры массивов:")
reversed_label.grid(row=12, column=0)

ent_N1 = tk.Entry(width=8)
ent_N1.grid(row=12, column=1)
ent_N1.config(validate='key', validatecommand=(window.register(callback), '%P'))

ent_N2 = tk.Entry(width=8)
ent_N2.grid(row=12, column=2)
ent_N2.config(validate='key', validatecommand=(window.register(callback), '%P'))

ent_N3 = tk.Entry(width=8)
ent_N3.grid(row=12, column=3)
ent_N3.config(validate='key', validatecommand=(window.register(callback), '%P'))

start_time = tk.Button(text="Измерить время")
start_time.grid(columnspan=4)
start_time.config(bd=1, command=lambda: main_process())

# Меню
main_menu = tk.Menu(window)  # создание основного меню
# заполнение основного меню
main_menu.add_command(label='Информация о программе и авторе', command=lambda: dev_menu())

window.config(menu=main_menu)  # включение меню в основное окно

window.mainloop()