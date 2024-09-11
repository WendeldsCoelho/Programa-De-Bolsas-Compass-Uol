import hashlib

while True:
    entrada_string = input("Digite uma string para gerar o seu hash SHA-1 ou digite 'exit' para finalizar: ")

    if entrada_string.lower() == 'exit':
        break

    hash_bin = hashlib.sha1(entrada_string.encode())

    print("O hash por meio do algoritmo SHA-1 da string é: ", hash_bin.hexdigest())
