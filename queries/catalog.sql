CREATE TABLE IF NOT EXISTS population_observation (
    indicator_id TEXT NOT NULL,
    indicator_name TEXT NOT NULL,
    geo_area TEXT NOT NULL,
    time_period TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT NOT NULL,
    topic TEXT NOT NULL,
    source_type TEXT NOT NULL,
    PRIMARY KEY (indicator_id, geo_area, time_period)
);

-- Observaciones de una entidad ordenadas por periodo.
SELECT indicator_id, geo_area, time_period, value
FROM population_observation
WHERE indicator_id = :indicator_id AND geo_area = :geo_area
ORDER BY time_period;

-- Ranking por entidad para un periodo.
SELECT geo_area, SUM(value) AS value
FROM population_observation
WHERE indicator_id = :indicator_id AND time_period = :time_period
GROUP BY geo_area
ORDER BY value DESC;

-- Cobertura por indicador.
SELECT indicator_id, COUNT(DISTINCT geo_area) AS geographies, COUNT(*) AS observations
FROM population_observation
GROUP BY indicator_id
ORDER BY indicator_id;
