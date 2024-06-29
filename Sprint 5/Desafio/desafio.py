import boto3

def desafio_sprint(evento):
    
    client_s3 = boto3.client('s3')

    bucket_desafio = 'wendel-desafio-bucket'
    arquivo_csv = '4-intern-hosp-2023.csv'

    query = """
    SELECT 
    COUNT(Mes) as qtd_mes,
    SUM(CASE WHEN CAST(Quantitativo AS INT) < 300 THEN 1 ELSE 0 END) as soma_quantitativo_menores_300,
    UTCNOW()
    FROM S3Object
    WHERE CAST(Quantitativo AS INT) >= 250 AND Mes <> 'Janeiro' AND CHAR_LENGTH(Mes) > 4
    """

    print("Executando a consulta no S3")

    resposta = client_s3.select_object_content(
        Bucket=bucket_desafio,
        Key=arquivo_csv,
        ExpressionType='SQL',
        Expression=query,
        InputSerialization={'CSV': {"FileHeaderInfo": "USE", "FieldDelimiter": ";"}},
        OutputSerialization={'CSV': {}}
    )

    for evento in resposta['Payload']:
        if 'Records' in evento:
            records = evento['Records']['Payload'].decode('utf-8').splitlines()
            for record in records:
                print(record)

if __name__ == "__main__":
    fake_event = {}  # testando o código
    resposta = desafio_sprint(fake_event)