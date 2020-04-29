from math import factorial as fc
from math import fsum
import tkinter as tk
from tkinter.ttk import Notebook

HEIGHT = 700
WIDTH = 1200
MYFONT = ('arial', 14, 'bold')
MYHEADER = ('arial', 10, 'bold')


# Одноканальная СМО с отказом
def odnokanal_SMO_otkaz():
    potokZav = float(potokZavE.get())  # lambda
    tAverage = float(tAverageE.get())  # Среднее время обслуживания в МИНУТАХ
    potokObs = (1 / tAverage)  # Интенсивонсть потока обслуживания U в ЧАСАХ

    p0 = round((potokObs / (potokZav + potokObs)), 3)  # канал свободен
    p1 = round((potokZav / (potokZav + potokObs)), 3)  # канал занят
    Q = round((potokObs / (potokZav + potokObs)), 3)  # относительная пропускная способность
    A = round((potokZav * potokObs / (potokZav + potokObs)), 3)  # абсолютная пропускная способность

    return (
        P0E.set(p0),
        P1E.set(p1),
        QE.set(Q),
        AE.set(A),
        potokObsE.set(potokObs)
    )


# Одноканальная СМО с ограничением на длину очереди
def ondokanal_SMO_dlina_ocheredi():
    potokZav = float(potokZavE.get())  # lambda
    tAverage = float(tAverageE.get())  # Среднее время обслуживания в МИНУТАХ
    potokObs = round((1 / tAverage), 5)  # Интенсивонсть потока обслуживания U переведена в ЧАСЫ
    nagruzka_m = int(nagruzka_mE.get())

    p = potokZav / potokObs  # Нагрузка системы
    print('ETO p', p)
    p_round = round(p)
    p_rotv = round(p, 5)
    print('ETO p posle', p_round)

    if p == 1:
        p0 = round(1 / (nagruzka_m + 2), 5)  # Вероятность простоя системы
        L_och = round((((nagruzka_m * (nagruzka_m + 1)) / 2) * p0),
                      5)  # Ср. число заявок, стоящий в очереди на обслуживание
        T_och = round((L_och / potokZav), 5)  # Среднее время ожидания обслужвания
        T_smo = round(((nagruzka_m + 1) / 2 * potokObs), 5)  # Среднее время пребывания заявки в системе
        p1 = round(((p ** (nagruzka_m + 1)) * p0), 5)  # Вероятность отказа
        Q = round((1 - p1), 5)  # относительная пропускная способность
        A = round((Q * potokZav), 5)  # абсолютная пропускная способность
        return (
            pE.set(p_rotv),
            P0E.set(p0),
            P1E.set(p1),
            QE.set(Q),
            AE.set(A),
            L_ochE.set(L_och),
            T_ochE.set(T_och),
            T_smoE.set(T_smo),
            potokObsE.set(potokObs))
    else:
        p0 = round(((1 - p) / (1 - p ** (nagruzka_m + 2))), 5)
        L_och = round((p ** 2 * ((1 - p ** (nagruzka_m) * (nagruzka_m - nagruzka_m * p + 1)) / (
                1 - p) ** 2) * p0), 5)  # Ср. число заявок, стоящий в очереди на обслуживание
        T_och = round((L_och / potokZav), 5)  # Среднее время ожидания обслужвания
        L_ob = round(((nagruzka_m + 1) / (nagruzka_m + 2)), 5)  # Ср. число заявок, находящихся на обслуживании
        L_smo = round((L_ob + L_och), 5)  # Ср. число завяок, находящихся в системе
        T_smo = round((L_smo / potokZav), 5)  # Среднее время пребывания заявки в системе
        p1 = round(((p ** (nagruzka_m + 1)) * p0), 5)  # Вероятность отказа
        Q = round((1 - p1), 5)  # относительная пропускная способность
        A = round((Q * potokZav), 5)  # абсолютная пропускная способность
        return (
            pE.set(p_rotv),
            P0E.set(p0),
            P1E.set(p1),
            QE.set(Q),
            AE.set(A),
            L_ochE.set(L_och),
            T_ochE.set(T_och),
            T_smoE.set(T_smo),
            L_obE.set(L_ob),
            L_smoE.set(L_smo),
            potokObsE.set(potokObs))


# Одноканальная СМО без ограничений
def odnokanal_SMO_bez():
    potokZav = float(potokZavE.get())  # lambda
    tAverage = float(tAverageE.get())  # Среднее время обслуживания в Часах
    potokObs = (1 / tAverage)  # Интенсивонсть потока обслуживания U

    p = potokZav / potokObs  # Нагрузка системы
    p_rotv = round(p, 3)
    Q = 1  # относительная пропускная способность
    A = round((Q * potokZav), 3)  # абсолютная пропускная способность
    p0 = round((1 - p), 3)  # Вероятность простоя системы
    # p0 = str(p0*100) + ' %'
    p1 = '0 %'  # Вероятность отказа
    L_och = round(((p ** 2) / (1 - p)), 3)  # Ср. число заявок, стоящий в очереди
    L_smo = round((L_och + p), 3)  # Ср. число завяок, находящихся в системе
    T_och = round((L_och / potokZav), 3)  # Среднее время ожидания обслужвания
    T_smo = round((L_smo / potokZav), 3)  # Среднее время пребывания заявки в системе

    return (
        pE.set(p_rotv),
        P0E.set(p0),
        P1E.set(p1),
        QE.set(Q),
        AE.set(A),
        L_ochE.set(L_och),
        T_ochE.set(T_och),
        T_smoE.set(T_smo),
        L_smoE.set(L_smo),
        potokObsE.set(potokObs))


