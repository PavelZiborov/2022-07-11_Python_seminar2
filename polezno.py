def needIntNumber (text): # Функция, которая принимает на вход целое число
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

A = needIntNumber('Введите целое число: ')
print(A)

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

B = needFloatNumber('Введите вещественное число: ')
print(B)