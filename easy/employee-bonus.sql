# Write your MySQL query statement below


SELECT name, bonus from Employee as e  LEFT OUTER JOIN Bonus as b on e.empId = b.empId where bonus is NULL or bonus< 1000;
