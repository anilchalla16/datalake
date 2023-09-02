from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Create a SparkSession (if not already created)
spark = SparkSession.builder.appName("CreateSchema").getOrCreate()

path = r"D:\datalake\data\source_data\singlelinejson.json"

# Define the schema using StructType and StructField
schema = StructType([
    StructField("sno", IntegerType(), True),  # True indicates the column can contain NULL values
    StructField("name", StringType(), True),
    StructField("place", StringType(), True)
])

df = spark.read.json(path,schema=schema)
df.show()
