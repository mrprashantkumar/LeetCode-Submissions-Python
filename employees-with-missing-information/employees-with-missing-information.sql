# Write your MySQL query statement below
SELECT E.employee_id
FROM Employees AS E
WHERE E.employee_id NOT IN (
  SELECT S.employee_id
  FROM Salaries AS S
)

UNION 

SELECT S.employee_id
FROM Salaries AS S
WHERE S.employee_id NOT IN (
  SELECT E.employee_id
  FROM Employees AS E
)

ORDER BY employee_id