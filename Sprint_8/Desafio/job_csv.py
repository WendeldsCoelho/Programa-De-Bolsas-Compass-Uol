import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

# Configurações do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_MOVIES', 'S3_INPUT_PATH_SERIES', 'S3_OUTPUT_PATH_MOVIES', 'S3_OUTPUT_PATH_SERIES'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída 
input_path_1 = args['S3_INPUT_PATH_MOVIES']
input_path_2 = args['S3_INPUT_PATH_SERIES']
output_path_1 = args['S3_OUTPUT_PATH_MOVIES']
output_path_2 = args['S3_OUTPUT_PATH_SERIES']

# Leitura dos dados com o delimitador |
df1 = spark.read.format("csv").option("header", "true").option("sep", "|").load(input_path_1)
df2 = spark.read.format("csv").option("header", "true").option("sep", "|").load(input_path_2)

# Aplicando os filtros necessários
df1 = df1.filter((col("anoLancamento") >= 2010) & (col("anoLancamento") <= 2020))
df1 = df1.filter(col("genero").rlike(r'\b(Action|Adventure)\b'))

df2 = df2.filter((col("anoLancamento") >= 2010) & (col("anoLancamento") <= 2020))
df2 = df2.filter(col("genero").rlike(r'\b(Action|Adventure)\b'))

# Gravação dos dados
df1.write.mode("overwrite").format("parquet").save(output_path_1)
df2.write.mode("overwrite").format("parquet").save(output_path_2)

# Finalizando o job
job.commit()