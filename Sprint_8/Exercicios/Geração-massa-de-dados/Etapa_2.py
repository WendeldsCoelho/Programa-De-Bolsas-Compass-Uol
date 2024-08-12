lista_animais = ["Golfinho", "Falcão", "Gorila", "Jaguar", "Lobo",
    "Urso", "Raposa", "Elefante", "Cervo", "Tubarão",
    "Tucano", "Pato", "Lontra", "Javali", "Antílope",
    "Tartaruga", "Baleia", "Pinguim", "Flamingo", "Hiena"]

lista_animais.sort()

[print(animal) for animal in lista_animais]

with open('animais.csv', 'w', encoding='utf-8') as arquivo:
    [arquivo.write(f"{animal}\n") for animal in lista_animais]