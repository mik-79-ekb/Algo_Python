"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""

import timeit
import cProfile
from random import randint


# """
# Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Пример:
# Задайте количество строк в матрице: 3
# Задайте количество столбцов в матрице: 4
#  36 20 42 38
#  46 27  7 33
#  13 12 47 15
# [13, 12, 7, 15] минимальные значения по столбцам
# Максимальное среди них = 15
# """

# from random import randint


# def matrix(row, col, row_idx=0):
#     """Функция для построения матрицы
#         row - количество строк
#         col - количество колонок
#         row_idx - индекс новой строки
#     """
#     if not row:
#         for elem in MATRIX:
#             print(' ', *elem)
#
#         row_matrix = []
#         for idx in range(len(MATRIX[0])):
#             row_matrix.append([el_row for el in MATRIX for el_row in el if el.index(el_row) == idx])
#         min_in_row = [el_row for el in row_matrix for el_row in el if el_row == min(el)]
#         print(f"{min_in_row} "
#               f"минимальные значения по столбцам \nМаксимальное среди них: {max(min_in_row)}")
#         return
#     MATRIX.append([])
#     for elem in range(col):
#         MATRIX[row_idx].append(randint(10, 100))
#
#     return matrix(row - 1, col, row_idx + 1)
#
#
# MATRIX = []
# try:
#     ROW_MATRIX = int(input("Задайте количество строк в матрице: "))
#     COL_MATRIX = int(input("Задайте количество столбцов в матрице: "))
#
#     if not ROW_MATRIX or not COL_MATRIX:
#         raise ValueError
#
#     matrix(ROW_MATRIX, COL_MATRIX)
# except ValueError as exception:
#     print("Необходимо вводить положительное количество")

MATRIX = [[]]


def func1(col=5, row_idx=0):
    """O(n) – линейная сложность"""
    for elem in range(col):
        MATRIX[row_idx].append(randint(10, 100))


MATRIX = [[]]


def func2(col=5, row_idx=0):
    """O(n) – линейная сложность"""
    MATRIX[row_idx].append([randint(10, 100) for _ in range(col)])


ROW_MATRIX = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]


def func3(row_matrix):
    """O(n^2) – квадратичная сложность"""
    min_in_row = [el_row for el in row_matrix for el_row in el if el_row == min(el)]


def func4(row_matrix):
    """O(n^2) – квадратичная сложность"""
    min_in_row = []
    for el in row_matrix:
        for el_row in el:
            if el_row == min(el):
                min_in_row.append(el_row)


def functions():
    func1()
    func2()
    func3(ROW_MATRIX)
    func4(ROW_MATRIX)


functions()


cProfile.run('functions()')
print(timeit.timeit("func1()",
                    setup="from __main__ import func1",
                    number=1000))
print(timeit.timeit("func2()",
                    setup="from __main__ import func2",
                    number=1000))
print(timeit.timeit("func3(ROW_MATRIX)",
                    setup="from __main__ import func3, ROW_MATRIX",
                    number=1000))
print(timeit.timeit("func4(ROW_MATRIX)",
                    setup="from __main__ import func4, ROW_MATRIX",
                    number=1000))


"""
Результат:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:103(functions)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:72(func1)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:81(func2)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:83(<listcomp>)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:89(func3)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:91(<listcomp>)
        1    0.000    0.000    0.000    0.000 lesson4_task1.py:94(func4)
       10    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
       10    0.000    0.000    0.000    0.000 random.py:290(randrange)
       10    0.000    0.000    0.000    0.000 random.py:334(randint)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       42    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       16    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


0.00899720000000001
0.008294200000000002
0.008760400000000002
0.009136100000000008
1,2. Оптимизировал код, заменив цикл for на генератор работающий быстрее 
и заменив итерируемую переменную на мусорную (_)
3,4. Обратный пример из той же функции. В квадратичной функции заменил двойной генератор на
цикл и вложенный цикл, в итоге код стал работать медленнее.
"""