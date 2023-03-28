# генерация файлов с последовательностями чисел
import random

with open('file1.txt', 'w') as f1:
    seq1 = [random.randint(-50, 50) for _ in range(20)]
    f1.write(' '.join(map(str, seq1)))

with open('file2.txt', 'w') as f2:
    seq2 = [random.randint(-50, 50) for _ in range(25)]
    f2.write(' '.join(map(str, seq2)))


# чтение данных из файлов
with open('file1.txt') as f1:
    seq1 = list(map(int, f1.read().split()))

with open('file2.txt') as f2:
    seq2 = list(map(int, f2.read().split()))


# обработка данных
average = (sum(seq1) + sum(seq2)) / (len(seq1) + len(seq2))
odd1 = len([x for x in seq1 if x % 2 != 0])
odd2 = len([x for x in seq2 if x % 2 != 0])
common = [x for x in seq1 if x in seq2]
common_count = len(common)


# запись результатов в файл
with open('result.txt', 'w') as f:
    f.write('Элементы первого файла:\n')
    f.write(' '.join(map(str, seq1)) + '\n\n')
    f.write('Элементы второго файла:\n')
    f.write(' '.join(map(str, seq2)) + '\n\n')
    f.write(f'Среднее арифметическое элементов обоих файлов: {average:.2f}\n\n')
    f.write(f'Количество нечетных элементов первого файла: {odd1}\n')
    f.write(f'Количество нечетных элементов второго файла: {odd2}\n\n')
    f.write('Элементы общие для двух файлов:\n')
    f.write(' '.join(map(str, common)) + '\n\n')
    f.write(f'Количество элементов, общих для двух файлов: {common_count}\n')