def mnogokanal_SMO_otkaz():
    potokZav = float(potokZavE.get())  # lambda
    tAverage = float(tAverageE.get())  # Среднее время обслуживания в Часах
    n = int(nE.get())  # Количество каналов
    potokObs = (1 / tAverage)  # Интенсивонсть потока обслуживания U

    p = potokZav / potokObs  # Нагрузка системы
    p_rotv = round(p, 3)
    p0 = 0
    for c in range(n + 1):
        p0 += (p ** c / fc(c))
    p0 = round((1 / p0), 3)  # Вероятность простоя системы
    p1 = round(((p ** n / fc(n)) * p0), 3)  # Вероятность отказа
    Q = round((1 - p1), 3)  # относительная пропускная способность
    A = round((potokZav * Q), 3)  # абсолютная пропускная способность
    n_z = round((p * Q), 3)  # Число каналов занятый обслуживанием
    k_z = round((n_z / n), 3)  # Коэффициент занятости каналов
    T_smo = round((n_z / potokZav), 3)  # Среднее время пребывания заявки в системе
    T_ob = round((1 / potokObs), 3)  # Ср. время обслуживанияканалом одной заявки
    potokObs = round(potokObs, 3)
    return (
        pE.set(p_rotv),
        P0E.set(p0),
        P1E.set(p1),
        QE.set(Q),
        AE.set(A),
        n_zE.set(n_z),
        k_zE.set(k_z),
        T_smoE.set(T_smo),
        T_obE.set(T_ob),
        potokObsE.set(potokObs))


def mnogokanal_SMO_dlina_ocheredi():
    potokZav = float(potokZavE.get())  # lambda
    tAverage = float(tAverageE.get())  # Среднее время обслуживания в Часах
    n = int(nE.get())  # Количество каналов
    potokObs = (1 / tAverage)  # Интенсивонсть потока обслуживания U
    nagruzka_m = int(nagruzka_mE.get())  # Длина очереди
    mid = 0
    p = potokZav / potokObs  # Нагрузка системы
    p_rotv = round(p, 3)

    if p / n == 1:
        # ch = 1
        # while n-1 != ch:
        #     mid += (p ** ch / fc(ch))
        #     ch += 1
        ch = 1
        for ii in range(n):
            mid += (p ** ch / fc(ch))
            ch += 1
        last = (nagruzka_m * p ** (n + 1)) / (n * fc(n))
        p0 = round((1 + mid + last) ** -1, 3)  # Вероятность простоя
        pn = round((p ** n / fc(n)) * p0, 3)  # Вероятность того, что в СМО находится какое-либо кол-во заявок
        try:
            p_och = round((p ** n / (fc(n))) * (
                    (1 - ((p / n) ** nagruzka_m)) / (1 - (p / n))) * p0, 3)  # Вероятность образования очереди
            p_ochE.set(p_och)
        except:
            print('Error')
        p1 = round(((p ** (n + nagruzka_m)) / (n ** nagruzka_m * fc(n))) * p0, 3)  # Вероятность отказа
        Q = round((1 - p1), 3)  # Относительная пропускная способность
        A = round((potokZav * Q), 3)  # Абсолютная пропускная способность
        n_z = round((p * Q), 3)  # Ср. Число каналов занятый обслуживанием
        n_pr = round((n - n_z), 3)  # Ср. Число простаивающих каналов
        L_och = round((((p ** (n + 1)) / (n * fc(n))) * (
                    nagruzka_m * (nagruzka_m + 1)) / 2 * p0), 3)  # Ср. число заявок, стоящий в очереди
        T_och = round((L_och / potokZav), 3)  # Среднее время ожидания обслужвания
        T_smo = round((L_och / potokZav) + (Q / potokObs), 3)  # Среднее время пребывания заявки в системе
        k_z = round(n_z / n, 3)  # Коэффициент занятости каналов
        k_pr = round(1 - k_z, 3)  # Коэффициент простоя каналов
        L_ob = round(p * Q, 3)  # Ср.число заявок, находящихся на обслуживании
        L_smo = round(L_och + L_ob, 3)  # Ср. число завяок, находящихся в системе

        pE.set(p_rotv),
        P0E.set(p0),
        PnE.set(pn),
        P1E.set(p1),
        QE.set(Q),
        AE.set(A),
        n_zE.set(n_z),
        n_prE.set(n_pr),
        L_ochE.set(L_och),
        T_ochE.set(T_och),
        T_smoE.set(T_smo),
        k_zE.set(k_z),
        k_prE.set(k_pr),
        L_obE.set(L_ob),
        L_smoE.set(L_smo),
        potokObsE.set(potokObs)
    else:
        start = 0
        for i in range(n + 1):
            start += (p ** i / fc(i))
        p0 = round(1 / (start + ((p ** (n + 1) / (fc(n) * (n - p))) * (1 - ((p / n) ** nagruzka_m)))), 3)
        try:
            p_och = round(((p ** n / (fc(n))) * (
                        (1 - ((p / n) ** nagruzka_m)) / (1 - (p / n))) * p0), 3)  # Вероятность образования очереди
            p_ochE.set(p_och)
        except:
            print('Error')
        L_och = round((((p ** (n + 1)) / (n * fc(n))) * (
                    1 - (p / n) ** nagruzka_m * (nagruzka_m + 1 - nagruzka_m * (p / n))) / (
                        (1 - p / n) ** 2) * p0), 3)
        T_och = round((L_och / potokZav), 3)
        # p1 = (p ** (n + nagruzka_m) / n ** nagruzka_m * fc(n)) * p0
        p1 = round((((p ** (n + nagruzka_m)) / (n ** nagruzka_m * fc(n))) * p0), 3)
        Q = round((1 - p1), 3)
        A = round((potokZav * Q), 3)
        n_z = round((p * Q), 3)  # Число каналов занятый обслуживанием
        n_pr = round((n - n_z), 3)  # Ср. Число простаивающих каналов
        k_z = round((n_z / n), 3)  # Коэффициент занятости каналов обслуживанием
        k_pr = round((1 - k_z), 3)  # Коэффициент простоя каналов
        L_ob = round((p * Q), 3)  # Ср.число заявок, находящихся на обслуживании
        L_smo = round((L_och + L_ob), 3)  # Ср. число завяок, находящихся в системе
        T_smo = round((L_smo / A), 3)
        print(p)
        print(p0)
        print(nagruzka_m)
        print(n)
        return (
            pE.set(p_rotv),
            P0E.set(p0),
            P1E.set(p1),
            QE.set(Q),
            AE.set(A),
            n_zE.set(n_z),
            n_prE.set(n_pr),
            L_ochE.set(L_och),
            T_ochE.set(T_och),
            T_smoE.set(T_smo),
            k_zE.set(k_z),
            k_prE.set(k_pr),
            L_obE.set(L_ob),
            L_smoE.set(L_smo),
            potokObsE.set(potokObs))

