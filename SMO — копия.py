import math
import tkinter as tk
from tkinter.ttk import Notebook


# Одноканальная СМО с отказом
def odnokanal_SMO_otkaz():
    potokZav = float(input('Введите интенсивность - '))  # lambda
    tAverage = float(input('Введите время обслуживания - '))  # Среднее время обслуживания в МИНУТАХ
    potokObs = (1 / tAverage) * 60  # Интенсивонсть потока обслуживания U в ЧАСАХ

    print('===================================')
    p0 = (potokObs / (potokZav + potokObs))  # канал свободен
    p1 = (potokZav / (potokZav + potokObs))  # канал занят
    Q = (potokObs / (potokZav + potokObs))  # относительная пропускная способность
    A = (potokZav * potokObs / (potokZav + potokObs))  # абсолютная пропускная способность

    # print('P0 = ', p0)
    # print('P1 или P отказа = ' + str(p1) + ' = ' + str(p1 * 100) + '%')
    # print('Q = ', Q)
    # print('A = ', str(A) + 'заявок в час')
    otvet = ('P0 = ' + str(p0) + ' \n'
                                 'P1 или P отказа = ' + str(p1) + ' = ' + str(p1 * 100) + '%\n'
                                                                                          'Q = ' + str(Q) + '\n'
                                                                                                            'A = ' + str(
        A) + ' заявок в час')
    return otvet


# Одноканальная СМО с ограничением на длину очереди
def ondokanal_SMO_dlina_ocheredi():
    potokZav = float(input('Введите интенсивность - '))  # lambda
    tAverage = float(input('Введите время обслуживания - '))  # Среднее время обслуживания в МИНУТАХ
    edinica_izmerenija = input('Введите какая у вас единица измерения, введите часы или минуты - ')
    if edinica_izmerenija == 'минуты':
        potokObs = (1 / tAverage) * 60  # Интенсивонсть потока обслуживания U переведена в ЧАСЫ
        print('+Время обслуживания переведено в ЧАСЫ')
    else:
        potokObs = (1 / tAverage) / 60  # Интенсивонсть потока обслуживания U переведена в МИНУТЫ
        print('+Время обслуживания переведено в МИНУТЫ')

    nagruzka_m = float(input('Введите нагрузку - '))

    print('===================================')
    p = potokZav / potokObs  # Нагрузка системы
    print('p ==== ', p)
    p = round(p)
    print('Нагрузка системы (p) = ', p)
    if p == 1:
        p0 = 1 / (nagruzka_m + 2)  # Вероятность простоя системы
        L_och = ((nagruzka_m * (nagruzka_m + 1)) / 2) * p0  # Ср. число заявок, стоящий в очереди на обслуживание
        T_och = L_och / potokZav  # Среднее время ожидания обслужвания
        T_smo = (nagruzka_m + 1) / 2 * potokObs  # Среднее время пребывания заявки в системе
        otvet = ('P0 = ' + str(p0) + '\n'
                                     'Lоч = ' + str(L_och) + '\n'
                                                             'Tоч = ' + str(T_och) + '\n'
                                                                                     'Tсмо = ' + str(T_smo) + '\n')
        return otvet
    else:
        p0 = ((1 - p) / (1 - p ** (nagruzka_m + 2)))
        L_och = p ** 2 * ((1 - p ** (nagruzka_m) * (nagruzka_m - nagruzka_m * p + 1)) / (
                1 - p) ** 2) * p0  # Ср. число заявок, стоящий в очереди на обслуживание
        T_och = L_och / potokZav  # Среднее время ожидания обслужвания
        L_ob = ((nagruzka_m + 1) / (nagruzka_m + 2))  # Ср. число заявок, находящихся на обслуживании
        L_smo = L_ob + L_och  # Ср. число завяок, находящихся в системе
        T_smo = (L_smo / potokZav)  # Среднее время пребывания заявки в системе
        otvet = ('======================\n'
                 'Ваш ответ: \n'
                 'P0 = ' + str(p0) + '\n'
                                     'L_och = ' + str(L_och) + '\n'
                                                               'L_ob = ' + str(L_ob) + '\n'
                                                                                       'L_smo = ' + str(L_smo) + '\n'
                                                                                                                 'T_och = ' + str(
            T_och) + '\n'
                     'T_smo = ' + str(T_smo) + '\n'
                                               '======================')
        return otvet


