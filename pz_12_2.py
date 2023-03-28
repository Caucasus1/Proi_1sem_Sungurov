def lower_case(text):
    for letter in text:
        if letter.isupper():
            yield letter.lower()
        else:
            yield letter

my_text = "ThIs Is A tEsT"
for char in lower_case(my_text):
    print(char, end="")
