# Write your MySQL query statement below

with temp as (select num, count(num) as _count from MyNumbers group by num)
select max(num) as num from temp where _count = 1;
