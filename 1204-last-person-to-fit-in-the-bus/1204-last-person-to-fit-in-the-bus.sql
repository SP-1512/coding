with cte as(
    select queue.*, 
    sum(weight) over(order by turn) as total_weight
    from queue
)
select person_name from cte 
where turn = (select max(turn) from cte where total_weight <= 1000 );