def mnogokanal_SMO_bez():
    potokZav = float(potokZavE.get())  # lambda
    tAverage = float(tAverageE.get())  # Среднее время обслуживания в Часах
    n = int(nE.get())  # Количество каналов
    potokObs = (1 / tAverage)  # Интенсивонсть потока обслуживания U
    p = potokZav / potokObs  # Нагрузка системы
    p_rotv = round(p, 3)
    g = 1
    p_start = 0
    for i in range(n):
        p_start += p**n/fc(n)
        g += 1
    p0 = round((1/(1 + p_start + ((p**(n + 1))/(fc(n) * (n-p))))), 3)
    p_och = round((((p**(n + 1))/(fc(n) * (n-p))) * p0), 3)
    L_och = round((n/(n-p)) * p_och, 3)
    T_och = round((L_och/potokZav), 3)
    T_smo = round((T_och + tAverage), 3)
    p1 = '0 %'
    Q = 1
    A = round((potokZav * Q), 3)
    n_z = round(p, 3)
    n_pr = round((n - n_z), 3)
    k_z = round(n_z / n, 3)
    potokObs = round(potokObs, 3)
    return (
        pE.set(p_rotv),
        P0E.set(p0),
        P1E.set(p1),
        QE.set(Q),
        AE.set(A),
        n_zE.set(n_z),
        n_prE.set(n_pr),
        L_ochE.set(L_och),
        T_ochE.set(T_och),
        T_smoE.set(T_smo),
        k_zE.set(k_z),
        potokObsE.set(potokObs))

def reset():
    potokZavE.set('')
    tAverageE.set('')
    nagruzka_mE.set('')
    pE.set('')
    P0E.set('')
    P1E.set('')
    QE.set('')
    AE.set('')
    L_ochE.set('')
    T_ochE.set('')
    T_smoE.set('')
    L_obE.set('')
    L_smoE.set('')
    T_obE.set('')
    n_zE.set('')
    k_zE.set('')
    potokObsE.set('')
    p_ochE.set('')
    n_prE.set('')
    k_prE.set('')
    nE.set('')


########################## GUI ##############################
root = tk.Tk()
root.title('Системы Массового Обслуживания')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

tablayout = Notebook(root)

######################## Tab 1 ###################

#####    ПЕРЕМЕННЫЕ    #####
potokZavE = tk.StringVar()
tAverageE = tk.StringVar()
P0E = tk.StringVar()
P1E = tk.StringVar()
AE = tk.StringVar()
QE = tk.StringVar()
nagruzka_mE = tk.StringVar()
pE = tk.StringVar()
L_ochE = tk.StringVar()
T_ochE = tk.StringVar()
T_smoE = tk.StringVar()
L_obE = tk.StringVar()
L_smoE = tk.StringVar()
nE = tk.StringVar()
n_zE = tk.StringVar()
k_zE = tk.StringVar()
T_obE = tk.StringVar()
potokObsE = tk.StringVar()
PnE = tk.StringVar()
n_prE = tk.StringVar()
k_prE = tk.StringVar()
p_ochE = tk.StringVar()
tab_odnokanal_otkaz = tk.Frame(tablayout)
tab_odnokanal_otkaz.pack(fill='both')
tablayout.add(tab_odnokanal_otkaz, text='Одноканальная с отказом')

