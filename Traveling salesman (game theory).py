import pandas as pd

a = [[-1, 90, 80, 40, 80] ,
     [60, -1, 40, 50, 70],
     [50, 30, -1, 60, 20],
     [10, 70, 20, -1, 50],
     [20, 40, 50, 20, -1]]

maximum = 100


xarray=[-1]
yarray=[-1]

def reduce(a):

    n=5

    di = 0
    for i in range(n):

        minstring = maximum

        for j in range(n):
            if ((a[i][j]<minstring) and (a[i][j]>=0)):
                minstring = a[i][j]

        if minstring != maximum:
            di = di + minstring

        for j in range(n):
            if a[i][j] >= 0:
                if minstring != maximum:
                    a[i][j] = a[i][j] - minstring

    dj = 0
    mincolumn = [maximum,maximum,maximum,maximum,maximum]

    for i in range(n):
        for j in range(n):
            if a[i][j]<mincolumn[j] and a[i][j]>=0:
                mincolumn[j] = a[i][j]


    for i in range(n):
        for j in range(n):
            if a[i][j] >= 0 and mincolumn[j]!=maximum:
                a[i][j] -= mincolumn[j]

    for i in range(n):
        if mincolumn[i] != maximum:
            dj = dj + mincolumn[i]

    return di + dj

def branch_edge(a):
    bri=-1
    brj=-1
    resi=-1
    resj=-1

    n = 5

    minstring = [maximum,maximum,maximum,maximum,maximum]
    mincolumn = [maximum,maximum,maximum,maximum,maximum]

    for i in range(n):
        for j in range(n):
            if a[i][j]<mincolumn[j] and a[i][j]>0:
                mincolumn[j] = a[i][j]
            if a[i][j]<minstring[i] and a[i][j]>0:
                minstring[i] = a[i][j]

    for i in range(n):
        k = 0
        for j in range(n):
            if a[i][j] == 0:
                k+=1
        if k != 1:
            minstring[i] = 0
        k = 0

    for i in range(n):
        k = 0
        for j in range(n):
            if a[j][i] == 0:
                k+=1
        if k != 1:
            mincolumn[i] = 0
        k = 0

    for i in range(n):
        for j in range(n):
            if a[i][j] == 0 and (bri+brj)<(minstring[i]+mincolumn[j]) and not (j in xarray):

                bri=minstring[i]
                brj=mincolumn[j]
                resi = i
                resj = j


    return (resi,resj,bri+brj)

def rib_exclusion(x,y,a):
    n=5
    for i in range(n):
        for j in range(n):
            if i==x:
                a[i][j]=-1
            if y==j:
                a[i][j]=-1
            if i==y and j==x:
                a[i][j]=-1

def printa(a):
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])



H = reduce(a)
printa(a)

#Приведение матрицы по строкам и столбцам и нахождение нижней границы множества
#через сложение констант приведения
for i in range(3):
    print("\nШаг №" + str(i+1))
    x, y, H1 = branch_edge(a)
    #Определяем ребро ветвления
    #С этой целью для всех клеток матрицы с нулевыми элементами заменяем поочередно нули на
    # -1 и определяем для них сумму образовавшихся констант приведения
    #Определив ребро ветвления разбиваем множество решений на два подмножества (x,y) и (x*,y*)
    #Нижняя граница гамильтоновых циклов (x*,y*) равна наибольшей сумме констант приведения + Н
    xarray.append(x)
    yarray.append(y)
    rib_exclusion(x,y,a)
    print("Ребро:(" + str(x) + "," + str(y) + ")\nИсключение ребра:")
    printa(a)
    #Исключение ребра (x,y) проводится путем исключения всех элементов x-ой строки и y-го столбца
    #в которой элемент ayx заменяем на -1, для исключения образования негамильтонова цикла
    #В результате получим другую сокращенную матрицу (n-1 x n-1), которая подлежит операции приведения.
    print("Приведение сокращенной матрицы:")
    H2 = reduce(a)
    printa(a)
    #Нижняя граница подмножества (x,y) равна сумме констант приведения сокращенной матрицы + H
    H = H + min(H1,H2)
    #Выбираем из нижних границ (x,y) и (x*,y*) наименьшую и включаем ребро (x,y)


print("\n\nРасстояние = " + str(H))
