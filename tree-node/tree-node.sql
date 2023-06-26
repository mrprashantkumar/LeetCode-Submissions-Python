# Write your MySQL query statement below
SELECT id, 'Root' as type
FROM Tree
WHERE p_id IS NULL

UNION ALL

SELECT id, 'Leaf' as type
FROM Tree
WHERE p_id IS NOT NULL AND id NOT IN (
    SELECT DISTINCT p_id
    FROM TREE
    WHERE p_id IS NOT NULL
)

UNION ALL

SELECT id, 'Inner' as type
FROM Tree
WHERE p_id IS NOT NULL AND id IN (
    SELECT DISTINCT p_id
    FROM TREE
    WHERE p_id IS NOT NULL
)