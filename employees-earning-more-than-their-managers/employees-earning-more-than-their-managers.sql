# Write your MySQL query statement below
SELECT A.name as Employee
FROM employee as A
JOIN employee as B
ON A.managerId = B.id and A.salary > B.salary;