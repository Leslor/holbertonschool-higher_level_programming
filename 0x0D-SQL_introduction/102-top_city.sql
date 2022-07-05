-- script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT TOP 3 city, AVG(value) as avg_temp FROM temperatures GROUP BY city WHERE month = 7 OR month = 8 ORDER BY avg_temp DESC;
