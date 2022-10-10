# 1.Напишите программу, которая принимает на вход вещественное
#  число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите число  '))
sum_digits = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum_digits += num % 10
    num //= 10

print(int(sum_digits))

# # через список

# print('Enter a real number:', end = ' ')
# num_list = list(input())
# sum_dig = 0

# for i in range(len(num_list)):
# if num_list[i] == '.':
# continue
# sum_dig += int(num_list[i])
# print(sum_dig)

# #==============================

# # математически

# print('Enter a real number:', end = ' ')
# num = input()
# # print(type(num)) #str
# count = 10 ** (len(num) - 2)
# # print(type(count)) #int
# # print(count)
# num = int(float(num) * count)
# # print(num)
# res = 0
# while num > 0:
# res += num % 10
# num //= 10
# print(res)


# #Вариант 1
# numb = input("Введите число: ")
# sum1 = 0
# for digit in numb:
# if digit.isdigit():
# sum1 += int(digit)
# print(f"Сумма цифр числа {numb} равна:", sum1)

# #Вариант 2
# # number = input("Введите число: ")
# # n = int(float((number).replace(",", ".")) * (10 ** (len(number) - 2)))
# # sum1 = 0
# # while n != 0:
# # sum1 += n % 10
# # n = n // 10
# # print(f"Сумма цифр числа {number} равна:", sum1)