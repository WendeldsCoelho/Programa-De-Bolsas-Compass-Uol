# importar bibliotecas necessárias
import os
import boto3
from datetime import datetime
from dotenv import load_dotenv

# Carregar as chaves da AWS
load_dotenv('.env')

# Configurações
bucket_name = 'desafio-sprint6-w'
storage_layer = 'Raw'
data_origin = 'Local'
data_format = 'CSV'

# Caminhos para os arquivos csv
movies_file_path = '/app/data/movies.csv' 
series_file_path = '/app/data/series.csv' 

# Função para o upload de um arquivo para o S3
def upload_s3(file_path, data_specification):
    # Criação de um cliene S3 utilizando as credencias AWS
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
        region_name=os.getenv('AWS_DEFAULT_REGION')                 
                             )
    # Obter o nome do arquivo
    nome_Arquivo = os.path.basename(file_path)

    # Obter a data atual no formata requisitado
    current_date = datetime.now().strftime('%Y/%m/%d')

    # Criação do caminho no bucket
    s3_key = f"{storage_layer}/{data_origin}/{data_format}/{data_specification}/{current_date}/{nome_Arquivo}"

    # Upload do arquivo com tratamento de exceção
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"Upload bem-sucedido de {file_path} para s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Erro ao fazer upload de {file_path}: {e}")

# Função para executar os uploads
def main():
    upload_s3(movies_file_path, 'Movies')
    upload_s3(series_file_path, 'Series')

if __name__ == "__main__":
    main()
