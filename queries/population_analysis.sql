-- DA-05: descriptive SQL queries for the normalized population table.

-- summary_by_entity
SELECT geo_area, geo_name, COUNT(*) AS observation_count,
       MIN(value) AS minimum_value, MAX(value) AS maximum_value
FROM population_observations
WHERE indicator_id = :indicator_id
GROUP BY geo_area, geo_name
ORDER BY geo_area;

-- latest_values
WITH latest_period AS (
    SELECT MAX(time_period) AS time_period
    FROM population_observations
    WHERE indicator_id = :indicator_id
)
SELECT geo_area, geo_name, time_period, value
FROM population_observations
WHERE indicator_id = :indicator_id
  AND time_period = (SELECT time_period FROM latest_period)
ORDER BY value DESC, geo_area;

-- year_over_year_change
WITH series AS (
    SELECT geo_area, geo_name, time_period, value,
           LAG(value) OVER (
               PARTITION BY indicator_id, geo_area ORDER BY time_period
           ) AS previous_value
    FROM population_observations
    WHERE indicator_id = :indicator_id
)
SELECT geo_area, geo_name, time_period, value, previous_value,
       value - previous_value AS absolute_change,
       CASE WHEN previous_value IS NULL OR previous_value = 0 THEN NULL
            ELSE ((value - previous_value) / previous_value) * 100.0
       END AS percent_change
FROM series
WHERE previous_value IS NOT NULL
ORDER BY geo_area, time_period;
