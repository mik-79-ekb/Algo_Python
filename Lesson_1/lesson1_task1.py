"""
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака
"""

number_1 = 5
number_2 = 6

print(
    f"Побитовые операции над числами {number_1} = {bin(number_1)} и {number_2} = {bin(number_2)}: \n\n"
    f"Побитовое 'ИЛИ': {number_1 | number_2} = {bin(number_1 | number_2)} \n"
    f"Побитовое, исключающее 'ИЛИ': {number_1 ^ number_2} = {bin(number_1 ^ number_2)} \n"
    f"Побитовое 'И': {number_1 & number_2} = {bin(number_1 & number_2)} \n"
    f"Битовый сдвиг влево числа {number_1} на 2 знака: {number_1 << 2} = {bin(number_1 << 2)} \n"
    f"Битовый сдвиг вправо числа {number_1} на 2 знака: {number_1 >> 2} = {bin(number_1 >> 2)} \n")