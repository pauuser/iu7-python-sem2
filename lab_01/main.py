# Лабораторная работа №1
# Выполнил студент ИУ7-25Б Иванов Павел
# Вариант 6
# Программа переводит вещественные числа из 6-й СС в 10-ю и обратно

import tkinter as tk
import tkinter.messagebox as box
from math import modf, copysign


# функция, которая убирает флажки
def flags_deselect():
    btn1.deselect()
    btn2.deselect()


# функция, которая очищает все поля
def clear_all():
    flags_deselect()  # убираем флажки
    in_text.delete(0, 'end')  # очищение поля ввода
    output_txt.delete('0.0', 'end')  # очищение поля вывода


# функция, которая проверяет, не выбрал ли пользователь сразу два флажка
def task_processor():
    if (btn1_var.get() == btn2_var.get() == 1):
        box.showerror(title='Ошибка', message='Необходимо выбрать только одну опцию!')
        flags_deselect()


# функция проверки наличия букв в строке
def letter_in_str(inp):
    for i in inp:
        if 'a' <= i <= 'z' or 'A' <= inp <= 'Z' or 'а' <= i <= 'я' or 'А' <= inp <= 'Я':
            return True
    else:
        return False


# функция проверки очередного ввода на допустимость
def callback(input):
    if input == '':  # пустая строка допустима
        return True
    elif input.count('-') > 1:  # наличие двух и более минусов недопустимо
        return False
    elif '-' in input and input[0] != '-':  # наличие минуса не в начале недопустимо
        return False
    elif input.count('.') > 1:  # более двух точек недопустимы
        return False
    elif input[0] == '.':  # точка в начале не допустима
        return False
    elif letter_in_str(input):  # наличие букв недопустимо
        print('here')
        return False
    else:
        return True


# функция вставки заданного символа с клавиатуры
def text_insert(n):
    # если это точка, надо проверить, не будет ли она на первом месте или не единственной
    if n == '.' and (len(in_text.get()) == 0 or '.' in in_text.get()):
        return
    else:
        # остальные можно вставлять
        in_text.insert(len(in_text.get()), n)


# функция удаления последнего числа
def delete():
    # если длина 1, то для строки особые индексы
    if len(in_text.get()) == 1:
        in_text.delete(0, 1)
    else:
        in_text.delete(len(in_text.get()) - 1, len(in_text.get()))


# основной алгоритм перевода
def main_process():
    # проверяем, выбран ли флажок
    if tick_choice() == 0:
        pass
    # если перевод из 6 в 10 СС
    elif tick_choice() == 610:
        # проверяем, корректно ли число
        if not (num_is_correct(6)):
            # если нет, то выдаем ошибку
            box.showerror(title='Ошибка', message='Некорректный ввод числа в заданной СС - перевод невозможен!')
            in_text.delete(0, 'end')
        else:
            # если корректно, переводим и выводим в окне для вывода
            output_txt.delete('0.0', 'end')
            output_txt.insert('0.0', '{:f}'.format(trans_610(float(in_text.get()))))
    # если перевод из 10 в 6 СС
    else:
        # проверяем, корректно ли число
        if not (num_is_correct(10)):
            # если нет, то выдаем ошибку
            box.showerror(title='Ошибка', message='Некорректный ввод числа в заданной СС - перевод невозможен!')
            in_text.delete(0, 'end')
        else:
            # переводим
            output_txt.delete('0.0', 'end')
            output_txt.insert('0.0', '{:f}'.format(trans_106(float(in_text.get()))))


# функция, определяющая, какой флажок поднят
def tick_choice():
    # если ни один не поднят, то поднимаем ошибку
    if (btn1_var.get() == btn2_var.get() == 0):
        box.showerror(title='Ошибка', message='Необходимо выбрать системы счисления перевода!')
        return 0
    elif btn1_var.get() == 1:
        # если выбран перевод из 10-й СС в 6-ю, передаём код 106
        return 106
    else:
        # если выбран перевод из 6-й СС в 10-ю, передаём код 610
        return 610


# функция проверки существования введённого числа в данной СС
def num_is_correct(system):
    if system == 6:
        # в шестеричной не сущетвуют пустые числа, просто минус или числа с цифрами больше 5
        if in_text.get().strip() in ('', '-'):
            return False
        for i in in_text.get():
            # при проверке первый минус пропускаем
            if i == '-':
                continue
            if i not in '012345.':
                return False
        return True
    else:
        # в десятичной не сущетвуют пустые числа или просто минус
        if in_text.get().strip() in ('', '-'):
            return False
        else:
            return True


