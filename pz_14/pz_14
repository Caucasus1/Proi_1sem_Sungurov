import re
from datetime import datetime

# Чтение исходного файла
with open('dates.txt', 'r') as file:
    text = file.read()

# Поиск дат в формате ДД.ММ.ГГГГ и ДД/ММ/ГГГГ
pattern1 = r'\b\d{2}\.\d{2}\.\d{4}\b'
pattern2 = r'\b\d{2}/\d{2}/\d{4}\b'
dates1 = re.findall(pattern1, text)
dates2 = re.findall(pattern2, text)

# Подсчет количества дат в каждом формате
count1 = len(dates1)
count2 = len(dates2)

# Найти даты февраля в формате ДД/ММ/ГГГГ
february_dates = []
for date in dates2:
    try:
        parsed_date = datetime.strptime(date, '%d/%m/%Y')
        if parsed_date.month == 2:
            february_dates.append(date)
    except ValueError:
        pass

# Запись дат февраля в формате ДД/ММ/ГГГГ в новый файл
with open('february_dates.txt', 'w') as file:
    file.write('\n'.join(february_dates))

# Вывод результатов
print(f"Количество дат в формате ДД.ММ.ГГГГ: {count1}")
print(f"Количество дат в формате ДД/ММ/ГГГГ: {count2}")
print("Даты февраля в формате ДД/ММ/ГГГГ сохранены в файл 'february_dates.txt'.")
