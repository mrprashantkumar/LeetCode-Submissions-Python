# Write your MySQL query statement below
SELECT DISTINCT T1.num AS ConsecutiveNums
FROM Logs T1, Logs T2, Logs T3
WHERE T1.id = T2.id-1 AND T2.id = T3.id-1 AND T1.num = T2.num AND T2.num = T3.num