# Write your MySQL query statement below

SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
INNER JOIN Department
ON Employee.departmentId = Department.id
WHERE (Employee.DepartmentId, Employee.salary) IN (
  SELECT Employee.DepartmentId, MAX(Employee.salary)
  FROM Employee
  GROUP BY Employee.departmentID
);

# SELECT Employee.DepartmentId, MAX(Employee.salary)
# FROM Employee
# GROUP BY Employee.departmentID;