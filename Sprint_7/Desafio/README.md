# Explicação 

### Para resolver o desafio:
- Criei duas layers contendo o boto3.zip e a outra request-dotoenv.
- Criei a função e adicionei as duas layers criadas anteriormente.
- Inseri em variáveis de ambiente a chave do TMDB que eu adquiri.
- Concedi a permissão através do IAM para a função conseguir enviar os dados para o S3.
- Estruturei os códigos movies.py e tv_shows.py para buscar e filtrar os dados da API
- Configurei o lambda_function para salvar no s3 os dados obtidos pelas duas classes citadas acima.


# PRINTS

### Caminho do arquivo s3

![arquivo](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_7/Evid%C3%AAncias/desafio/caminho-arquivo-s3.jpeg)

### Função lambda

![lambda](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_7/Evid%C3%AAncias/desafio/funcao-lambda.jpeg)

### Json series

![json](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_7/Evid%C3%AAncias/desafio/json-series-s3.jpeg)

### Obs:.. modifiquei as perguntas do desafio reduzindo o espaço tempo para 2010-2020.

- Quais são os diretores que mais dirigiram filmes de ação e aventura?(2010-2020)
- Maiores notas médias de ator/atriz principal por séries (2010-2020)


