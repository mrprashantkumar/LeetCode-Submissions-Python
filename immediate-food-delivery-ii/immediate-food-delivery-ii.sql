# Write your MySQL query statement below
SELECT ROUND(COUNT(*)*100 / (
  SELECT COUNT(DISTINCT customer_id)
  FROM Delivery
), 2) AS immediate_percentage
FROM Delivery 
WHERE (customer_id, order_date) IN (
  SELECT customer_id, MIN(order_date) AS minDate
  FROM Delivery
  GROUP BY customer_id
) AND order_date = customer_pref_delivery_date