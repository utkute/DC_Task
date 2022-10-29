from random import randint
a = randint(0, 100)
b = randint(1, 100)
print(a, b)
remainder = a % b
res = a//b
print("Результат целочисленного деления:", res)
print("Остаток от деления:", remainder)
