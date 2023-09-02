

source_file_path = "D:\datalake\ingestion\pythonnotes\sourcefiles\EMPLOYEES.csv"

with open(source_file_path,"r") as files:
    for file_data in files:
        print(type(file_data))

file = open(source_file_path,"r")
print(f"file type : {type(file.read())}")

file = open(source_file_path,"r")
print(f"file type : {type(file.readline())}")

file = open(source_file_path,"r")
print(f"file type : {type(file.readlines())}")

file.close()



with open(source_file_path,"r") as files:
    aa = files.readlines()
    print(aa[0])
print("********************************************--readlines--******************************************************")
with open(source_file_path,"r") as files:
    bb = files.readline()
    print(bb)
print("********************************************--readline--*******************************************************")

with open(source_file_path,"r") as files:
    cc = files.read()
    print(cc)
print("********************************************--read--***********************************************************")