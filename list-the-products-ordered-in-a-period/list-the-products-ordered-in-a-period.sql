# Write your MySQL query statement below
SELECT Products.product_name, SUM(Orders.unit) AS unit
FROM Products
INNER JOIN Orders
ON Products.product_id = Orders.product_id AND Orders.order_date LIKE '2020-02-__'
GROUP BY Products.product_name
HAVING SUM(Orders.unit) >= 100;