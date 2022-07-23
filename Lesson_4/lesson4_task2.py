"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее
простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

import timeit
import cProfile


def i_prime_num(i_num):
    """Без решета"""
    lst = [2]
    i = 1

    while len(lst) < i_num:
        i += 2
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)

    return lst[-1]


def eratosfen(i):
    """Используя алгоритм «Решето Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]


I_NUM = int(input("Порядковый номер простого числа: "))


def functions():
    i_prime_num(I_NUM)
    eratosfen(I_NUM)


cProfile.run('functions()')
print(timeit.timeit("i_prime_num(I_NUM)",
                    setup="from __main__ import i_prime_num, I_NUM", number=100))
print(timeit.timeit("eratosfen(I_NUM)",
                    setup="from __main__ import eratosfen, I_NUM", number=100))


"""
При I_NUM = 10 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson4_task2.py:16(i_prime_num)
        1    0.005    0.005    0.006    0.006 lesson4_task2.py:37(eratosfen)
        1    0.001    0.001    0.001    0.001 lesson4_task2.py:41(<listcomp>)
        1    0.001    0.001    0.001    0.001 lesson4_task2.py:50(<listcomp>)
        1    0.000    0.000    0.006    0.006 lesson4_task2.py:56(functions)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
       15    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.0009184999999991561
0.5714102000000008

При I_NUM = 100
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson4_task2.py:16(i_prime_num)
        1    0.005    0.005    0.006    0.006 lesson4_task2.py:37(eratosfen)
        1    0.001    0.001    0.001    0.001 lesson4_task2.py:41(<listcomp>)
        1    0.001    0.001    0.001    0.001 lesson4_task2.py:50(<listcomp>)
        1    0.000    0.000    0.006    0.006 lesson4_task2.py:56(functions)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
      271    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.027055400000000063
0.5613418000000001

При I_NUM = 1000
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
        1    0.007    0.007    0.008    0.008 lesson4_task2.py:16(i_prime_num)
        1    0.005    0.005    0.007    0.007 lesson4_task2.py:37(eratosfen)
        1    0.001    0.001    0.001    0.001 lesson4_task2.py:41(<listcomp>)
        1    0.001    0.001    0.001    0.001 lesson4_task2.py:50(<listcomp>)
        1    0.000    0.000    0.015    0.015 lesson4_task2.py:56(functions)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
     3960    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.7013093000000001
0.7046006
Решето было взято из примеров к уроку, его эффективность была замечена при входных данных от 1000
и более соответсвенно оно наиболее эффективно при больших числах
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))
"""