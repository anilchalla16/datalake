select * from hr.employees;

select * from hr.departments;

--inner join using emp and dept tables (coomon id = depa_id)
select 
e.employee_id,
e.first_name,
e.last_name,
e.hire_date,
e.salary,
e.department_id,
d.department_name
from 
hr.employees e
inner join hr.departments d 
on
e.department_id = d.department_id
where e.department_id = 50;


-- group by and inner join using emp and dept tables (common id is dept_id)
select e.department_id,
e.first_name,
e.last_name,
e.salary,
d.department_name,
MAX(e.salary)
from 
hr.employees e
INNER JOIN
hr.departments d
on
e.department_id = d.department_id
GROUP BY e.department_id,
e.first_name,
e.last_name,
e.salary,
d.department_name
HAVING e.department_id =100;


--window function used row number ,densk rank ,rank 
SELECT
    e.first_name,
    e.last_name,
    e.first_name||' '||e.last_name as fullname,
    e.salary,
    d.department_name,
    rank() over(PARTITION BY (e.department_id) order by e.department_id desc) as dep_rank,
    DENSE_RANK() over(PARTITION BY (e.department_id) order by e.department_id desc) as dep_rank,
    ROW_NUMBER() over(PARTITION BY (e.department_id) order by e.department_id desc) as seq
FROM
employees e
inner join 
hr.departments d
on e.department_id = d.department_id
where e.department_id = 100;


select 
e.first_name,
e.last_name,
e.first_name ||' '||e.last_name as fullname,
concat(e.first_name,concat(' ',e.last_name)) as fullname 
from
hr.employees e;


select e.department_id,count(e.department_id) from hr.employees e
group by e.department_id;


select 
count(e.department_id),
e.department_id,
d.department_name
from
hr.employees e
inner join 
hr.departments d
on e.department_id = d.department_id
group by e.department_id,
d.department_name
;



select 
count(e.department_id),
e.department_id,
d.department_name,
e.first_name ||' '||e.last_name as name
from
hr.employees e
inner join 
hr.departments d
on e.department_id = d.department_id
group by e.department_id,
d.department_name,
e.first_name,
e.last_name
;

select 
e.first_name ||' '||e.last_name as name,
concat(e.first_name,concat(' ',e.last_name)) as fullname,
d.department_name
from
hr.employees e
inner join 
hr.departments d
on e.department_id = d.department_id
;

SELECT
    e.first_name,
    e.last_name,
    e.first_name||' '||e.last_name as fullname,
    e.salary,
    d.department_name,
    count(e.department_id) over(PARTITION BY (e.department_id) order by e.department_id desc) as seq
FROM
employees e
inner join 
hr.departments d
on e.department_id = d.department_id
where e.department_id = 100;








select * from hr.employees e
where e.salary =
(select max(e.salary) from hr.employees e);

select e.department_id,max(e.salary) from hr.employees e
GROUP BY e.department_id;



select * from hr.employees;

select
emp_sal.salary_rank,
emp_sal.department_id,
emp_sal.first_name,
emp_sal.last_name,
emp_sal.salary
from
(select
e.department_id,
e.first_name,
e.last_name,
e.salary,
row_number() OVER (PARTITION BY e.department_id ORDER BY e.department_id DESC) as salary_rank
from
hr.employees e) emp_sal
where emp_sal.salary_rank=1;