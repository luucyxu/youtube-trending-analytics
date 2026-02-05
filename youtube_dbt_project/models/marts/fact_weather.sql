{{ config(enabled = false) }}

-- models/marts/fact_weather.sql

SELECT
    city,
    datetime,
    temperature_2m,
    relative_humidity_2m,
    windspeed_10m,
    temperature_2m - (0.7 * windspeed_10m) AS feels_like
FROM {{ ref('stg_weather') }}  -- Reference another dbt model!
