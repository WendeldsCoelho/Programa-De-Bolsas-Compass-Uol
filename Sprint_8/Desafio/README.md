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

# Consultas e seus respectivos resultados no AWS Athena para teste dos arquivos.

### Filmes csv

- SELECT DISTINCT titulopincipal, anolancamento, genero, notamedia FROM movies LIMIT 50;

![filmes csv](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/athena-result-movies-csv.jpeg)


### Series csv

- SELECT DISTINCT titulopincipal, anolancamento, genero, notamedia FROM series LIMIT 50;

![series csv](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/athena-result-series-csv.jpeg)

### Filmes json

- SELECT * FROM movies_450b144634bbf5b5c70a085634d252c3 LIMIT 15;

![filmes json](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/athena-result-movies-json.jpeg)

### Series json

- SELECT * FROM tv_shows LIMIT 15;

![series json](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_8/Evid%C3%AAncias/Desafio/athena-result-series-json.jpeg)








### As perguntas do desafio permaneceram.

- Quais são os diretores que mais dirigiram filmes de ação e aventura?(2010-2020)
- Maiores notas médias de ator/atriz principal por séries (2010-2020)

