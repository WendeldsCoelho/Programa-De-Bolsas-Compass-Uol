# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos locais para o diretório de trabalho no container
COPY . /app

# Instala as dependências
RUN pip install boto3

RUN pip install python-dotenv


# Define o comando padrão para executar o script Python
CMD ["python", "Desafio.py"]
