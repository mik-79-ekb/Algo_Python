"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.
"""

num_year = int(input("Введите год: "))
if num_year % 400 == 0 or (num_year % 4 == 0 and num_year % 100 != 0):
    print("Год является високосным!")
else:
    print("Год не является високосным!")