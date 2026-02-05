{{ config(enabled = false) }}

-- models/marts/fact_weather_daily.sql

{{ config(
    materialized='table',
    tags=['daily', 'aggregated']
) }}

SELECT
    city,
    DATE(datetime) AS date,
    AVG(temperature_2m) AS avg_temperature,
    AVG(relative_humidity_2m) AS avg_humidity,
    AVG(windspeed_10m) AS avg_windspeed,
    AVG(feels_like) AS avg_feels_like,
    MIN(temperature_2m) AS min_temperature,
    MAX(temperature_2m) AS max_temperature,
    COUNT(*) AS hourly_records
FROM {{ ref('fact_weather') }}
GROUP BY city, DATE(datetime)
ORDER BY date
