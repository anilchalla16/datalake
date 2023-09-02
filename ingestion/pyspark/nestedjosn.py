from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Create a SparkSession (if not already created)
spark = SparkSession.builder.appName("CreateSchema").getOrCreate()

path = r"D:\datalake\data\source_data\nestedjsonfile.json"

# Define the schema using StructType and StructField
nameschema = StructType([
    StructField("firstname", StringType(), True),
    StructField("lastname",StringType(), True)
])
schema = StructType([
    StructField("sno", IntegerType(), True),  # True indicates the column can contain NULL values
    StructField("name", nameschema),
    StructField("Btech", StringType(), True)
])

df = spark.read.json(path,schema=schema,multiLine=True)
df.show()
df.printSchema()

df.select(df.name.firstname,df.name.lastname).show()
