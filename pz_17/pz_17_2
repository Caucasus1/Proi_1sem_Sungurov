class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age


class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed


class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

# Создание объектов класса "Собака" и "Кошка"
dog = Dog("Собака", 3, "Лабрадор")
cat = Cat("Кошка", 5, "Британская")

# Вывод информации о животных
print(f"Собака: Вид - {dog.species}, Возраст - {dog.age}, Порода - {dog.breed}")
print(f"Кошка: Вид - {cat.species}, Возраст - {cat.age}, Порода - {cat.breed}")
