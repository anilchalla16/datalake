import configparser
#################################################################################################################
config = configparser.ConfigParser()
config.read(r"C:\Users\canil\PycharmProjects\datatransfer\assets\config.ini")
df_input_path = config.get('paths', 'emp_path')


import logging
import fnmatch
import os



patter_count = 0
match_count = 2

file_count_match = 3

retry=0
max_try = 5
is_success = False
while retry<max_try and not is_success:
    pattern =  'DEP*.csv'
    path = r"D:\Informatica\server\infa_shared\SrcFiles\python"
    file_path = os.listdir(path)
    file_count = len(file_path)
    print(file_count)
    for file in file_path:
        if fnmatch.fnmatch(file, pattern):
            print(f"file in dir {file}")
            patter_count = patter_count +1
            is_success=True
        if is_success:
            if match_count == int(patter_count):
                print("count is equal")
                break
            else:
                print(f"File count in SFG  is not equal match count {file_match_count} != {match_count}")
    else:
        retry = retry+1
        if retry == max_try:
            if file_count_match == file_count:
                print('not found')
            elif file_count_match > file_count:
                print('none')
            break
