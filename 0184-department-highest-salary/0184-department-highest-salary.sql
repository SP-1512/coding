select d.name as department, e.name as employee, e.salary from employee e
join
department d
on e.departmentId = d.id
where (d.name,e.salary) in (select d.name,max(e.salary) from employee e
join
department d
on e.departmentId = d.id
group by d.name);