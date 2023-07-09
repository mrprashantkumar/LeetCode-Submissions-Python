# Write your MySQL query statement below
SELECT LEFT(trans_date, 7) AS month, country, COUNT(*) AS trans_count, SUM(IF(state = 'approved', 1, 0)) AS approved_count,
SUM(amount) AS trans_total_amount, SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount

FROM Transactions
GROUP BY LEFT(trans_date, 7), country;