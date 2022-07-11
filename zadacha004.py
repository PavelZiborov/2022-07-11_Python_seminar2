





# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.


import math


def needDigit(text):  # Функция, которая принимает на вход целое число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = float(number)
            return number
            needTrue = True
        except:
            print('Ошибка ввода. Введите целое число: ')

# def list_of_numbers_and_operations(new_string):
#     list_of_numbers = []
#     num = ''
#     for i in range(len(new_string)):
#         if new_string[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
#             num += new_string[i]
#             if i == len(new_string) - 1:
#                 list_of_numbers.append(num)
#         elif new_string[i] in ['*', '/', '+', '-']:
#             list_of_numbers.append(num)
#             list_of_numbers.append(new_string[i])
#             num =''

#     return list_of_numbers


# РАЗОБРАТЬ:

# дешифратор
# alphabet_list = str(input("Введите пример: "))
# str_a=''
# str_b=''
# t=0
# C = ''
# for i in alphabet_list: 
#      if chr(ord(i))=='+' or chr(ord(i))=='-' or chr(ord(i))=='*' or chr(ord(i))=='/':
#       C = chr(ord(i))
#       t=1
#      elif t==0:
#         str_a = str_a+''.join(chr(ord(i)))
#      elif t==1:
#         str_b = str_b+''.join(chr(ord(i)))    
# A = float(str_a)
# B = float(str_b)

# #тело калькулятора
# if C == '/':
#     if B==0:
#         print ('На ноль делить нельзя')
#     else:
#          print (A/B)
# if C == '+': 
#     print (A+B)
# if C == '-': 
#     print (A-B)
# if C == '*': 
#     print (A*B)


def Calculator(A, operator, B):
    try:
        if operator == '+':
            return A + B
        elif operator == '-':
            return A - B
        elif operator == '/':
            return A / B
        elif operator == '*':
            return A * B
        elif operator == 'mod':
            return A % B
        elif operator == 'pow':
            return A ** B
        elif operator == 'div':
            return A // B
    except:
        print('Ошибка вычисления.')


A = needDigit('Введите первое число: ')
operator = input(('Введите операцию (+, -, *, /, mod, pow, div): '))
B = needDigit('Введите второе число: ')
print(f'A {operator} B = {Calculator(A, operator, B)}')

s = '5.1535*1.55'
print(eval(s)) # eval встроенная функция 
help(eval)