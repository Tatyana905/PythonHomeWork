# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите цифру от 1 до 7  -  '))
if 1<= a <=5:
    print("да")
elif 6<= a <=7:
    print("нет")
else:
    print("Не в диапазоне от 1 до 7, повторите ввод")