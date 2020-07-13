-- displays the average temperature by city ordered by temperature
SELECT city, AVG(value) as avg_temp
from temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
