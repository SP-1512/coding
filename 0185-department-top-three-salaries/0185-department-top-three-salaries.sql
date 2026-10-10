with cte as(
    select d.name as department, e.name as Employee, e.salary as salary, 
    dense_rank() over(partition by d.id order by e.salary DESC) 
    as rank 
    from
    employee e join
    department d
    on e.departmentId = d.id
)
select department, Employee, salary from cte 
where rank <= 3;