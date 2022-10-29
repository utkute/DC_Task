num = 123
is_positive = True
if num < 0:
    is_positive = False
res = "".join(reversed(str(abs(num))))
print("Начальное число: ", num)
if not is_positive:
    res = -int(res)
print("Обратное число: ", res)