# print(ondokanal_SMO_dlina_ocheredi())
print(odnokanal_SMO_otkaz())

########################## GUI ##############################

HEIGHT = 700
WIDTH = 1200
MYFONT = ('arial', 14, 'bold')

root = tk.Tk()
root.title('Системы Массового Обслуживания')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame_odnokanal = tk.Frame(root, bg='red')
# frame_odnokanal.place(relx=0, rely=0, relwidth=1, relheight=0.03)

tablayout = Notebook(root)
# Tab 1
#####    ПЕРЕМЕННЫЕ    #####
potokZav = tk.StringVar()
Result = tk.StringVar()
tAverage = tk.StringVar()

tab_odnokanal_otkaz = tk.Frame(tablayout)
tab_odnokanal_otkaz.pack(fill='both')
tablayout.add(tab_odnokanal_otkaz, text='Одноканальная с отказом')

left_frame = tk.Frame(tab_odnokanal_otkaz, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Одноканальная СМО с отказом', font=100, width=42)
smo_label.place(relx=0.1, rely=0.05)
# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность -')
potokZav_label.place(relx=0.1, rely=0.2)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZav)
potokZav_entry.place(relx=0.45, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания -')
tAverage_label.place(relx=0.1, rely=0.3)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverage)
tAverage_entry.place(relx=0.55, rely=0.3)

Result_label = tk.Label(left_frame_inside, text='result -')
Result_label.place(relx=0.1, rely=0.4)
Result_entry = tk.Entry(left_frame_inside, textvariable=Result)
Result_entry.place(relx=0.55, rely=0.4)


def add():
    p = float(potokZav.get())
    t = float(tAverage.get())
    r = p + t
    Result.set(r)


def reset():
    potokZav.set('')
    tAverage.set('')
    Result.set('')


button_odnokanal_otkaz = tk.Button(left_frame_inside, text='Посчитать', command=add, bg='#E50914', fg='white',
                                   font=MYFONT)
button_odnokanal_otkaz.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)

right_frame = tk.Frame(tab_odnokanal_otkaz, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

# Tab 2
tab_odnokonal_ochered = tk.Frame(tablayout)
tab_odnokonal_ochered.pack(fill='both')
label1 = tk.Label(tab_odnokonal_ochered, text='Suka blyat')
label1.pack()
tablayout.add(tab_odnokonal_ochered, text='Одноканальная с ограничением на очередь')

tablayout.place(relx=0, rely=0, relwidth=1, relheight=1)

# button1 = tk.Button(frame_odnokanal, text='Одноканальная с отказом')
# button1.place(relheight=1, relwidth=0.33)
# button2 = tk.Button(frame_odnokanal, text='Одноканальная с ограничением на очередь')
# button2.place(relheight=1, relx=0.33, relwidth=0.33)
# button3 = tk.Button(frame_odnokanal, text='Одноканальная без ограничений')
# button3.place(relheight=1, relx=0.66, relwidth=0.34)
#
# frame_mnogokanal = tk.Frame(root, bg='blue')
# frame_mnogokanal.place(relx=0, rely=0.03, relwidth=1, relheight=0.03)
# button4 = tk.Button(frame_mnogokanal, text='Многоканальная с отказом')
# button4.place(relheight=1, relwidth=0.33)
# button5 = tk.Button(frame_mnogokanal, text='Многоканальна с ограничением на очередь')
# button5.place(relheight=1, relx=0.33, relwidth=0.33)
# button6 = tk.Button(frame_mnogokanal, text='Многоканальная без ограничений')
# button6.place(relheight=1, relx=0.66, relwidth=0.34)
#
# left_frame = tk.Frame(root, bg='yellow')
# left_frame.place(relx=0, rely=0.06, relwidth=0.5, relheight=1)
#
#
#
# right_frame = tk.Frame(root, bg='green')
# right_frame.place(relx=0.5, rely=0.06, relwidth=0.5, relheight=1)

# label = tk.Label(frame, text='This is a label', bg='yellow')
# label.pack()

# entry = tk.Entry(frame, bg='green')
# entry.pack()

root.mainloop()
