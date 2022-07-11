
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math
def Sqrt(x1, y1, x2, y2):
    sqrt = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    print(sqrt)
    return(sqrt)

X1 = float(input('Введите координату X1: '))
Y1 = float(input('Введите координату Y1: '))
X2 = float(input('Введите координату X2: '))
Y2 = float(input('Введите координату Y2: '))

Sqrt(X1,Y1,X2,Y2)