left_frame = tk.Frame(tab_odnokanal_otkaz, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

right_frame = tk.Frame(tab_odnokanal_otkaz, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Одноканальная СМО с отказом', font=MYHEADER, width=42)
smo_label.place(relx=0.1, rely=0.05)
# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность (lambda/час)')
potokZav_label.place(relx=0.1, rely=0.2, width=210)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZavE)
potokZav_entry.place(relx=0.55, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания (t/час)')
tAverage_label.place(relx=0.1, rely=0.3, width=210)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverageE)
tAverage_entry.place(relx=0.55, rely=0.3)

# Вероятность простоя (P0)
Result_label = tk.Label(right_frame, text='Вероятность простоя (P0)')
Result_label.place(relx=0.1, rely=0.1, width=300)
Result_entry = tk.Entry(right_frame, textvariable=P0E)
Result_entry.place(relx=0.7, rely=0.1)

# Вероятность отказа (P1)
Result_label = tk.Label(right_frame, text='Вероятность отказа (Pотказ)')
Result_label.place(relx=0.1, rely=0.15, width=300)
Result_entry = tk.Entry(right_frame, textvariable=P1E)
Result_entry.place(relx=0.7, rely=0.15)

# относительная пропускная способность (Q)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (Q)')
Result_label.place(relx=0.1, rely=0.2, width=300)
Result_entry = tk.Entry(right_frame, textvariable=QE)
Result_entry.place(relx=0.7, rely=0.2)

# Абсолютная пропускная способность (A)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (A)')
Result_label.place(relx=0.1, rely=0.25, width=300)
Result_entry = tk.Entry(right_frame, textvariable=AE)
Result_entry.place(relx=0.7, rely=0.25)

# Интенсивонсть потока обслуживания (U)
Result_label = tk.Label(right_frame, text='Интенсивонсть потока обслуживания (U)')
Result_label.place(relx=0.1, rely=0.3, width=300)
Result_entry = tk.Entry(right_frame, textvariable=potokObsE)
Result_entry.place(relx=0.7, rely=0.3)

# Автор
Result_label = tk.Label(right_frame, text='(c) Маштаков Кирилл ИС 3 курс', bg='#090909', fg='white')
Result_label.place(relx=0.55, rely=0.95, width=350)

button_odnokanal_otkaz = tk.Button(left_frame_inside, text='Рассчитать', command=odnokanal_SMO_otkaz, bg='#E50914',
                                   fg='white',
                                   font=MYFONT)
button_odnokanal_otkaz.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)

#############  TAB 2  #####################

tab_odnokonal_ochered = tk.Frame(tablayout)
tab_odnokonal_ochered.pack(fill='both')
tablayout.add(tab_odnokonal_ochered, text='Одноканальная с ограничением на очередь')

left_frame = tk.Frame(tab_odnokonal_ochered, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

right_frame = tk.Frame(tab_odnokonal_ochered, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Одноканальная СМО с ограничением на очередь', font=MYHEADER, width=42)
smo_label.place(relx=0.1, rely=0.05)

# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность (lambda/час)')
potokZav_label.place(relx=0.1, rely=0.2, width=210)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZavE)
potokZav_entry.place(relx=0.55, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания (t/час)')
tAverage_label.place(relx=0.1, rely=0.3, width=210)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverageE)
tAverage_entry.place(relx=0.55, rely=0.3)

nagruzka_m_label = tk.Label(left_frame_inside, text='Введите длину очереди (m)')
nagruzka_m_label.place(relx=0.1, rely=0.4, width=210)
nagruzka_m_entry = tk.Entry(left_frame_inside, textvariable=nagruzka_mE)
nagruzka_m_entry.place(relx=0.55, rely=0.4)

# Нагрузка системы (p)
Result_label = tk.Label(right_frame, text='Нагрузка системы (p)')
Result_label.place(relx=0.1, rely=0.1, width=350)
Result_entry = tk.Entry(right_frame, textvariable=pE)
Result_entry.place(relx=0.7, rely=0.1)

# Вероятность простоя (P0)
Result_label = tk.Label(right_frame, text='Вероятность простоя (P0)')
Result_label.place(relx=0.1, rely=0.15, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P0E)
Result_entry.place(relx=0.7, rely=0.15)

# Вероятность отказа (P1)
Result_label = tk.Label(right_frame, text='Вероятность отказа (Pотказ)')
Result_label.place(relx=0.1, rely=0.2, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P1E)
Result_entry.place(relx=0.7, rely=0.2)

# Относительная пропускная способность (Q)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (Q)')
Result_label.place(relx=0.1, rely=0.25, width=350)
Result_entry = tk.Entry(right_frame, textvariable=QE)
Result_entry.place(relx=0.7, rely=0.25)

# Абсолютная пропускная способность (A)
Result_label = tk.Label(right_frame, text='Абсолютная пропускная способность (A)')
Result_label.place(relx=0.1, rely=0.3, width=350)
Result_entry = tk.Entry(right_frame, textvariable=AE)
Result_entry.place(relx=0.7, rely=0.3)

# Ср. число заявок, стоящий в очереди на обслуживание (Lоч)
Result_label = tk.Label(right_frame, text='Ср. число заявок, стоящий в очереди на обслуживание (Lоч)')
Result_label.place(relx=0.1, rely=0.35, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_ochE)
Result_entry.place(relx=0.7, rely=0.35)

# Среднее время ожидания обслужвания (Tоч)
Result_label = tk.Label(right_frame, text='Среднее время ожидания обслужвания (Tоч)')
Result_label.place(relx=0.1, rely=0.4, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_ochE)
Result_entry.place(relx=0.7, rely=0.4)

# Среднее время пребывания заявки в системе (Tсмо)
Result_label = tk.Label(right_frame, text='Среднее время пребывания заявки в системе (Tсмо)')
Result_label.place(relx=0.1, rely=0.45, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_smoE)
Result_entry.place(relx=0.7, rely=0.45)

# Ср. число заявок, находящихся на обслуживании (Lоб)
Result_label = tk.Label(right_frame, text='Ср. число заявок, находящихся на обслуживании (Lоб)')
Result_label.place(relx=0.1, rely=0.5, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_obE)
Result_entry.place(relx=0.7, rely=0.5)

# Ср. число завяок, находящихся в системе (Lсмо)
Result_label = tk.Label(right_frame, text='Ср. число завяок, находящихся в системе (Lсмо)')
Result_label.place(relx=0.1, rely=0.55, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_smoE)
Result_entry.place(relx=0.7, rely=0.55)

# Интенсивонсть потока обслуживания (U)
Result_label = tk.Label(right_frame, text='Интенсивонсть потока обслуживания (U)')
Result_label.place(relx=0.1, rely=0.6, width=350)
Result_entry = tk.Entry(right_frame, textvariable=potokObsE)
Result_entry.place(relx=0.7, rely=0.6)

# Автор
Result_label = tk.Label(right_frame, text='(c) Маштаков Кирилл ИС 3 курс', bg='#090909', fg='white')
Result_label.place(relx=0.55, rely=0.95, width=350)

button_odnokonal_ochered = tk.Button(left_frame_inside, text='Рассчитать', command=ondokanal_SMO_dlina_ocheredi,
                                     bg='#E50914', fg='white',
                                     font=MYFONT)
button_odnokonal_ochered.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)

