import json

caminho_arquivo = "person.json"

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        
        conteudo_json = json.load(arquivo)
        print(conteudo_json)

ler_arquivo_json(caminho_arquivo)