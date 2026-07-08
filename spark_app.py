from pyspark.sql import SparkSession

spark = SparkSession.builder \
     .appName("taxi_etl") \
     .getOrCreate()

df = spark.read.parquet("data/yellow.parquet")

df.show(5)
df.printSchema()
print(df.count())

