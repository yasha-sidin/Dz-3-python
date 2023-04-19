# Задача 20: В настольной игре Скрабл (Scrabble)
# каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка;B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;K – 5 очков;J, X – 8 очков;Q, Z – 10 очков.
# А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
# ноутбук
# 12

dict = {}
first_value = 1
first_elements = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
for item in first_elements:
    dict[item] = first_value

second_value = 2
second_elements = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
for item in second_elements:
    dict[item] = second_value

third_value = 3
third_elements = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
for item in third_elements:
    dict[item] = third_value

forth_value = 4
forth_elements = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
for item in forth_elements:
    dict[item] = forth_value

fifth_value = 5
fifth_elements = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
for item in fifth_elements:
    dict[item] = fifth_value

sixth_value = 8
sixth_elements = ['J', 'X', 'Ш', 'Э', 'Ю']
for item in sixth_elements:
    dict[item] = sixth_value

seventh_value = 10
seventh_elements = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
for item in seventh_elements:
    dict[item] = seventh_value

result = 0
word = input("Введите слово капсом: ")
try:
    for letter in word:
        result += dict[letter]
    print(result)
except:
    print("В слово входят буквы, которые нельзя использовать")