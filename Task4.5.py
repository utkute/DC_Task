num = 1
bit32_check = 2**31
is_positive = True
if num < 0:
    is_positive = False
res = int("".join(reversed(str(abs(num)))))
print("Начальное число: ", num)
if not is_positive:
    res = -res
    if abs(res) > bit32_check:
        res = 0
elif abs(res) > bit32_check - 1:
    res = 0
print("Обратное число: ", res)
