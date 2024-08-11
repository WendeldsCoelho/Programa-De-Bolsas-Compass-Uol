import sys
from datetime import datetime
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Configurações do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_SERIES', 'S3_OUTPUT_PATH_SERIES', 'S3_INPUT_PATH_MOVIES', 'S3_OUTPUT_PATH_MOVIES'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída via argumentos
input_path_series = args['S3_INPUT_PATH_SERIES']
output_path_series = args['S3_OUTPUT_PATH_SERIES']
input_path_movies = args['S3_INPUT_PATH_MOVIES']
output_path_movies = args['S3_OUTPUT_PATH_MOVIES']

# Inserindo a data de execução como particionamento
execution_date = datetime.now().strftime("dt=%Y/%m/%d")

# Definindo o esquema para JSON de séries
schema_series = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("first_air_date", StringType(), True),
    StructField("original_language", StringType(), True),
    StructField("overview", StringType(), True),
    StructField("popularity", FloatType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", IntegerType(), True),
    StructField("main_actor", StringType(), True)
])

#  Esquema para JSON de filmes
schema_movies = StructType([
    StructField("id", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("release_date", StringType(), True),
    StructField("original_language", StringType(), True),
    StructField("overview", StringType(), True),
    StructField("popularity", FloatType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", IntegerType(), True),
    StructField("main_actor", StringType(), True),
    StructField("director", StringType(), True)  # Opcional
])

# Leitura do conjunto de dados JSON de séries 
df_series = spark.read.option("multiline", "true").schema(schema_series).json(input_path_series)

# Gravação do conjunto de dados de séries em Parquet
df_series.write.mode("overwrite").format("parquet").save(f"{output_path_series}/{execution_date}")

# Leitura do conjunto de dados JSON de filmes com o esquema definido
df_movies = spark.read.option("multiline", "true").schema(schema_movies).json(input_path_movies)
# Gravação do conjunto de dados de filmes em Parquet, particionando pela data de execução
df_movies.write.mode("overwrite").format("parquet").save(f"{output_path_movies}/{execution_date}")

job.commit()