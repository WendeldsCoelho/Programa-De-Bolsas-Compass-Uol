# Explicação

### Para resolver o desafio:
- Criei dois jobs no AWS Glue, para os arquivos CSV e JSON.
- Com esses scripts eu modifiquei a formato dos arquivos para parquet e também filtrei dados dos arquivos presentes no CSV.
- Depois de executar ambos os jobs com sucesso, verifiquei a camada TRUSTRED preenchida pelos dados.
- Por fim, criei tabelas no AWS Athena para verificar por meio de consultas a estrutura dos dados de filmes e series. 


# PRINTS

### JOB CSV

![job csv](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/Job_csv.jpeg)

### JOB JSON

![job json](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/Job_json.jpeg)

### PASTA MOVIES CSV

![movies](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/bucket_movies_csv.jpeg)

### PASTA MOVIES JSON

![movies](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/bucket_movies_json.jpeg)

### PASTA SERIES CSV

![series](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/bucket_series_csv.jpeg)

### PASTA SERIES JSON

![series](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/bucket_series_json.jpeg)






### As perguntas do desafio permaneceram.

- Quais são os diretores que mais dirigiram filmes de ação e aventura?(2010-2020)
- Maiores notas médias de ator/atriz principal por séries (2010-2020)

