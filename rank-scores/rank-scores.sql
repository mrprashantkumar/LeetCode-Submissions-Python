# Write your MySQL query statement below
SELECT S1.score, (
    SELECT COUNT(DISTINCT score)
    FROM Scores AS S2
    WHERE S2.score >= S1.score
) AS 'rank'
FROM Scores AS S1
ORDER BY S1.score DESC