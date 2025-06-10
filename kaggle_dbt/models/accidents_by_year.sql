-- models/accidents_by_year.sql

SELECT
    date_part('year', crash_date) AS accident_year,
    COUNT(*) AS total_accidents,
    SUM(injuries_total) AS total_injuries,
    SUM(injuries_fatal) AS total_fatalities
FROM {{ ref('stg_accidents') }}
GROUP BY accident_year
ORDER BY accident_year
