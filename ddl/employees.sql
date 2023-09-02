create external table if not exists ukdatalake_eng_landing.employees
(
EMPLOYEE_ID string,
FIRST_NAME string,
LAST_NAME string,
EMAIL string,
PHONE_NUMBER string,
HIRE_DATE string,
JOB_ID string,
SALARY string,
COMMISSION_PCT string,
MANAGER_ID string,
DEPARTMENT_ID string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
location '/tmp/data/sample_employees';
