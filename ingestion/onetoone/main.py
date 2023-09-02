import os
import sys
path = sys.path.append("/")
print(sys.path.append("/".join(os.getcwd().split('/'))))
from generic.common.generic_functions import upper_case
import pandas as pd

employees_df = pd.read_csv(r"D:\datalake\ingestion\onetoone\files\EMPLOYEES.csv")

dep_df = employees_df[employees_df['DEPARTMENT_ID']==90]
print(dep_df)
