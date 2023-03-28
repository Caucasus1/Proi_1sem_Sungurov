# чтение данных из файла
with open('text18-28.txt') as f:
    text = f.read()

print(f'Количество символов в тексте: {len(text)}')


# формирование текста в стихотворной форме
n = int(input('Введите номер строки: '))
phrase = input('Введите произвольную фразу: ')

lines = text.split('\n')
if n < 1 or n > len(lines):
    print('Неверный номер строки')
else:
    lines[n-1] += ' ' + phrase

poem = '\n'.join([f'{i+1}. {line}' for i, line in enumerate(lines)])
print(poem)


# запись текста в файл
with open('poem.txt', 'w') as f:
    f.write(poem)
