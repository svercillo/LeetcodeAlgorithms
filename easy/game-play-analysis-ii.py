# Write your MySQL query statement below

select A.player_id, A.device_id from activity as A Inner join
(SELECT player_id, MIN(event_date) as date 
from activity GROUP BY player_id) as temp
    on A.player_id = temp.player_id and A.event_date = temp.date
