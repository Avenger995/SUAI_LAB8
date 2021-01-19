from pylab import *
import numpy as np
import csv


#       проверка правильного выбора местоположения
def check_country(country, mas_country):
    if country not in mas_country:
        print('Такого местоположения не существует. Выберете местоположение из списка.')
        return 1
    else:
        return 0


#       проверка k и p
def check_third(n):
    if n.isspace() or str(n) == '':  # Проверка на пустое значение
        print('Ничего не введено. Попробуйте ввести значение снова.')
        return 'Ничего не введено. Попробуйте ввести значение снова.'
    if str(n).isalpha():  # Проверка на численное значение
        print('Введен символ или несколько значений. Попробуйте ввести значение снова.')
        return 'Введен символ или несколько значений. Попробуйте ввести значение снова.'
    if float(n) < 0:  # Проверка на <0
        print('Введено отрицательное значение. Попробуйте ввести значение снова.')
        return 'Введено отрицательное значение. Попробуйте ввести значение снова.'
    if float(n) > 36:  # Проверка на максимальное кол-во стран
        print('Превышен лимит. Попробуйте ввести значение снова.')
        return 'Превышен лимит. Попробуйте ввести значение снова.'
    try:    # Проверка на вещественное число
        int(n)
    except ValueError:
        print('Введено вещественное число. Попробуйте ввести значение снова.')
        return 'Введено вещественное число. Попробуйте ввести значение снова.'
    return 0

mas = []
mas_country = []
x = []
y1 = []
y2 = []
file1 = [["MAXLOCNUC", "MAXLOCTOT", "DECADEFROM", "DECADEUNTIL"]]
file2 = [["MINLOCNUC", "MINLOCTOT", "DECADEFROM", "DECADEUNTIL"]]
nuct = []
nuc = []
tot = []
tott = []

#       чтение csv-файла
with open("ElectricityGeneration.csv", 'r', encoding='utf-8') as rfile:
    fileridder = csv.reader(rfile, delimiter=",")
    for line in fileridder:
        if line != []:
            if '#' not in line[0]:
                mas.append(line)
rfile.close()

#       выбор страны
for i in mas:
    if i[0] not in mas_country and i[0] != 'LOCATION' and i[3] == 'GWH':
        mas_country.append(i[0])
print('Выберете местоположение из списка ниже для которого Вы хотите построить график:')
for i in mas_country:
    print(i, end=' ')
print()
country = input()
country = country.upper()
while check_country(country, mas_country):
    country = input()
    country = country.upper()

#       отбор значений для графика
for i in mas:
    if i[0] == country and i[2] == 'NUCLEAR' and i[7] == '' and i[3] == 'GWH':
        x.append(int(i[5]))
        y1.append(float(i[6]))
    if i[0] == country and i[2] == 'TOT' and i[7] == '' and i[3] == 'GWH':
        y2.append(float(i[6]))


#       построение графика
fig, ax = plt.subplots()
ax.plot(x, y1, label='NUCLEAR')
ax.plot(x, y2, label='TOT')
ax.grid()  # Сетка
ax.legend(loc=2)  # Легенда
ax.set_title(country)   # Название страны графика
ax.set_xlabel('Годы')   # Подпись к оси x
ax.set_ylabel('Кол-во воспроизводимой энергии (А)')     # Подпись к оси y
show()

#       доп задание
print()

k = input('Введите k:')
while check_third(k):
    k = input('Введите k:')

p = input('Введите p:')
while check_third(p):
    p = input('Введите p:')

year = 1960
while year <= 2015:
    nuct = []
    nuc = []
    tot = []
    tott = []

    for i in mas:
        if i[3] == 'GWH' and i[2] == 'NUCLEAR' and year <= int(i[5]) and int(i[5])<= int(year) + 9 and int(i[5]) != 2015:
            try:
                float(i[6])
            except ValueError:
                i[6] = 0
            nuct.append(i[0])
            nuc.append(float(i[6]))
        elif i[3] == 'GWH' and i[2] == 'TOT' and year <= int(i[5]) and int(i[5]) <= year + 9 and int(i[5]) != 2015:
            try:
                float(i[6])
            except ValueError:
                i[6] = 0
            tott.append(i[0])
            tot.append(float(i[6]))

    for j in range(int(k)):
        maxindexnuc = nuct[nuc.index(max(nuc))]
        maxindextot = tott[tot.index(max(tot))]
        file1.append([maxindexnuc, maxindextot, int(year), year+9])
        indexsave = [z for z, ltr in enumerate(nuct) if ltr == maxindexnuc]
        nuct[:] = [x for z,x in enumerate(nuct) if z not in indexsave]
        nuc[:] = [x for z,x in enumerate(nuc) if z not in indexsave]
        indexsave = [z for z, ltr in enumerate(tott) if ltr == maxindextot]
        tott[:] = [x for z, x in enumerate(tott) if z not in indexsave]
        tot[:] = [x for z, x in enumerate(tot) if z not in indexsave]

    for i in mas:
        if i[3] == 'GWH' and i[2] == 'NUCLEAR' and year <= int(i[5]) and int(i[5])<= int(year) + 9 and int(i[5]) != 2015:
            try:
                float(i[6])
            except ValueError:
                i[6] = 0
            nuct.append(i[0])
            nuc.append(float(i[6]))
        elif i[3] == 'GWH' and i[2] == 'TOT' and year <= int(i[5]) and int(i[5]) <= year + 9 and int(i[5]) != 2015:
            try:
                float(i[6])
            except ValueError:
                i[6] = 0
            tott.append(i[0])
            tot.append(float(i[6]))

    for j in range(int(p)):
        minindexnuc = nuct[nuc.index(min(nuc))]
        minindextot = tott[tot.index(min(tot))]
        file2.append([minindexnuc, minindextot, int(year), year+9])
        indexsave = [z for z, ltr in enumerate(nuct) if ltr == minindexnuc]
        nuct[:] = [x for z,x in enumerate(nuct) if z not in indexsave]
        nuc[:] = [x for z,x in enumerate(nuc) if z not in indexsave]
        indexsave = [z for z, ltr in enumerate(tott) if ltr == minindextot]
        tott[:] = [x for z, x in enumerate(tott) if z not in indexsave]
        tot[:] = [x for z, x in enumerate(tot) if z not in indexsave]

    year += 10

#       Запись в первый файл
my_file1 = open('MAXFILE.csv', 'w')
my_file1.write('Максимальные значения\n')
for line in file1:
    for j in line:
        a = str(j)+','
        my_file1.write(str(a))
    my_file1.write('\n')
my_file1.close()


#       Запись во второй файл
my_file1 = open('MINFILE.csv', 'w')
my_file1.write('Минимальные значения\n')
for line in file2:
    for j in line:
        a = str(j) + ','
        my_file1.write(str(a))
    my_file1.write('\n')
my_file1.close()
