
from collections import Counter
colors = ['blue', 'blue', 'blue', 'red', 'red']
counter = Counter(colors)
print(counter)

counter['yellow'] += 2
print(counter)

Counter({'blue': 3, 'red': 2, 'yellow': 1})
print(counter.most_common()[0])
