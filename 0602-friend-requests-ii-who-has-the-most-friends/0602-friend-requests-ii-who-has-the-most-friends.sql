with cte as
(
    select requester_id as id from RequestAccepted
    union all
    select accepter_id as id from RequestAccepted;
),
friends_count as
(
select id, count(*) as num from cte
group by id;
)
select * from friends_count where num = (select max(num) from friends_count);