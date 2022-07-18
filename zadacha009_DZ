# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.




def needIntNumber(text):  # Функция, которая принимает на вход целое число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = int(number)
            needTrue = True
            return number
        except:
            print('Ошибка ввода. Введите целое число: ')


def List(number):
    list = []
    for i in range(-number, number + 1):
        list.append(i)
    return list


N = needIntNumber('Введите целое число: ')
L = List(N)
print(L)


try:
    with open('file.txt', 'r') as data:
        multiplication = 1
        for line in data: # пробегаем циклом по всем строчкам и печатаем их (читает строчку)
                multiplication = multiplication * L[int(line)]
except:
    multiplication = None
    print(f"Ошибка чтения файла. Не удалось считать строчку: '{line}'")
print(f'Произведение чисел равно: {multiplication}')
