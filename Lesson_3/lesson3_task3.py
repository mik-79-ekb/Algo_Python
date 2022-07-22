"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

from random import randint
MASSIVE = [randint(0, 100) for el in range(randint(5, 20))]
MIN_INDEX = 0
MAX_INDEX = 0
for x in range(len(MASSIVE)):
    if MASSIVE[x] < MASSIVE[MIN_INDEX]:
        MIN_INDEX = x
    if MASSIVE[x] > MASSIVE[MAX_INDEX]:
        MAX_INDEX = x
print(
    f"В данном массиве чисел максимальное число {MASSIVE[MAX_INDEX]} стоит на {MAX_INDEX + 1}"
    f" позиции, а минимальное число {MASSIVE[MIN_INDEX]} стоит на {MIN_INDEX + 1} позиции "
    f"\nЗаменяем их\n", MASSIVE)
MASSIVE[MAX_INDEX], MASSIVE[MIN_INDEX] = MASSIVE[MIN_INDEX], MASSIVE[MAX_INDEX]
print(f' {MASSIVE}')