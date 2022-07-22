"""
Определить, какое число в массиве встречается чаще всего
"""

from random import randint
MASSIVE = [randint(0, 10) for el in range(randint(20, 30))]
from collections import Counter
print(f"В массиве {MASSIVE} \nчисло {Counter(MASSIVE).most_common()[0][0]}"
      f" встречается чаще всего")