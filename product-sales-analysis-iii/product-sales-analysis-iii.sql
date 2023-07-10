# Write your MySQL query statement below
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
  SELECT Sales.product_id, MIN(year) as mini
  FROM Sales
  GROUP BY Sales.product_id
);