# Write your MySQL query statement below
SELECT Temp.name
FROM (
  SELECT E1.id, E1.name
  FROM Employee AS E1
  INNER JOIN Employee AS E2
  ON E1.id = E2.managerId
) AS Temp
GROUP BY Temp.id
HAVING COUNT(*) >= 5;