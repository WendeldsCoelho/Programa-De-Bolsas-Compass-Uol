#Script utilizado no AWS Glue:

import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper, col
from pyspark.sql.types import IntegerType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Nome do bucket e caminho do arquivo
bucket_name = "awsglue-ex-w" 
file_key = "nomes.csv"  
input_path = f"s3://{bucket_name}/{file_key}"

# Lendo o arquivo CSV 
dfRead = spark.read.option("header", "true").csv(input_path)

# Conversão da coluna 'total' para o tipo Integer
dfRead = dfRead.withColumn("total", col("total").cast(IntegerType()))

# Imprimindo o schema do dataframe
dfRead.printSchema()

# Alterando a caixa dos valores da coluna nome para MAIÚSCULO
df_Maiusculo = dfRead.withColumn("nome", upper(col("nome")))

# Contagem e impressão de linhas presentes no dataframe
df_Cont = df_Maiusculo.count()
print(f"Total de linhas no dataframe: {df_Cont}")

# Contagem de nomes agrupando por ano e sexo
df_group = df_Maiusculo.groupBy("ano", "sexo").count()

# Ordenação por ano de forma decrescente
df_group_sorted = df_group.orderBy(col("ano").desc())

# Nome feminino com mais registros e ano correspondente
df_feminino = df_Maiusculo.filter(col("sexo") == "F")
df_feminino_group = df_feminino.groupBy("nome", "ano").sum("total")
df_feminino_max = df_feminino_group.orderBy(col("sum(total)").desc()).first()
print(f"Nome feminino com mais registros: {df_feminino_max['nome']} no ano {df_feminino_max['ano']}")

# Nome masculino com mais registros e ano correspondente
df_masculino = df_Maiusculo.filter(col("sexo") == "M")
df_masculino_group = df_masculino.groupBy("nome", "ano").sum("total")
df_masculino_max = df_masculino_group.orderBy(col("sum(total)").desc()).first()
print(f"Nome masculino com mais registros: {df_masculino_max['nome']} no ano {df_masculino_max['ano']}")

# Total de registros para cada ano
df_total_ano = df_Maiusculo.groupBy("ano").sum("total").orderBy("ano").limit(10)
df_total_ano.show()

# Escrever o conteúdo no S3 em formato JSON
output_path = f"s3://{bucket_name}/lab-glue/frequencia_registro_nomes_eua"
df_Maiusculo.write.mode("overwrite").partitionBy("sexo", "ano").json(output_path)

# Finalizando o job
job.commit()