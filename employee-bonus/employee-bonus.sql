# Write your MySQL query statement below
SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empID = Bonus.empID
WHERE IFNULL(Bonus.bonus, 0) < 1000;