# Explicação

### Para resolver o desafio:
- Criei um job no AWS Glue para a camada refined.
- Com esse script eu agrupei os dados da camada trusted, seguindo os princípios de modelagem multidimensional.
- Depois de executar  o job com sucesso, verifiquei a camada REFINED preenchida pelos dados no s3.
- Por fim, criei tabelas no AWS Athena para verificar por meio de consultas a estrutura dos dados. 


# PRINTS

### JOB REFINED

![job refined](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_9/Evid%C3%AAncias/Desafio/job_refined.jpeg)

### RUN JOB REFINED

![job refined](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_9/Evid%C3%AAncias/Desafio/run_job_refined.jpeg)

### S3 CAMADA REFINED

![s3 refined](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_9/Evid%C3%AAncias/Desafio/camada_refined_s3.jpeg)

### MODELO MULTIDIMENSIONAL 

![multidimensional](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_9/Evid%C3%AAncias/Desafio/sprint9_modelo_multidimensional.jpeg)


# Consultas e seus respectivos resultados no AWS Athena para teste dos arquivos.

### Quais são os diretores que mais dirigiram filmes de ação e aventura com media_avaliacao > 7

![result1](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_9/Evid%C3%AAncias/Desafio/teste_athena_pergunta1.jpeg)

###  Maiores notas médias de ator/atriz principal por séries com pelo menos duas séries atuadas

[result2](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/Sprint_9/Evid%C3%AAncias/Desafio/teste_athena_pergunta2.jpeg)

### As perguntas do desafio permaneceram.

- Quais são os diretores que mais dirigiram filmes de ação e aventura?(2010-2020)
- Maiores notas médias de ator/atriz principal por séries (2010-2020)

