{{ config(enabled = false) }}

-- models/staging/stg_weather.sql

SELECT					-- note there is no CREATE TABLE
    time,
    CAST(time AS TIMESTAMP) AS datetime,
    temperature_2m,
    relative_humidity_2m,
    windspeed_10m,
    'Chicago' AS city
FROM raw_weather
WHERE time IS NOT NULL