#####   TAB 3 #########

tab_odnokonal_bez = tk.Frame(tablayout)
tab_odnokonal_bez.pack(fill='both')
tablayout.add(tab_odnokonal_bez, text='Одноканальная без ограничений')

left_frame = tk.Frame(tab_odnokonal_bez, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

right_frame = tk.Frame(tab_odnokonal_bez, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Одноканальная СМО без ограничений', font=MYHEADER, width=42)
smo_label.place(relx=0.1, rely=0.05)

# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность (lambda/час)')
potokZav_label.place(relx=0.1, rely=0.2, width=210)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZavE)
potokZav_entry.place(relx=0.55, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания (t/час)')
tAverage_label.place(relx=0.1, rely=0.3, width=210)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverageE)
tAverage_entry.place(relx=0.55, rely=0.3)

# Нагрузка системы (p)
Result_label = tk.Label(right_frame, text='Нагрузка системы (p)')
Result_label.place(relx=0.1, rely=0.1, width=350)
Result_entry = tk.Entry(right_frame, textvariable=pE)
Result_entry.place(relx=0.7, rely=0.1)

# Вероятность простоя (P0)
Result_label = tk.Label(right_frame, text='Вероятность простоя (P0)')
Result_label.place(relx=0.1, rely=0.15, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P0E)
Result_entry.place(relx=0.7, rely=0.15)

# Вероятность отказа (P1)
Result_label = tk.Label(right_frame, text='Вероятность отказа (Pотказ)')
Result_label.place(relx=0.1, rely=0.2, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P1E)
Result_entry.place(relx=0.7, rely=0.2)

# Относительная пропускная способность (Q)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (Q)')
Result_label.place(relx=0.1, rely=0.25, width=350)
Result_entry = tk.Entry(right_frame, textvariable=QE)
Result_entry.place(relx=0.7, rely=0.25)

# Абсолютная пропускная способность (A)
Result_label = tk.Label(right_frame, text='Абсолютная пропускная способность (A)')
Result_label.place(relx=0.1, rely=0.3, width=350)
Result_entry = tk.Entry(right_frame, textvariable=AE)
Result_entry.place(relx=0.7, rely=0.3)

# Ср. число заявок, стоящий в очереди на обслуживание (Lоч)
Result_label = tk.Label(right_frame, text='Ср. число заявок, стоящий в очереди на обслуживание (Lоч)')
Result_label.place(relx=0.1, rely=0.35, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_ochE)
Result_entry.place(relx=0.7, rely=0.35)

# Среднее время ожидания обслужвания (Tоч)
Result_label = tk.Label(right_frame, text='Среднее время ожидания обслужвания (Tоч)')
Result_label.place(relx=0.1, rely=0.4, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_ochE)
Result_entry.place(relx=0.7, rely=0.4)

# Среднее время пребывания заявки в системе (Tсмо)
Result_label = tk.Label(right_frame, text='Среднее время пребывания заявки в системе (Tсмо)')
Result_label.place(relx=0.1, rely=0.45, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_smoE)
Result_entry.place(relx=0.7, rely=0.45)

# Ср. число завяок, находящихся в системе (Lсмо)
Result_label = tk.Label(right_frame, text='Ср. число завяок, находящихся в системе (Lсмо)')
Result_label.place(relx=0.1, rely=0.5, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_smoE)
Result_entry.place(relx=0.7, rely=0.5)

# Интенсивонсть потока обслуживания (U)
Result_label = tk.Label(right_frame, text='Интенсивонсть потока обслуживания (U)')
Result_label.place(relx=0.1, rely=0.55, width=350)
Result_entry = tk.Entry(right_frame, textvariable=potokObsE)
Result_entry.place(relx=0.7, rely=0.55)

# Автор
Result_label = tk.Label(right_frame, text='(c) Маштаков Кирилл ИС 3 курс', bg='#090909', fg='white')
Result_label.place(relx=0.55, rely=0.95, width=350)

button_odnokonal_bez = tk.Button(left_frame_inside, text='Рассчитать', command=odnokanal_SMO_bez,
                                 bg='#E50914', fg='white',
                                 font=MYFONT)
button_odnokonal_bez.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)

#####   TAB 4 #########

tab_mnogokanal_bez = tk.Frame(tablayout)
tab_mnogokanal_bez.pack(fill='both')
tablayout.add(tab_mnogokanal_bez, text='Многоканальная с отказом')

