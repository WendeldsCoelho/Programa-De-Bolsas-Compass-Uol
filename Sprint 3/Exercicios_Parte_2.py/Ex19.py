import random

random_list = random.sample(range(500), 50)

random_list_ordered = sorted(random_list)
n = len(random_list_ordered)
meio1 = random_list_ordered[(n//2) - 1]
meio2 = random_list_ordered[(n//2)]
mediana = (meio1+meio2)/2

media = (sum(random_list))/50

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")