{{ config(materialized = 'view') }}

select
    video_id,
    country,
    title,
    channel_title,
    category_id,
    trending_date,
    publish_ts,
    tags,
    comments_disabled,
    ratings_disabled,
    video_error_or_removed
from {{ ref('stg_youtube_videos') }}
