"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

def num_of_multiples(multiples, before):
    nums = [num for num in range(2, 100) if num % multiples == 0]
    print(f"В диапазоне 2-99: {len(nums)} чисел кратны {multiples}",
          f"Это числа: {nums}", sep="\n", end="\n\n")
    if multiples < 10:
        return num_of_multiples(multiples + 1, before)

num_of_multiples(2, 9)