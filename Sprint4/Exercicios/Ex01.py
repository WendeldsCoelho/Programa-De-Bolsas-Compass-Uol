with open('number.txt', 'r') as arquivo:
    
    numeros = list(map(int, arquivo.readlines()))

lista_par = list(filter(lambda x: x % 2 == 0, numeros))

pares_decresc = sorted(lista_par, reverse = True)

top_5_pares = pares_decresc[:5]

soma_pares = sum(top_5_pares)

print(top_5_pares)

print(soma_pares)