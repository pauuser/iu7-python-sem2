import tkinter as tk
import tkinter.messagebox as box
import math


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


def add_drawing(event):
    global set_1, set_2
    print(event.x, event.y)
    if rb1_var.get() == 1:
        if not (points_are_in_set(1, (event.x, event.y))) and not (points_are_in_set(2, (event.x, event.y))):
            canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill="SteelBlue1")
            canvas.create_text(event.x, event.y - 15, text=str(event.x) + ", " + str(event.y))
            set_1.append((event.x, event.y))
        else:
            box.showerror(title="Ошибка!", message="Вы ввели новую точку слишком близко к существующей!")
    elif rb2_var.get() == 1:
        if not (points_are_in_set(1, (event.x, event.y))) and not (points_are_in_set(2, (event.x, event.y))):
            canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill="Red")
            canvas.create_text(event.x, event.y - 15, text=str(event.x) + ", " + str(event.y))
            set_2.append((event.x, event.y))
        else:
            box.showerror(title="Ошибка!", message="Вы ввели новую точку слишком близко к существующей!")
    renew_num_widget(len(set_1), len(set_2))


def add_dot(set_num, x, y):
    if set_num == 1:
        canvas.create_oval(x, y, x + 5, y + 5, fill="SteelBlue1")
    elif set_num == 2:
        canvas.create_oval(x, y, x + 5, y + 5, fill="Red")
    canvas.create_text(x, y - 15, text=str(int(x)) + ", " + str(int(y)))


def renew_num_widget(size1, size2):
    entry1_quantity1.config(text=str(size1))
    entry1_quantity2.config(text=str(size2))


def points_are_in_set(set_num, points):
    result = False
    eps = 15
    x, y = map(float, points)
    if set_num == 1:
        for cur in set_1:
            if abs(x - cur[0]) < 15 and abs(y - cur[1]) < eps:
                result = True
    elif set_num == 2:
        for cur in set_2:
            if abs(x - cur[0]) < 15 and abs(y - cur[1]) < eps:
                result = True
    return result


def is_triangle(a, b, c):
    result = False
    a_len = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    b_len = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
    c_len = math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
    if (a_len + b_len > c_len) and (a_len + c_len > b_len) and (b_len + c_len > a_len):
        result = True
    return result


def data_is_correct(data):
    output = False
    if ',' in data:
        points = data.split(',')
        if it_is_a_number(points[0].strip()) and it_is_a_number(points[1].strip()):
            if 0 < float(points[0]) < 600 and 0 < float(points[1]) < 600:
                output = True
    return output


def add_dot_from_keyboard(set_num, set_1, set_2):
    if set_num == 1:
        points = entry_input1.get()
        if data_is_correct(points):
            if not (points_are_in_set(1, points.split(','))) and not (points_are_in_set(2, points.split(','))):
                set_1.append((float(points.split(',')[0]), float(points.split(',')[1])))
                add_dot(1, set_1[-1][0], set_1[-1][1])
            else:
                box.showerror(title="Ошибка!", message="Вы ввели новую точку слишком близко к существующей!")
        else:
            box.showerror(title="Ошибка!", message="Некорректные данные!")
    if set_num == 2:
        points = entry_input2.get()
        if data_is_correct(points):
            if not (points_are_in_set(1, points.split(','))) and not (points_are_in_set(2, points.split(','))):
                set_2.append((float(points.split(',')[0]), float(points.split(',')[1])))
                add_dot(2, set_2[-1][0], set_2[-1][1])
            else:
                box.showerror(title="Ошибка!", message="Вы ввели новую точку слишком близко к существующей!")
        else:
            box.showerror(title="Ошибка!", message="Некорректные данные!")
    renew_num_widget(len(set_1), len(set_2))


