import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, lit

# Configurações do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_TRUSTED_PATH_JSON_MOVIES', 'S3_TRUSTED_PATH_JSON_SERIES', 'S3_TRUSTED_PATH_CSV_MOVIES', 'S3_REFINED_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
trusted_path_json_movies = args['S3_TRUSTED_PATH_JSON_MOVIES']
trusted_path_json_series = args['S3_TRUSTED_PATH_JSON_SERIES']
trusted_path_csv_movies = args['S3_TRUSTED_PATH_CSV_MOVIES']
refined_path = args['S3_REFINED_PATH']

# Dados da camada Trusted (JSON)
json_movies_df = spark.read.option("multiline", "true").parquet(trusted_path_json_movies)
json_series_df = spark.read.option("multiline", "true").parquet(trusted_path_json_series)

# Dados da camada Trusted (CSV)
csv_movies_df = spark.read.option("header", "true").parquet(trusted_path_csv_movies)

# Seleção das colunas para filmes e séries
json_movies_df = json_movies_df.select(
    col("id"),
    col("title"),
    col("release_date"),
    col("original_language"),
    col("overview"),
    col("popularity"),
    col("vote_average"),
    col("vote_count"),
    col("main_actor"),
    col("director")
)

json_series_df = json_series_df.select(
    col("id"),
    col("name").alias("title"),
    col("first_air_date").alias("release_date"),
    col("original_language"),
    col("overview"),
    col("popularity"),
    col("vote_average"),
    col("vote_count"),
    col("main_actor"),
    lit(None).alias("director"),  # Coluna 'director' não existe em séries JSON
    lit(None).alias("tempo_minutos")  # Adicionando a coluna 'tempo_minutos' para séries
)

# Filtro para filmes e séries com vote_count > 0
json_movies_df = json_movies_df.filter(col("vote_count") > 0)
json_series_df = json_series_df.filter(col("vote_count") > 0)

# Adicionar tempo_minutos ao conjunto de dados de filmes JSON
csv_movies_df = csv_movies_df.select(
    col("tituloPincipal").alias("csv_title"),  # Renomeando para evitar conflito
    col("tempoMinutos").alias("tempo_minutos")
)

# left join entre o DataFrame JSON de filmes e o DataFrame CSV para adicionar tempo_minutos
json_movies_with_time_df = json_movies_df.join(
    csv_movies_df,
    json_movies_df["title"] == csv_movies_df["csv_title"],
    "left"
).drop("csv_title")  # Removendo a coluna renomeada após o join

# Garantir que a coluna 'tempo_minutos' em filmes (mesmo que seja null)
json_movies_with_time_df = json_movies_with_time_df.withColumn("tempo_minutos", col("tempo_minutos"))

# Unir filmes (com tempo_minutos) e séries em um único DataFrame
combined_df = json_movies_with_time_df.withColumn("categoria", lit("Filme")).unionByName(
    json_series_df.withColumn("categoria", lit("Série")),
    allowMissingColumns=True  # Permitir que colunas ausentes sejam preenchidas com null
)

# Criando a Dimensão Obra
dim_obra = combined_df.select(
    col("id").alias("obra_id"),
    col("title").alias("titulo"),
    col("release_date").alias("data_lancamento"),
    col("original_language").alias("idioma_original"),
    col("overview"),
    col("popularity"),
    col("categoria"),
    col("tempo_minutos")
).distinct()

# Criando a Dimensão Pessoa
dim_pessoa_actors = combined_df.select(
    col("id").alias("obra_id"),
    col("main_actor").alias("nome"),
    lit("Ator").alias("tipo_participacao")
).distinct()

dim_pessoa_directors = combined_df.select(
    col("id").alias("obra_id"),
    col("director").alias("nome"),
    lit("Diretor").alias("tipo_participacao")
).distinct()

dim_pessoa = dim_pessoa_actors.unionByName(dim_pessoa_directors).distinct()

# Criando a Tabela Fato Avaliação
fato_avaliacao = combined_df.select(
    col("id").alias("obra_id"),
    col("vote_average").alias("media_avaliacao"),
    col("vote_count").alias("total_votos")
).distinct()

# Salvando as pastas na camada Refined
dim_obra.write.mode("overwrite").format("parquet").save(f"{refined_path}/dim_obra")
dim_pessoa.write.mode("overwrite").format("parquet").save(f"{refined_path}/dim_pessoa")
fato_avaliacao.write.mode("overwrite").format("parquet").save(f"{refined_path}/fato_avaliacao")

# Finalizando o Job
job.commit()