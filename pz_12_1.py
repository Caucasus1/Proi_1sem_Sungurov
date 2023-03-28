import random

sequence = []
for i in range(20):
    sequence.append(random.randint(1, 10))

unique_sequence = list(set(sequence))   # выбираем только уникальные элементы
count = len(unique_sequence)            # находим количество уникальных элементов

for i in range(len(unique_sequence)):
    if unique_sequence[i] > 5:
        unique_sequence[i] *= 2

print(unique_sequence)
print(count)
