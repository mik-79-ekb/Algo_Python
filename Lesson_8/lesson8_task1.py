"""
На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
"""

def handshakes(n):
    vertex = [i for i in range(1, n + 1)]  # вершины графа - люди с номерами от 1 до n включительно
    edge = []  # рёбра графа - уникальные урукопожатия

    for i in vertex:
        for j in range(i + 1, n + 1):
            edge.append((i, j))

    print(f'Количество рукопожатий: {len(edge)}')
    print(f'Пары друзей, пожавших друг другу руки: {edge}')


n = int(input('Веедите количество друзей: '))
handshakes(n)