import boto3

# Função criada para execução do código pedido no desafio
def desafio_sprint(evento):
    
    # Cria um cliente S3 utilizando o boto3 para interagir com o S3
    client_s3 = boto3.client('s3')

    # Criação de variáveis para bucker e arquivo csv
    bucket_desafio = 'wendel-desafio-bucket'
    arquivo_csv = '4-intern-hosp-2023.csv'

    # query cumprindo todos os requisitos solicitados, abaixo a explicação do resultado.
    # 1.(COUNT(Mes) as qtd_mes) trará uma contagem dos meses com quantitativo maior que 250, diferente do mês de janeiro e com mais de 4 caracteres.
    # 2.(SUM(CASE WHEN CAST(Quantitativo AS INT) < 300 THEN 1 ELSE 0 END) as soma_quantitativo_menores_300) soma de quantos meses possuem quantitativo menor que 300 e são diferentes de janeiro
    # 3.(UTCNOW()) data e hora atuais em UTC.
    query = """
    SELECT 
    COUNT(Mes) as qtd_mes,
    SUM(CASE WHEN CAST(Quantitativo AS INT) < 300 THEN 1 ELSE 0 END) as soma_quantitativo_menores_300,
    UTCNOW()
    FROM S3Object
    WHERE CAST(Quantitativo AS INT) >= 250 AND Mes <> 'Janeiro' AND CHAR_LENGTH(Mes) > 4
    """

    print("Executando a consulta no S3")

    # Consulta sql no objeto S3
    resposta = client_s3.select_object_content(
        # nome do Bucket e arquivo criados anteriormente
        Bucket=bucket_desafio, 
        Key=arquivo_csv,
        ExpressionType='SQL',
        Expression=query,
        InputSerialization={'CSV': {"FileHeaderInfo": "USE", "FieldDelimiter": ";"}},
        OutputSerialization={'CSV': {}}
        # Acima especifico o arquivo de entrada com delimitador ';' e o arquivo de entrada também um csv
    )

    # iteração sobre os eventos na resposta
    for evento in resposta['Payload']:
        if 'Records' in evento:
            # Decodifição e formatação das respostas de forma apropriada
            records = evento['Records']['Payload'].decode('utf-8').splitlines()
            for record in records:
                # Reprodução do resultado
                print(record)

# Main e evento falso para executar diretamente a função
if __name__ == "__main__":
    fake_event = {}  # testando o código
    resposta = desafio_sprint(fake_event)
