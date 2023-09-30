a = int(input("Введите первое  число: "))
b = int(input("Введите второе  число: "))
maxx = 0
minn = 0
print("Сумма чисел:", a+b)
print("Разность чисел:", a-b)
print("Среднее арифметическое чисел:", (a+b)//2)
if a > 0 and b < 0:
    a = a
    b = b * (-1)
if a < 0 and b > 0:
    a = a * (-1)
    b = b
else:
    a = a
    b = b
if  a >= b:
    maxx = a
    minn = b
else:
    maxx = b
    minn = a
print("Разность максимального и минимального по модулю:", maxx-minn)