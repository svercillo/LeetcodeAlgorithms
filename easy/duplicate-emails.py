# Write your MySQL query statement below


select Email from Person group by Email Having count(Email) >1 
