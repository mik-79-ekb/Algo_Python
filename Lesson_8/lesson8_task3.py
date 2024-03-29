"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

from collections import deque
from random import randint

# функция генерации графа по количеству вершин
def gen_grath(n):
    g = []
    for x in range(n):
        g.append([randint(0, 1) for y in range(n)])
    return g

# на вход подаётся граф в виде таблицы смежности
def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:

        current = deq.pop()

        if current == finish:
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'Кратчайший путь {list(way)} длинною в {cost} условных единиц'

n = int(input('Введите количество вершин графа: '))
g = gen_grath(n)
print('Сгенерированный граф:')
print(*g, sep='\n')
s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(bfs(g, s, f))