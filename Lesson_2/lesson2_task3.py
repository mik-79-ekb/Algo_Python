"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

def inverse_num(num, num_reverse=''):
    while True:
        if num:
            num_reverse += str(num % 10)
            num //= 10
            continue
        return int(num_reverse)

num = int(input("Введите число, которое требуется перевернуть: "))
inverse_num(num)
print(f"Перевернутое число: {inverse_num(num)}")