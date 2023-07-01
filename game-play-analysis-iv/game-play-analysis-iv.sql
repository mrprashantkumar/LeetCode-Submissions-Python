# Write your MySQL query statement below
SELECT ROUND(COUNT(*) / (
  SELECT COUNT(DISTINCT player_id)
  FROM Activity
) , 2) AS fraction
FROM (
  SELECT A1.player_id, MIN(A1.event_date) AS minDate
  FROM Activity AS A1
  GROUP BY A1.player_id
) AS T1
INNER JOIN Activity AS A2
ON T1.player_id = A2.player_id AND DATEDIFF(A2.event_date, T1.minDate) = 1

# SELECT A1.player_id, MIN(A1.event_date) AS minDate
# FROM Activity AS A1
# GROUP BY A1.player_id