# функция очистки поля вывода
def clear_output():
    output_txt.delete('0.0', 'end')


# алгоритм перевода из 6СС в 10СС
def trans_610(num):
    frac = modf(abs(num))[0]  # сохраняем дробную часть
    integ = int(modf(abs(num))[1])  # сохраняем целую часть числа
    ans = 0  # переведённое число
    integ = str(integ)[::-1]  # инверсируем порядок цифр числа, чтобы было удобнее переводить
    k = 0  # счётчик текущей степени шестёрки
    for i in integ:
        ans += int(i) * 6 ** k  # прибавляем степени шестерки, умноженные на цифры числа
        k += 1
    k = -1  # теперь будем идти по отрицательным степеням
    for i in str(frac)[2:]:
        ans += int(i) * 6 ** k  # прибавляем степени помноженные на цифры
        k -= 1
    return copysign(ans, num)  # возвращаем переведённое число со знаком исходного


# алгоритм перевода из 10СС в 6СС
def trans_106(num):
    ans = ''  # результат перевода
    frac = modf(abs(num))[0]  # дробная часть числа
    integ = int(modf(abs(num))[1])  # целая часть числа
    # будем делаить на 6 и собирать остатки
    while integ // 6 != 0:
        ans += str(integ % 6)
        integ //= 6
    ans += str(integ)
    ans = ans[::-1]  # инвертированные остатки и будут целой частью в 6СС
    ans = float(ans)
    k = 0  # номер текущего порядка после запятой
    ans_frac = ''  # искомая дробная часть
    if frac != 0:
        while k < 10:  # будем вычислять с точностью до 10 знаков после запятой
            frac = frac * 6  # умножаем на 6
            ans_frac += str(int(modf(frac)[1]))  # забираем целую часть в ответ
            frac -= modf(frac)[1]  # вычитаем целую часть
            k += 1
        k = -1
        # теперь будем приписывать к числу получившийся ответ
        for i in ans_frac:
            ans += int(i)*10**k
            k -= 1
    return copysign(ans, num)  # возвращаем переведённое число со знаком исходного


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
    info_txt = tk.Label(dev_window, text='Калькулятор осуществляет перевод заданного\n'
                                         'вещественного числа из 10-й системы счисления\nв 6-ю и обратно.')
    info_txt.config(bg='ghost white')
    info_txt.grid()  # размещение информации

    # информация о разработчике
    developed_info = tk.Label(dev_window,
                              text='Выполнил студент группы ИУ7-25Б\nМГТУ им. Н.Э.Баумана для лабораторной\n'
                                   'работы №1 курса "Программирование"\nipa20u488@student.bmstu.ru')
    developed_info.config(bg='ghost white')
    developed_info.grid()  # размещение информации

    # информация о дате создания
    date_info = tk.Label(dev_window, text='Февраль 2021', bg='ghost white')
    date_info.grid()

    dev_window.mainloop()


# создание основного окна
window = tk.Tk()
window.title("Калькулятор")  # имя окна
window.geometry('675x600')  # размеры окна
window.config(bg='ghost white')

# надпись заголовка
header = tk.Label(window, text='Калькулятор перевода вещественного числа из 10-й СС в 6-ю СС и обратно.',
                  bg='ghost white')
header.grid(columnspan=2)

# надпись "выберите СС"
choice_label = tk.Label(window, text='Выберите систему счисления:', bg='ghost white')
choice_label.grid(column=0)

# кнопка перевода 10 СС --> 6 СС
btn1_var = tk.IntVar()
btn1 = tk.Checkbutton(window, text='Из десятичной в шестеричную', variable=btn1_var,
                      onvalue=1, offvalue=0, command=task_processor, bg='ghost white')
btn1.grid(column=1, row=1)

# кнопка перевода 6 СС --> 10 СС
btn2_var = tk.IntVar()
btn2 = tk.Checkbutton(window, text='Из шестеричной в десятичную', variable=btn2_var,
                      onvalue=1, offvalue=0, command=task_processor, bg='ghost white')
btn2.grid(column=2, row=1)

# надпись "введите число"
input_label = tk.Label(window, text='Введите число:', bg='ghost white')
input_label.grid(column=0, row=2)

