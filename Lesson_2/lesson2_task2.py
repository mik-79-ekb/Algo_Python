"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def even_odd_num(num, even=0, odd=0):
    while True:
        if num:
            num_modulo = num % 10
            num //= 10
            if num_modulo % 2 == 0:
                even += 1
            else:
                odd += 1
            continue
        return even, odd

num = int(input("Введите число: "))
even_odd_num(num)
print (f'Число {num} состоит из {even_odd_num(num)[0]} четных и {even_odd_num(num)[1]} нечетных чисел')
