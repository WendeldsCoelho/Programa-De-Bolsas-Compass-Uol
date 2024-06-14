import csv

def processar_arquivo(arquivo):
    
    estudantes = []
    
    with open(arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        
        for row in leitor:
            nome = row[0]
            notas = list(map(int, row[1:]))
            
            top_tres_notas = sorted(notas, reverse=True)[:3]
        
            media_maiores_notas = round(sum(top_tres_notas)/3, 2)
        
            estudantes.append((nome, top_tres_notas, media_maiores_notas))
        
    ordenar_estudantes = sorted(estudantes, key=lambda x: x[0])    
        
    for estudante in ordenar_estudantes:    
        nome, top_notas, media = estudante 
        print(f"Nome: {nome} Notas: {top_notas} Média: {media}")
        
processar_arquivo('estudantes.csv')