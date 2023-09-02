from fastparquet import ParquetFile
import pandas as pd
pf = ParquetFile(r'D:\datalake\ingestion\conversations\targetfiles\sample_1.parquet')
df = pf.to_pandas()
print(df)
df.to_csv(r'D:\datalake\ingestion\conversations\targetfiles\testing.csv',index = False)
print('************')