left_frame = tk.Frame(tab_mnogokanal_bez, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

right_frame = tk.Frame(tab_mnogokanal_bez, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Многоканальная СМО с отказом', font=MYHEADER, width=42)
smo_label.place(relx=0.1, rely=0.05)

# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность (lambda/час)')
potokZav_label.place(relx=0.1, rely=0.2, width=210)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZavE)
potokZav_entry.place(relx=0.55, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания (t/час)')
tAverage_label.place(relx=0.1, rely=0.3, width=210)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverageE)
tAverage_entry.place(relx=0.55, rely=0.3)

n_label = tk.Label(left_frame_inside, text='Введите количество каналов (n)')
n_label.place(relx=0.1, rely=0.4, width=210)
n_entry = tk.Entry(left_frame_inside, textvariable=nE)
n_entry.place(relx=0.55, rely=0.4)

# Нагрузка системы (p)
Result_label = tk.Label(right_frame, text='Нагрузка системы (p)')
Result_label.place(relx=0.1, rely=0.1, width=350)
Result_entry = tk.Entry(right_frame, textvariable=pE)
Result_entry.place(relx=0.7, rely=0.1)

# Вероятность простоя (P0)
Result_label = tk.Label(right_frame, text='Вероятность простоя (P0)')
Result_label.place(relx=0.1, rely=0.15, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P0E)
Result_entry.place(relx=0.7, rely=0.15)

# Вероятность отказа (P1)
Result_label = tk.Label(right_frame, text='Вероятность отказа (Pотказ)')
Result_label.place(relx=0.1, rely=0.2, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P1E)
Result_entry.place(relx=0.7, rely=0.2)

# Относительная пропускная способность (Q)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (Q)')
Result_label.place(relx=0.1, rely=0.25, width=350)
Result_entry = tk.Entry(right_frame, textvariable=QE)
Result_entry.place(relx=0.7, rely=0.25)

# Абсолютная пропускная способность (A)
Result_label = tk.Label(right_frame, text='Абсолютная пропускная способность (A)')
Result_label.place(relx=0.1, rely=0.3, width=350)
Result_entry = tk.Entry(right_frame, textvariable=AE)
Result_entry.place(relx=0.7, rely=0.3)

# Среднее время пребывания заявки в системе (Tсмо)
Result_label = tk.Label(right_frame, text='Среднее время пребывания заявки в системе (Tсмо)')
Result_label.place(relx=0.1, rely=0.35, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_smoE)
Result_entry.place(relx=0.7, rely=0.35)

# Ср. время обслуживания каналом одной заявки (Tоб)
Result_label = tk.Label(right_frame, text='Ср. время обслуживания каналом одной заявки (Tоб)')
Result_label.place(relx=0.1, rely=0.4, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_obE)
Result_entry.place(relx=0.7, rely=0.4)

# Число каналов занятый обслуживанием (Nз)
Result_label = tk.Label(right_frame, text='Число каналов занятый обслуживанием (Nз)')
Result_label.place(relx=0.1, rely=0.45, width=350)
Result_entry = tk.Entry(right_frame, textvariable=n_zE)
Result_entry.place(relx=0.7, rely=0.45)

# Коэффициент занятости каналов (Kз)
Result_label = tk.Label(right_frame, text='Коэффициент занятости каналов (Kз)')
Result_label.place(relx=0.1, rely=0.5, width=350)
Result_entry = tk.Entry(right_frame, textvariable=k_zE)
Result_entry.place(relx=0.7, rely=0.5)

# Интенсивонсть потока обслуживания (U)
Result_label = tk.Label(right_frame, text='Интенсивонсть потока обслуживания (U)')
Result_label.place(relx=0.1, rely=0.55, width=350)
Result_entry = tk.Entry(right_frame, textvariable=potokObsE)
Result_entry.place(relx=0.7, rely=0.55)

# Автор
Result_label = tk.Label(right_frame, text='(c) Маштаков Кирилл ИС 3 курс', bg='#090909', fg='white')
Result_label.place(relx=0.55, rely=0.95, width=350)

button_mnogokanal_okaz = tk.Button(left_frame_inside, text='Рассчитать', command=mnogokanal_SMO_otkaz,
                                   bg='#E50914', fg='white',
                                   font=MYFONT)
button_mnogokanal_okaz.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)

#####   TAB 5 #########

tab_mnogokanal_ochered = tk.Frame(tablayout)
tab_mnogokanal_ochered.pack(fill='both')
tablayout.add(tab_mnogokanal_ochered, text='Многоканальная с ограниченной очередью')

