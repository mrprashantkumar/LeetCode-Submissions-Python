# Write your MySQL query statement below
(SELECT Users.name AS results
FROM Users
INNER JOIN MovieRating
ON Users.user_id = MovieRating.user_id
GROUP BY Users.name
ORDER BY COUNT(rating) DESC, Users.name
LIMIT 1)

UNION ALL

(SELECT Movies.title AS results
FROM Movies
INNER JOIN MovieRating
ON Movies.movie_id = MovieRating.movie_id AND created_at LIKE '2020-02-%'
GROUP BY Movies.title
ORDER BY AVG(rating) DESC, Movies.title
LIMIT 1)