# Write your MySQL query statement below
SELECT Product.product_id, Product.product_name
FROM Product
INNER JOIN Sales
ON Product.product_id = Sales.product_id
GROUP BY Sales.product_id
HAVING COUNT(*) = SUM(IF(Sales.sale_date BETWEEN '2019-01-01' AND '2019-03-31', 1, 0))