# строка ввода чисел
in_text = tk.Entry(bd=0, width=70)
in_text.grid(column=1, row=2, columnspan=4)
in_text.config(validate='key', validatecommand=(window.register(callback), '%P'))

# создание кнопок калькулятора: ввод в in_text производится с помощью text_insert()
# кнопка, которая вводит 1
b1 = tk.Button(text='1', bd=1, command=lambda: text_insert('1'))
b1.grid(column=0, row=3)
b1.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 2
b2 = tk.Button(text='2', bd=1, command=lambda: text_insert('2'))
b2.grid(column=1, row=3)
b2.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 3
b3 = tk.Button(text='3', bd=1, command=lambda: text_insert('3'))
b3.grid(column=2, row=3)
b3.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 4
b4 = tk.Button(text='4', bd=1, command=lambda: text_insert('4'))
b4.grid(column=0, row=4)
b4.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 5
b5 = tk.Button(text='5', bd=1, command=lambda: text_insert('5'))
b5.grid(column=1, row=4)
b5.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 6
b6 = tk.Button(text='6', bd=1, command=lambda: text_insert('6'))
b6.grid(column=2, row=4)
b6.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 7
b7 = tk.Button(text='7', bd=1, command=lambda: text_insert('7'))
b7.grid(column=0, row=5)
b7.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 8
b8 = tk.Button(text='8', bd=1, command=lambda: text_insert('8'))
b8.grid(column=1, row=5)
b8.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 9
b9 = tk.Button(text='9', bd=1, command=lambda: text_insert('9'))
b9.grid(column=2, row=5)
b9.config(width=30, height=3, bg='alice blue')

# кнопка, которая вводит 0
b0 = tk.Button(text='0', bd=1, command=lambda: text_insert('0'))
b0.grid(column=1, row=6)
b0.config(width=30, height=3, bg='alice blue')

# кнопка для запятой (будет вводится точка)
b_comma = tk.Button(text=',', bd=1, command=lambda: text_insert('.'))
b_comma.grid(column=0, row=6)
b_comma.config(width=30, height=3, bg='alice blue')

# кнопка для минуса
b_minus = tk.Button(text='-', bd=1, command=lambda: text_insert('-'))
b_minus.grid(column=2, row=6)
b_minus.config(width=30, height=3, bg='alice blue')

# кнопка для стриания последнего элемента
b_del = tk.Button(text='Backspace', bd=1, command=lambda: delete())
b_del.grid(column=2, row=7)
b_del.config(width=30, height=3, bg='misty rose')

# кнопка для очистки поля
b_clear = tk.Button(text='Очистить поле', bd=1, command=lambda: in_text.delete(0, 'end'))
b_clear.grid(column=0, row=7)
b_clear.config(width=30, height=3, bg='misty rose')

# Кнопка начала перевода
b_start = tk.Button(text='Перевод', bd=1, command=lambda: main_process())
b_start.grid(column=1, columnspan=1, row=7)
b_start.config(width=30, height=3, bg='light cyan')

# Подпись "результат"
result_label = tk.Label(window, text='Результат:', bg='ghost white')
result_label.grid(column=1)

# Окно, в котором будет появляться ответ
output_txt = tk.Text(window, bg='white', width=70, height=10, bd=0)
output_txt.grid(columnspan=3)

# Кнопка очистки поля вывода
b_clear_out = tk.Button(text='Очистить поле вывода', bd=1, command=lambda: clear_output())
b_clear_out.grid(column=1)
b_clear_out.config(width=30, height=3, bg='misty rose')

# Меню
main_menu = tk.Menu(window)  # создание основного меню

clear_menu = tk.Menu(main_menu)  # создание меню очистки
# Добавление кнопок в меню очистки:
# Все пункты привязаны к соответствующим функциям
clear_menu.add_command(label='Очистить поле ввода', command=lambda: in_text.delete(0, 'end'))
clear_menu.add_command(label='Очистить поле вывода', command=lambda: output_txt.delete('0.0', 'end'))
clear_menu.add_command(label='Убрать флажок', command=lambda: flags_deselect())
clear_menu.add_command(label='Очистить всё', command=lambda: clear_all())

# заполнение основного меню
main_menu.add_cascade(label='Очистка', menu=clear_menu)
main_menu.add_command(label='Перевод', command=lambda: main_process())
main_menu.add_command(label='Информация о программе и авторе', command=lambda: dev_menu())

window.config(menu=main_menu)  # включение меню в основное окно
window.mainloop()
