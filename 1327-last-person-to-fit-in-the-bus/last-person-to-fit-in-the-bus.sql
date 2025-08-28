# Write your MySQL query statement below
with cte as (select *,
sum(weight) over(order by turn ) as rn
from Queue)

select person_name
from cte 
where rn<1001
order by rn desc
limit 1;