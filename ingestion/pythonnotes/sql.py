import os
import sys

scriptname  = sys.argv[0]
table_name = sys.argv[1]
try:
    if len(sys.argv) ==2:
        print("process the script")
    else:
        print("No enough paramters")
except Exception as e:
    print(f"An exception occurred {e}")

for i in table_name.split(','):
    print(i)