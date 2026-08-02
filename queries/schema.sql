CREATE TABLE IF NOT EXISTS population_observations (
    indicator_id TEXT NOT NULL,
    indicator_name TEXT NOT NULL,
    topic TEXT,
    topic_label TEXT,
    unit TEXT,
    unit_label TEXT,
    geo_area TEXT NOT NULL,
    geo_name TEXT NOT NULL,
    time_period INTEGER NOT NULL,
    value REAL NOT NULL,
    source_type TEXT NOT NULL,
    PRIMARY KEY (indicator_id, geo_area, time_period)
);

CREATE INDEX IF NOT EXISTS idx_population_geo_period
    ON population_observations (geo_area, time_period);

CREATE INDEX IF NOT EXISTS idx_population_indicator_period
    ON population_observations (indicator_id, time_period);
