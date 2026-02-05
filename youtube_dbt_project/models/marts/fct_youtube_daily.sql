{{ config(
    materialized = 'table',
    schema = 'STAGING_MARTS'
) }}
        
with base as (
    select  
        trending_date,
        country,
        category_id,
        count(*)                              as video_count,
        sum(try_cast(views as int))           as total_views,
        sum(try_cast(likes as int))           as total_likes,
        sum(try_cast(comment_count as int))   as total_comments,
    from {{ ref('stg_youtube_videos') }}
    where trending_date is not null
    group by
        trending_date,
        country,
        category_id 
)
        
select 
    trending_date,
    country,
    category_id,
    video_count,
    total_views,
    total_likes,
    total_comments
from base

