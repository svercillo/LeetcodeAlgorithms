WITH max_salary AS(    
    SELECT Department.id AS d_id, MAX(salary) as m_salary
    FROM Employee 
    JOIN Department 
    ON departmentId = Department.id
    GROUP BY d_id
)
SELECT Department.name AS Department,
    Employee.name AS Employee,
    salary AS Salary
FROM Employee 
RIGHT JOIN max_salary ON departmentId = d_id
    AND salary = m_salary
LEFT JOIN Department ON Department.id = d_id;
    
