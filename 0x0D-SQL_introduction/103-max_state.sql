-- displays the average temperature by city ordered by temperature
SELECT state, MAX(value) as max_temp from temperatures
GROUP BY state ORDER BY state;
