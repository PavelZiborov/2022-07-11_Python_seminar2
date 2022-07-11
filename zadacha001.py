# 1) Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.




def verification_of_truth_of_statement(x, y, z):
    left = not(x or y or z)
    right = not x and not y and not z
    if left == right:
        return True
    else:
        return False


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(verification_of_truth_of_statement(x, y, z))

