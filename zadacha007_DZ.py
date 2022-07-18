# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


def needFloatNumber(text):  # Функция, которая принимает на вход вещественное число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = float(number)
            needTrue = True
            return number
        except:
            print('Ошибка ввода. Введите вещественное число: ')

def sum_of_digits (float_number): # Функция, которая считает сумму цифр вещественного числа
    string_number = str(float_number)
    sum = 0
    for i in string_number:
        try:
            digit = int(i)
            sum = sum + digit
        except:
            None
    return sum

A = needFloatNumber('Введите вещественное число: ')
sum = sum_of_digits(A)
print(f'Сумма цифр в вещественном числе {A} = {sum}')