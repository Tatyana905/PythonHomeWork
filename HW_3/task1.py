# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint

arr = []
sum_odd = 0

for i in range(6):
    arr.append(randint(0,20))
    if not i % 2 == 0:
        sum_odd += arr[i] 

print(arr)
print(f"Сумма элементов на нечетных позициях {sum_odd}")




