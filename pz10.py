Magistr = {
    "name": "magistr",
    "asort": {"лермонтов","достоевский","пушкин","тютчев"},
}
HouseofBook = {
    "name": "HouseofBook",
    "asort": {"Толстой","грибоедов","чехов","пушкин"},
}
Bookmarket = {
    "name": "bookmarket",
    "asort": {"Пушкин","достоевский","маяковский"},
}
Gallery = {
    "name": "gallery",
    "asort": {"Чехов","Тютчев","Пушкин"},
}
allShops = [Magistr,HouseofBook,Bookmarket,Gallery]
findPushkinAndTyutchev = []

fullList = Magistr["asort"] | HouseofBook["asort"] | Bookmarket["asort"] | Gallery["asort"]

for shop in allShops:
  if "Пушкин" in shop["asort"] and "Тютчев" in shop["asort"]:
   findPushkinAndTyutchev.append(shop["name"])

print(f"Полный список товаров: {fullList}\n В этих магазинах можно купить Пушкина и Тютчева: {findPushkinAndTyutchev}\n") 
