# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


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


def sequence(N):  # Функция, которая возвращает список из произведений чисел от 1 до N
    try:
        if N > 0:
            list = [1]
            for i in range(1, N):
                next = list[i-1] * (i+1)
                list.append(next)
            return list
    except:
        print('входящее число должно быть > 0')
        return None


N = needIntNumber('Введите целое число: ')
S = sequence(N)
print(f'Последовательность = {S}')
