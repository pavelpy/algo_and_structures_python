"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

mas_in = input("введите элементы массива через пробел: ")
mas_in = mas_in.split()

mas = [int(s) for s in mas_in]

mas.sort()

if len(mas) == 1:
    print("массив содержит только один элемент: ", mas[0])
else:
    print("два наименьших элемента массива: %d и %d" % (mas[0], mas[1]))
