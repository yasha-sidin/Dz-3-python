# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

import random

n = int(input('Введите количество элементов массива: '))
array = []
for i in range(n):
    array.append(random.randint(0, 15))
print(array)

searched_number = int(input('Введите число, самое близкое число к которому будем искать: '))
diff = abs(searched_number - array[0])
index = 0
temp_diff = 0
for i in range (1, n):
    temp_diff = abs(searched_number - array[i])
    if (temp_diff < diff):
        index = i
print(array[index])
