palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 
def is_Palindromo(palavra):
    return palavra == palavra[::-1]
    
for palavra in palavras:
    if is_Palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")