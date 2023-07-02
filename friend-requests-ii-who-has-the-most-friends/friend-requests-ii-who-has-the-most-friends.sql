# Write your MySQL query statement below
SELECT requester_id AS id, COUNT(requester_id) AS num
FROM (
  SELECT requester_id 
  FROM RequestAccepted

  UNION ALL

  SELECT accepter_id
  FROM RequestAccepted
) AS temp
GROUP BY id
ORDER BY num DESC
LIMIT 1