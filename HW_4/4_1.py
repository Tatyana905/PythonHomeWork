# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
from decimal import Decimal

num = str(pi)

d = input("Введите d:  ")
print(Decimal(num).quantize(Decimal(str(d))))



# from decimal import Decimal

# a = input("Введите число: ")
# d = input("Укажите точность в диапазоне: " )
# float_lst = Decimal(a)
# float_lst = float_lst.quantize(Decimal(d))
# print(float_lst)