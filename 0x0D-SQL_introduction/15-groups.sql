-- lists the rows of the table that meets the requis
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
ORDER BY number DESC;
