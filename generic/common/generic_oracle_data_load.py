"""
Load raw data from one schema to other schema using python oracle.
pass argument 1 script name
              2 table name(we can pass multiple tables using separator ",")
"""


import os
import sys
import time
import configparser
import cx_Oracle


def orcale_connection(user, password, encoding, Hostname, Port, SID):
    try:
        dsn = cx_Oracle.makedsn(Hostname, Port, SID)
        con = cx_Oracle.connect(user=user, password=password, dsn=dsn, encoding=encoding)
        print("Successfully connected to Oracle Database")
    except Exception as e:
        print(f"Error : {e}")
    return con
def data_load_tables(path,con):
    try:
        with open(path, 'r') as sqlfile:
            file = sqlfile.read().split(";")
            for sql in file:
                if sql != '':
                    sql_query = sql.strip()
                    cursor = con.cursor()
                    cursor.execute(sql_query)
                    con.commit()
            print(f"succesfully excuted")
    except Exception as e:
        print(f"Error : {e}")

"""*****************************connection between python and orcale*************************************************"""

script_name = sys.argv[0]
table_name = sys.argv[1]

config = configparser.ConfigParser()
config.read(r"D:\datalake\ingestion\file_to_oracle_db\config\connection.ini") #replace the path according to ypur file loaction
user = config.get("HR_DB", "user")
password = config.get("HR_DB", "password")
Hostname = config.get("HR_DB", "Hostname")
Port = config.get("HR_DB", "Port")
SID = config.get("HR_DB", "SID")
encoding = config.get("HR_DB", "encoding")

con = orcale_connection(user=user, password=password, encoding=encoding, Hostname=Hostname, Port=Port, SID=SID)
path = r"D:\datalake\ingestion\file_to_oracle_db\config"
for table in table_name.split(","):
    filepath = os.path.join(path,table)
    time.sleep(5)
    print(f"Data transfer to {table[:-4]}")
    data_load_tables(filepath,con)
con.close()
print("Connection closed")
print("Program ended")