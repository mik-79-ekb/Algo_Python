"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

letter1 = input('Введите первую букву (латинский алфавит): ')
letter2 = input('Введите вторую букву (латинский алфавит): ')

letter1 = letter1.lower()
letter2 = letter2.lower()

num1 = ord(letter1) - ord('a') + 1
num2 = ord(letter2) - ord('a') + 1
delta = abs(ord(letter1) - ord(letter2)) - 1

print(f'{letter1} - это {num1} буква алфавита')
print(f'{letter2} - это {num2} буква алфавита')
print(f'Количество букв между {letter1} и {letter2} равно {delta}')