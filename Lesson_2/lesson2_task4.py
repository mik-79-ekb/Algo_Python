"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

def sum_els(quantity, sum_el=0.0, start=1.0):
    while True:
        if quantity:
            quantity -= 1
            sum_el += start
            start /= -2
            continue
        return sum_el

num = int(input("Введите количество элементов: "))
print(f"Количество элементов - {num}, их сумма - {sum_els(num)}")