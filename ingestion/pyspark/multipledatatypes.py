from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType,ArrayType,MapType

# Create a SparkSession (if not already created)
spark = SparkSession.builder.appName("CreateSchema").getOrCreate()

path = r"D:\datalake\data\source_data\multipledatatypes.json"

# Define the schema using StructType and StructField
schema = StructType([  # True indicates the column can contain NULL values
    StructField("name", MapType(StringType(),StringType()), True)
])

df = spark.read.json(path,schema=schema)
df = df.select(df.name["firstname"],df.name.lastname)
df.show(truncate=False)
df.printSchema()