def vector_multiplication(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2


def vector_sign(x_dot, y_dot, x1, y1, x2, y2):
    return vector_multiplication(x_dot - x1, y_dot - y1, x2 - x1, y2 - y1)


def dot_is_inside(x1, y1, x2, y2, x3, y3, x_dot, y_dot):
    result = False
    sign_1 = vector_sign(x_dot, y_dot, x1, y1, x2, y2)
    sign_2 = vector_sign(x_dot, y_dot, x2, y2, x3, y3)
    sign_3 = vector_sign(x_dot, y_dot, x3, y3, x1, y1)
    if (sign_1 < 0 and sign_2 < 0 and sign_3 < 0) or \
            (sign_1 > 0 and sign_2 > 0 and sign_3 > 0):
        result = True
    return result


def equal_dots_inside(a, b, c, set_1, set_2):
    result = False
    count_1 = 0
    count_2 = 0
    for i in set_1:
        if i != a and i != b and i != c:
            if dot_is_inside(a[0], a[1], b[0], b[1], c[0], c[1], i[0], i[1]):
                count_1 += 1
    for i in set_2:
        if dot_is_inside(a[0], a[1], b[0], b[1], c[0], c[1], i[0], i[1]):
            count_2 += 1
    print("cnt", count_1, count_2)
    if count_1 == count_2 and count_1 != 0:
        result = True
    return result


def dot_inside_of_mas(a, b, c, mas):
    result = False
    if ((a, b, c) in mas) or ((a, c, b) in mas) or ((b, a, c) in mas) or \
            ((b, c, a) in mas) or ((c, a, b) in mas) or ((c, b, a) in mas):
        result = True
    return result


def triangle_search(set_1, set_2):
    triangles = []
    for i in range(len(set_1)):
        for j in range(i + 1, len(set_1)):
            for k in range(len(set_1)):
                if set_1[k] != set_1[i] and set_1[k] != set_1[j] and is_triangle(set_1[i], set_1[j], set_1[k]):
                    if equal_dots_inside(set_1[i], set_1[j], set_1[k], set_1, set_2) and \
                            not (dot_inside_of_mas(set_1[i], set_1[j], set_1[k], triangles)):
                        triangles.append((set_1[i], set_1[j], set_1[k]))
    return triangles


def draw_triangle(a, b, c, colour):
    canvas.create_line(a[0], a[1], b[0], b[1], fill=colour)
    canvas.create_line(b[0], b[1], c[0], c[1], fill=colour)
    canvas.create_line(c[0], c[1], a[0], a[1], fill=colour)


def process_coords(coord):
    i = coord[0]
    while i != "(":
        coord = coord[1:]
        i = coord[0]
    coords = [0, 0, 0, 0, 0, 0]
    cur = 0
    for i in coord:
        if i not in '1234567890':
            if coords[cur] != 0:
                cur += 1
                if cur > 5:
                    break
        else:
            if coords[cur] == 0:
                coords[cur] = i
            else:
                coords[cur] = coords[cur] + i
    return list(map(int, coords))


def create_ans_window(mas):
    def CurSelect(event):
        for triangle in mas:
            draw_triangle(triangle[0], triangle[1], triangle[2], "aquamarine")
        coord = results.get(results.curselection())
        coordinates = list(map(int, process_coords(coord)))
        draw_triangle(coordinates[0:2], coordinates[2:4], coordinates[4:], "red")


    ans_window = tk.Tk()
    ans_window.title("Результаты")
    ans_window.geometry("200x200")
    tk.Label(ans_window, text="Получены треугольники с вершинами:").grid()
    cnt = 1
    results = tk.Listbox(ans_window, width=40)
    results.grid(row=1, column=0)
    results.bind('<<ListboxSelect>>', CurSelect)
    for i in mas:
        results.insert(cnt, str(cnt) + ".  " + str(i[0]) + str(i[1]) + str(i[2]))
        cnt += 1
    if cnt == 1:
        tk.Label(ans_window, text="Треугольники не найдены!").grid()
    ans_window.mainloop()


def edit_sets(set_1, set_2):
    pass


def main_process(set_1, set_2):
    if len(set_1) < 4 or len(set_2) < 1:
        box.showerror(title="Ошибка!", message="Слишком мало элементов в множествах! В первом множестве должно "
                                               "быть не меньшее 4 элементов, во втором не менее одного!")
    else:
        triangles = triangle_search(set_1, set_2)
        for triangle in triangles:
            draw_triangle(triangle[0], triangle[1], triangle[2], "aquamarine")
        create_ans_window(triangles)


window = tk.Tk()
window.geometry("750x800")
window.title("Треугольники")

set_1 = []
set_2 = []

header_label = tk.Label(text="Программа определяет треугольник с вершинами из первого множества, такой, что внутри него"
                             " \n находится одинаковое число точек и из первого, и из второго множества. "
                             "\nТочки вводятся через запятую в порядке \"x, y\" и 0 < x < 600, 0 < y < 600")
header_label.grid(row=0, column=0, rowspan=2, columnspan=6)

lbl_input1 = tk.Label(text="Введите точку первого множества: ").grid(row=2, column=0)

entry_input1 = tk.Entry(width=15, )
entry_input1.grid(row=2, column=1)

add_button1 = tk.Button(text="Добавить", bd=0.5, command=lambda: add_dot_from_keyboard(1, set_1, set_2))
add_button1.grid(row=2, column=2)

lbl_input2 = tk.Label(text="Введите точку второго множества: ").grid(row=2, column=3)

entry_input2 = tk.Entry(width=15)
entry_input2.grid(row=2, column=4)

add_button2 = tk.Button(text="Добавить", bd=0.5, command=lambda: add_dot_from_keyboard(2, set_1, set_2))
add_button2.grid(row=2, column=5)

lbl_quantity1 = tk.Label(text="Введено элементов: ").grid(row=3, column=0)
entry1_quantity1 = tk.Label(text="0")
entry1_quantity1.grid(row=3, column=1)

lbl_quantity2 = tk.Label(text="Введено элементов: ").grid(row=3, column=3)
entry1_quantity2 = tk.Label(text="0")
entry1_quantity2.grid(row=3, column=4)

invitation_point = tk.Label(
    text="Вы можете ввести точки левой кнопкой мыши. Выберите, какое множество вы отмечаете: ").grid(row=4,
                                                                                                     columnspan=6)

rb1_var = tk.IntVar()
rb1_var.set(0)
rb2_var = tk.IntVar()
rb2_var.set(0)

first_check = tk.Checkbutton(text="Первое множество ", variable=rb1_var, onvalue=1, offvalue=0,
                             command=lambda: second_check.deselect())
first_check.grid(row=5, column=0, columnspan=3)

second_check = tk.Checkbutton(text="Второе множество ", variable=rb2_var, onvalue=1, offvalue=0,
                              command=lambda: first_check.deselect())
second_check.grid(row=5, column=3, columnspan=3)

canvas = tk.Canvas(height=600, width=600, bg="floral white")
canvas.grid(columnspan=6)

canvas.bind("<Button-1>", add_drawing)

start_btn_lbl = tk.Button(text="Начать вычисления!", width=35, bd=1, command=lambda: main_process(set_1, set_2))
start_btn_lbl.grid(column=0, columnspan=3)

show_btn_lbl = tk.Button(text="Показать список точек / редактировать", width=35, bd=1,
                         command=lambda: main_process(set_1, set_2))
show_btn_lbl.grid(column=3, columnspan=3, row=7)

window.mainloop()
