import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import upper,lower,explode,explode_outer,current_timestamp,col,udf
from pyspark.sql.types import DecimalType,IntegerType,StringType,StructType,StructField
from pyspark.sql.functions import col,column,concat,count,count_distinct,countDistinct,explode,explode_outer,\
lower,lpad,ltrim,rtrim,rpad,split,size,trim,udf,upper,lit


spark = SparkSession.builder.appName('sample').getOrCreate()
path = r"D:\datalake\ingestion\pyspark\files\EMPLOYEES.CSV"
df = spark.read.csv(path,header=True)
#df = spark.read.csv(path,header=True,inferSchema=True)
print(df.show())