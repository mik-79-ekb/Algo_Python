"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

from random import randint
MASSIVE = [randint(-100, 100) for elem in range(randint(5, 20))]
NEGATIVE_ELS = [el for el in MASSIVE if el < 0]
MAX_MIN = NEGATIVE_ELS[0]
MAX_MIN_INDEX = 0
for x in range(len(MASSIVE)):
    if MASSIVE[x] < 0 and MASSIVE[x] > MAX_MIN:
       MAX_MIN = MASSIVE[x]
       MAX_MIN_INDEX = x

print(MASSIVE)
print(f"В данном массиве чисел максимальный отрицательный элемент {MAX_MIN} "
      f"стоит на {MAX_MIN_INDEX + 1} позиции")