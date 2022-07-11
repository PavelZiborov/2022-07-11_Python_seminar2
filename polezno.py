def needDigit (text): # Функция, которая принимает на вход целое число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = int(number)
            return number
            needTrue = True
        except:
            print('Ошибка ввода. Введите целое число: ')

A = needDigit('Введите целое число: ')
print(A)

