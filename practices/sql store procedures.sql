(select * from hr.employees WHERE department_id =100);

select * from hr.temp;
truncate table hr.temp;

create or replace PROCEDURE hr.UsrTempEmp
IS
BEGIN
insert into hr.temp (select * from hr.employees WHERE department_id =100);
END UsrTempEmp;

EXEC  hr.UsrTempEmp;


create or replace PROCEDURE hr.UsrTempEmpPara1
(p_department_id int,p_job_id VARCHAR)
IS
BEGIN
insert into hr.temp (select * from hr.employees WHERE department_id =p_department_id and JOB_ID = p_job_id );
END UsrTempEmpPara1;