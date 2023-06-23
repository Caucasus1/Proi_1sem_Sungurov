class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

# Создание объекта класса Counter
counter = Counter()

# Вывод текущего значения счетчика
print(counter.value)
# Инкремент значения счетчика
counter.increment()

# Вывод обновленного значения счетчика
print(counter.value)

# Декремент значения счетчика
counter.decrement()

# Вывод окончательного значения счетчика
print(counter.value)  
