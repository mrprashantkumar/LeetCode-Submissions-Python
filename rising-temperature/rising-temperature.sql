# Write your MySQL query statement below

SELECT T1.id
FROM Weather AS T1
INNER JOIN Weather AS T2
ON DATEDIFF(T1.recordDate, T2.recordDate) = 1 and T1.temperature > T2.temperature