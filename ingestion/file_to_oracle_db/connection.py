import configparser
import cx_Oracle

config = configparser.ConfigParser()
config.read(r"D:\datalake\ingestion\file_to_oracle_db\config\connection.ini")
user = config.get("HR_DB","user")
password = config.get("HR_DB","password")
Hostname = config.get("HR_DB","Hostname")
Port = config.get("HR_DB","Port")
SID = config.get("HR_DB","SID")
encoding = config.get("HR_DB","encoding")


dsn = cx_Oracle.makedsn(Hostname,Port,SID)
con = cx_Oracle.connect(user = user,password = password,dsn = dsn,encoding = encoding)
print("Successfully connected to Oracle Database")
cursor = con.cursor()
cursor.execute("select * from hr.employees")
res = cursor.fetchall()
for row in res:
    pass

delete_query = "truncate table hr.emp"
cursor.execute(delete_query)
con.commit()
print("execute drop query successfully")

insert_query = "INSERT INTO hr.emp SELECT * FROM hr.employees"
cursor.execute(insert_query)
con.commit()
print("execute insert query successfully")

con.close()
print("connection close")

