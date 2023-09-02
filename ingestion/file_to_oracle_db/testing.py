import cx_Oracle
import os

#os.environ["user"] = "hr"
#password = os.environ["password"] = "hr"
Hostname = os.environ["Hostname"] = "localhost"
Port = os.environ["Port"] = "1521"
SID = os.environ["SID"] = "xe"
encoding = os.environ["encoding"] = "UTF-8"



user  = os.getenv("user")
print(user)
password = os.getenv("password")
print(password)
Hostname = os.getenv("Hostname")
Port = os.getenv("Port")
SID = os.getenv("SID")
encoding = os.getenv("encoding")




dsn = cx_Oracle.makedsn("localhost","1521","xe")
con = cx_Oracle.connect(user = "hr",password = "hr",dsn = dsn,encoding = "UTF-8")
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

