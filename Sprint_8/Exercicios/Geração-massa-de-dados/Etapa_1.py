import random 

lista_aleatoria = []

for _ in range(250):
    lista_aleatoria.append(random.randint(0,2500))

lista_aleatoria.reverse()

print(lista_aleatoria)