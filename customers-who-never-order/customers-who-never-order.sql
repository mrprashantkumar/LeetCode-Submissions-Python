# Write your MySQL query statement below

# SELECT Customers.name AS Customers
# FROM Customers
# WHERE Customers.id NOT IN (
#     SELECT customerId
#     FROM Orders
# );

SELECT Name AS 'Customers'
FROM Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.id IS NULL