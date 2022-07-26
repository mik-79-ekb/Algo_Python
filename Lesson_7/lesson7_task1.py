"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import timeit
import random


def bubble_sort(orig_list, reverse=False):
    n = 1
    flag = True
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if not reverse:
                if orig_list[i] < orig_list[i + 1]:
                    orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                    flag = False
            else:
                if orig_list[i] > orig_list[i + 1]:
                    orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                    flag = False
        if flag:
            return orig_list
        n += 1
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(orig_list)
print(bubble_sort(orig_list, reverse=True))


# замеры 10
print(timeit.timeit("bubble_sort(orig_list, reverse=True)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list, reverse=True)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list, reverse=True)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

"""
[-80, 89, -97, -100, 86, -76, 3, 39, -53, -61]
[-100, -97, -80, -76, -61, -53, 3, 39, 86, 89]
0.0017693000000000014
0.012734800000000004
0.3135392

Вывод:
С оптимизацией программа, в зависимости от исходных данных, работает быстрее
"""