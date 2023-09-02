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

class datatransfer:
    def __init__(self ,user, password, encoding, Hostname, Port, SID,path):
        self.user = user
        self.password = password
        self.encoding = encoding
        self.Hostname = Hostname
        self.Port = Port
        self.SID = SID
        self.path = path

        self.dsn = cx_Oracle.makedsn(self.Hostname, self.Port, self.SID)
        self.con = cx_Oracle.connect(user = self.user, password = self.password, dsn = self.dsn, encoding = self.encoding)
        print("***Database connection successfully***")

    def data_load_tables(self):
        try:
            con  = self.con
            path = self.path
            with open(path, 'r') as sqlfile:
                file = sqlfile.read().split(";")
                for sql in file:
                    if sql != '':
                        sql_query = sql.strip()
                        cursor = con.cursor()
                        cursor.execute(sql_query)
                        con.commit()
                print(f"***succesfully excuted***")
                con.close()
                print("Connection close")
        except Exception as e:
            print(f"Error : {e}")

"""*****************************connection between python and orcale*************************************************"""
script_name = sys.argv[0]
table_name = sys.argv[1]

config = configparser.ConfigParser()
config.read(r"D:\datalake\ingestion\file_to_oracle_db\config\connection.ini")
user = config.get("HR_DB", "user")
password = config.get("HR_DB", "password")
Hostname = config.get("HR_DB", "Hostname")
Port = config.get("HR_DB", "Port")
SID = config.get("HR_DB", "SID")
encoding = config.get("HR_DB", "encoding")
filepath = r"D:\datalake\ingestion\file_to_oracle_db\config"



for table in table_name.split(","):
    path = os.path.join(filepath,table)
    connection = datatransfer(user, password, encoding, Hostname, Port, SID, path)
    time.sleep(5)
    print(f"Data transfer to {table[:-4]}")
    connection.data_load_tables()
    print("ended")


