def upper_case(columnname):
    return columnname.upper()

def lower_case(columnname):
    columnname = columnname.strip(" ")
    return columnname.lower()

def file_validation(filepath,file_headers):
    with open(filepath,"r") as files:
        files_header = files.readline().strip().lower()
        if files_header == file_headers.lower():
            print("*******Headers_validated*******")
        else:
            print("*******Headers_mismatched******")

import os
import sys
def file_validations(filepath,file_headers):
    file_size = os.path.getsize(filepath)
    if file_size ==0:
        print(f"File contains zero bytes : {file_size}")
        sys.exit(1)
    with open(filepath,"r") as files:
        files_contains_headers = files.readlines()
        if len(files_contains_headers) == 1:
            print("File contains only headers")
            sys.exit(1)
        files_header = files.readline().strip().lower()
        if files_header == file_headers.lower():
            print("*******Headers_validated*******")
        else:
            print("*******Headers_mismatched******")
