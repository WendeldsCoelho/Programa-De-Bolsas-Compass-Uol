def maiores_que_media(conteudo:dict)->list:
    
    media_preco = sum(conteudo.values())/ len(conteudo)
    
    produtos_acima_media = [(produto,preco) for produto, preco in conteudo.items() if preco > media_preco]
    
    produtos_acima_media_cresc = sorted(produtos_acima_media, key= lambda x: x[1])
    
    return  produtos_acima_media_cresc
    
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))
    