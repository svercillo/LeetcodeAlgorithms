# Write your MySQL query statement below


Select E1.name as "Employee" From Employee as E1 inner join Employee as E2 on E2.id = E1.managerId where E1.salary > E2 .salary 
