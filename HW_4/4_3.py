# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


def fil(array):
    res = []
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if count == 1:
            res.append(array[i])
    print(res)
    
array = [4, 5, 3, 3, 4, 1, 2]
fil(array)