left_frame = tk.Frame(tab_mnogokanal_ochered, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

right_frame = tk.Frame(tab_mnogokanal_ochered, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Многоканальная СМО с ограничением на очередь', font=MYHEADER, width=42)
smo_label.place(relx=0.1, rely=0.05)

# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность (lambda/час)')
potokZav_label.place(relx=0.1, rely=0.2, width=210)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZavE)
potokZav_entry.place(relx=0.55, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания (t/час)')
tAverage_label.place(relx=0.1, rely=0.3, width=210)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverageE)
tAverage_entry.place(relx=0.55, rely=0.3)

n_label = tk.Label(left_frame_inside, text='Введите количество каналов (n)')
n_label.place(relx=0.1, rely=0.4, width=210)
n_entry = tk.Entry(left_frame_inside, textvariable=nE)
n_entry.place(relx=0.55, rely=0.4)

n_label = tk.Label(left_frame_inside, text='Введите длину очереди (m)')
n_label.place(relx=0.1, rely=0.5, width=210)
n_entry = tk.Entry(left_frame_inside, textvariable=nagruzka_mE)
n_entry.place(relx=0.55, rely=0.5)

# Нагрузка системы (p)
Result_label = tk.Label(right_frame, text='Нагрузка системы (p)')
Result_label.place(relx=0.1, rely=0.1, width=350)
Result_entry = tk.Entry(right_frame, textvariable=pE)
Result_entry.place(relx=0.7, rely=0.1)

# Вероятность простоя (P0)
Result_label = tk.Label(right_frame, text='Вероятность простоя (P0)')
Result_label.place(relx=0.1, rely=0.15, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P0E)
Result_entry.place(relx=0.7, rely=0.15)

#  Вероятность того, что в СМО находится какое-либо кол-во заявок (Pn)
Result_label = tk.Label(right_frame, text='Вероятность того, что СМО есть заявоки (Pn)')
Result_label.place(relx=0.1, rely=0.2, width=350)
Result_entry = tk.Entry(right_frame, textvariable=PnE)
Result_entry.place(relx=0.7, rely=0.2)

#  Вероятность образования очереди (Pоч)
Result_label = tk.Label(right_frame, text='Вероятность образования очереди (Pоч)')
Result_label.place(relx=0.1, rely=0.25, width=350)
Result_entry = tk.Entry(right_frame, textvariable=p_ochE)
Result_entry.place(relx=0.7, rely=0.25)

# Вероятность отказа (P1)
Result_label = tk.Label(right_frame, text='Вероятность отказа (Pотказ)')
Result_label.place(relx=0.1, rely=0.3, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P1E)
Result_entry.place(relx=0.7, rely=0.3)

# Относительная пропускная способность (Q)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (Q)')
Result_label.place(relx=0.1, rely=0.35, width=350)
Result_entry = tk.Entry(right_frame, textvariable=QE)
Result_entry.place(relx=0.7, rely=0.35)

# Абсолютная пропускная способность (A)
Result_label = tk.Label(right_frame, text='Абсолютная пропускная способность (A)')
Result_label.place(relx=0.1, rely=0.4, width=350)
Result_entry = tk.Entry(right_frame, textvariable=AE)
Result_entry.place(relx=0.7, rely=0.4)

# Среднее время пребывания заявки в системе (Tсмо)
Result_label = tk.Label(right_frame, text='Среднее время пребывания заявки в системе (Tсмо)')
Result_label.place(relx=0.1, rely=0.45, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_smoE)
Result_entry.place(relx=0.7, rely=0.45)

# Число каналов занятый обслуживанием (Nз)
Result_label = tk.Label(right_frame, text='Число каналов занятый обслуживанием (Nз)')
Result_label.place(relx=0.1, rely=0.5, width=350)
Result_entry = tk.Entry(right_frame, textvariable=n_zE)
Result_entry.place(relx=0.7, rely=0.5)

# Ср. Число простаивающих каналов (Nпр)
Result_label = tk.Label(right_frame, text='Ср. Число простаивающих каналов (Nпр)')
Result_label.place(relx=0.1, rely=0.55, width=350)
Result_entry = tk.Entry(right_frame, textvariable=n_prE)
Result_entry.place(relx=0.7, rely=0.55)

# Ср. число заявок, стоящий в очереди (Lоч)
Result_label = tk.Label(right_frame, text='Ср. число заявок, стоящий в очереди (Lоч)')
Result_label.place(relx=0.1, rely=0.6, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_ochE)
Result_entry.place(relx=0.7, rely=0.6)

# Среднее время ожидания обслужвания (Tоч)
Result_label = tk.Label(right_frame, text='Среднее время ожидания обслужвания (Tоч)')
Result_label.place(relx=0.1, rely=0.65, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_ochE)
Result_entry.place(relx=0.7, rely=0.65)

# Коэффициент занятости каналов (Kз)
Result_label = tk.Label(right_frame, text='Коэффициент занятости каналов (Kз)')
Result_label.place(relx=0.1, rely=0.7, width=350)
Result_entry = tk.Entry(right_frame, textvariable=k_zE)
Result_entry.place(relx=0.7, rely=0.7)

# Коэффициент простоя каналов (Kпр)
Result_label = tk.Label(right_frame, text='Коэффициент простоя каналов (Kпр)')
Result_label.place(relx=0.1, rely=0.75, width=350)
Result_entry = tk.Entry(right_frame, textvariable=k_prE)
Result_entry.place(relx=0.7, rely=0.75)

# Ср.число заявок, находящихся на обслуживании (Lоб)
Result_label = tk.Label(right_frame, text='Ср.число заявок, находящихся на обслуживании (Lоб)')
Result_label.place(relx=0.1, rely=0.8, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_obE)
Result_entry.place(relx=0.7, rely=0.8)

# Ср. число завяок, находящихся в системе (Lсмо)
Result_label = tk.Label(right_frame, text='Ср. число завяок, находящихся в системе (Lсмо)')
Result_label.place(relx=0.1, rely=0.85, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_smoE)
Result_entry.place(relx=0.7, rely=0.85)

# Интенсивонсть потока обслуживания (U)
Result_label = tk.Label(right_frame, text='Интенсивонсть потока обслуживания (U)')
Result_label.place(relx=0.1, rely=0.9, width=350)
Result_entry = tk.Entry(right_frame, textvariable=potokObsE)
Result_entry.place(relx=0.7, rely=0.9)

# Автор
Result_label = tk.Label(right_frame, text='(c) Маштаков Кирилл ИС 3 курс', bg='#090909', fg='white')
Result_label.place(relx=0.55, rely=0.95, width=350)

button_mnogokanal_ochered = tk.Button(left_frame_inside, text='Рассчитать', command=mnogokanal_SMO_dlina_ocheredi,
                                      bg='#E50914', fg='white',
                                      font=MYFONT)
button_mnogokanal_ochered.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)


#####   TAB 6 #########

tab_mnogokanal_bez = tk.Frame(tablayout)
tab_mnogokanal_bez.pack(fill='both')
tablayout.add(tab_mnogokanal_bez, text='Многоканальная без ограничений')

left_frame = tk.Frame(tab_mnogokanal_bez, bg='#020202')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

right_frame = tk.Frame(tab_mnogokanal_bez, bg='#090909')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

left_frame_inside = tk.Frame(left_frame, bg='#090909')
left_frame_inside.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

