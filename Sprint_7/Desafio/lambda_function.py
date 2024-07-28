import boto3
import json
from datetime import datetime
from movies import fetch_action_adventure_movies
from tv_shows import fetch_action_adventure_tv_shows

s3_client = boto3.client('s3')

# Função para converter objetos para dicionários
def convert_to_dict(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    
# Função para salvar JSON no S3
def save_json_s3(data, media_type, index):
    current_date = datetime.now().strftime('%Y-%m-%d')
    year, month, day = current_date.split('-')
    
    # Definindo o caminho da forma especificada
    storage_layer = "Raw"
    data_source = "TMDB"
    data_format = "JSON"
    file_name = f"{media_type}data_{index}_{len(data)}.json"  

    s3_key = f"{storage_layer}/{data_source}/{data_format}/{year}/{month}/{day}/{file_name}"
    bucket_name = 'desafio-sprint6-w'

    try:
        s3_client.put_object(
            Body=json.dumps(data, ensure_ascii=False, indent=4, default=convert_to_dict),
            Bucket=bucket_name,
            Key=s3_key
        )
        print(f"Dados salvos em s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Erro ao salvar dados no S3: {e}")

# Função principal para execução local
def lambda_handler(event, context):
    index = 0
    # Busca os dados de filmes de ação e aventura
    for data in fetch_action_adventure_movies():
        if data:  # Verifica se está vazia antes de salvar
            save_json_s3(data, 'action_adventure_movies', index)
            index += 1

    # Busca os dados de séries de ação e aventura
    for data in fetch_action_adventure_tv_shows():
        if data: # Verifica se está vazia antes de salvar
            save_json_s3(data, 'action_adventure_tv_shows', index)
            index += 1

if __name__ == "__main__":
    lambda_handler(None, None)