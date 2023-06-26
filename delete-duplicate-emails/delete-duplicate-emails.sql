# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE FROM Person
WHERE Person.id NOT IN (
    SELECT minId
    FROM (
        SELECT MIN(Person.id) as minId
        FROM Person
        GROUP BY Person.email
    ) as newTable
);

# SELECT MIN(Person.id) as minId
# FROM Person
# GROUP BY Person.email;