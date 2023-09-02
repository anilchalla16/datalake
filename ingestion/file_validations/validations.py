import pandas as pd

file_headers = "sno,name,place,salary"
len_headers = 4

path = r"D:\datalake\ingestion\file_validations\src_files\sample.csv"
with open(path,"r") as files:
    for file in files:
        if file == file_headers:
            print("headers matches")
        else:
            print("headers not matches")

with open(path,"r") as files:
    dele_count = files.readlines()
    print(dele_count)
