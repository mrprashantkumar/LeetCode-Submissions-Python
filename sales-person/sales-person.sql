# Write your MySQL query statement below
SELECT SalesPerson.name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    INNER JOIN Company
    ON Orders.com_id = Company.com_id and Company.name = "RED"
);