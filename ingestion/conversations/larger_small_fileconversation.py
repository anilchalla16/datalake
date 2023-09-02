import pandas as pd

chunk_size = 5  # Number of rows per chunk
input_file = r'D:\datalake\ingestion\conversations\sourcefiles\EMPLOYEES.csv'
output_prefix = r"D:\datalake\ingestion\conversations\targetfiles\sample_"
chunk_number = 1

# Read the Parquet file into a pandas DataFrame
df = pd.read_csv(input_file)
print(df)

# Split the DataFrame into chunks and write each chunk to a separate file
for start in range(0, len(df), chunk_size):

    end = start + chunk_size
    chunk = df[start:end]

    output_file = f"{output_prefix}{chunk_number}.csv"
    chunk.to_csv(output_file, index=False)

    chunk_number += 1
