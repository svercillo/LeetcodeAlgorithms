SELECT max(salary) as SecondHighestSalary from (
    SELECT salary from employee where id not in (
        Select id from employee where salary = (
            SELECT max(salary) from employee as T
        )
    )
) as subquery_alias