smo_label = tk.Label(left_frame_inside, text='Многоканальная СМО без ограничений', font=MYHEADER, width=42)
smo_label.place(relx=0.1, rely=0.05)

# Значения для задачи
potokZav_label = tk.Label(left_frame_inside, text='Введите интенсивность (lambda/час)')
potokZav_label.place(relx=0.1, rely=0.2, width=210)
potokZav_entry = tk.Entry(left_frame_inside, textvariable=potokZavE)
potokZav_entry.place(relx=0.55, rely=0.2)

tAverage_label = tk.Label(left_frame_inside, text='Введите время обслуживания (t/час)')
tAverage_label.place(relx=0.1, rely=0.3, width=210)
tAverage_entry = tk.Entry(left_frame_inside, textvariable=tAverageE)
tAverage_entry.place(relx=0.55, rely=0.3)

n_label = tk.Label(left_frame_inside, text='Введите количество каналов (n)')
n_label.place(relx=0.1, rely=0.4, width=210)
n_entry = tk.Entry(left_frame_inside, textvariable=nE)
n_entry.place(relx=0.55, rely=0.4)

# Нагрузка системы (p)
Result_label = tk.Label(right_frame, text='Нагрузка системы (p)')
Result_label.place(relx=0.1, rely=0.1, width=350)
Result_entry = tk.Entry(right_frame, textvariable=pE)
Result_entry.place(relx=0.7, rely=0.1)

# Вероятность простоя (P0)
Result_label = tk.Label(right_frame, text='Вероятность простоя (P0)')
Result_label.place(relx=0.1, rely=0.15, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P0E)
Result_entry.place(relx=0.7, rely=0.15)

# Вероятность отказа (P1)
Result_label = tk.Label(right_frame, text='Вероятность отказа (Pотказ)')
Result_label.place(relx=0.1, rely=0.2, width=350)
Result_entry = tk.Entry(right_frame, textvariable=P1E)
Result_entry.place(relx=0.7, rely=0.2)

# Относительная пропускная способность (Q)
Result_label = tk.Label(right_frame, text='Относительная пропускная способность (Q)')
Result_label.place(relx=0.1, rely=0.25, width=350)
Result_entry = tk.Entry(right_frame, textvariable=QE)
Result_entry.place(relx=0.7, rely=0.25)

# Абсолютная пропускная способность (A)
Result_label = tk.Label(right_frame, text='Абсолютная пропускная способность (A)')
Result_label.place(relx=0.1, rely=0.3, width=350)
Result_entry = tk.Entry(right_frame, textvariable=AE)
Result_entry.place(relx=0.7, rely=0.3)

# Среднее время пребывания заявки в системе (Tсмо)
Result_label = tk.Label(right_frame, text='Среднее время пребывания заявки в системе (Tсмо)')
Result_label.place(relx=0.1, rely=0.35, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_smoE)
Result_entry.place(relx=0.7, rely=0.35)

# Число каналов занятый обслуживанием (Nз)
Result_label = tk.Label(right_frame, text='Число каналов занятый обслуживанием (Nз)')
Result_label.place(relx=0.1, rely=0.4, width=350)
Result_entry = tk.Entry(right_frame, textvariable=n_zE)
Result_entry.place(relx=0.7, rely=0.4)

# Ср. Число простаивающих каналов (Nпр)
Result_label = tk.Label(right_frame, text='Ср. Число простаивающих каналов (Nпр)')
Result_label.place(relx=0.1, rely=0.45, width=350)
Result_entry = tk.Entry(right_frame, textvariable=n_prE)
Result_entry.place(relx=0.7, rely=0.45)

# Ср. число заявок, стоящий в очереди (Lоч)
Result_label = tk.Label(right_frame, text='Ср. число заявок, стоящий в очереди (Lоч)')
Result_label.place(relx=0.1, rely=0.5, width=350)
Result_entry = tk.Entry(right_frame, textvariable=L_ochE)
Result_entry.place(relx=0.7, rely=0.5)

# Среднее время ожидания обслужвания (Tоч)
Result_label = tk.Label(right_frame, text='Среднее время ожидания обслужвания (Tоч)')
Result_label.place(relx=0.1, rely=0.55, width=350)
Result_entry = tk.Entry(right_frame, textvariable=T_ochE)
Result_entry.place(relx=0.7, rely=0.55)

# Коэффициент занятости каналов (Kз)
Result_label = tk.Label(right_frame, text='Коэффициент занятости каналов (Kз)')
Result_label.place(relx=0.1, rely=0.6, width=350)
Result_entry = tk.Entry(right_frame, textvariable=k_zE)
Result_entry.place(relx=0.7, rely=0.6)

# Интенсивонсть потока обслуживания (U)
Result_label = tk.Label(right_frame, text='Интенсивонсть потока обслуживания (U)')
Result_label.place(relx=0.1, rely=0.65, width=350)
Result_entry = tk.Entry(right_frame, textvariable=potokObsE)
Result_entry.place(relx=0.7, rely=0.65)

# Автор
Result_label = tk.Label(right_frame, text='(c) Маштаков Кирилл ИС 3 курс', bg='#090909', fg='white')
Result_label.place(relx=0.55, rely=0.95, width=350)

button_mnogokanal_bez = tk.Button(left_frame_inside, text='Рассчитать', command=mnogokanal_SMO_bez,
                                      bg='#E50914', fg='white',
                                      font=MYFONT)
button_mnogokanal_bez.place(relx=0.15, rely=0.8, relwidth=0.5, relheight=0.1)
button_clear = tk.Button(left_frame_inside, text='Очистить', command=reset, font=MYFONT)
button_clear.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.22)

tablayout.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()
