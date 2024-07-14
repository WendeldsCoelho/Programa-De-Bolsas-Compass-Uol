# Use a imagem base do Python
FROM python:3.9-slim

# Diretório utilizado  dentro do container
WORKDIR /app

# Copia os arquivos locais para o diretório de trabalho no container
COPY . /app

# Instalar aplicações necessárias
RUN pip install boto3

RUN pip install python-dotenv


# Comando para executar o script Python
CMD ["python", "Desafio.py"]
