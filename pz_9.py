def program():
  dic ={"Читать": "Read",
        "Сказать": "tell",
        "Машина": "Car",
        "База": "Base",
        "Учитель": "Teacher",
        "Монитор": "Monitor",
        "Страна": "Country",
        "Самолет": "Airplane",
        "Сети": "Web",
        "Телефон": "Phone"}
  a = str(input())
  if a not in dic:
        print("Неверное значение")
        program()
  else:
        print(dic[a])
program()                      
