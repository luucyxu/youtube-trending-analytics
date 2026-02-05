
        
with source as (
        
    select
        video_id,
        country,
        title,
        channel_title,   
        category_id,
        trending_date,
        publish_time,
        tags,
        views,
        likes,
        dislikes,
        comment_count,
        comments_disabled,
        ratings_disabled,
        video_error_or_removed
    from MAGPIE_FINAL_PROJECT.RAW.RAW_YOUTUBE_TRENDING
        
),
        
cleaned as (  
        
    select
        video_id,
        country,
        title,
        channel_title,
        category_id,
        try_to_date(trending_date, 'YY.DD.MM') as trending_date,
        try_to_timestamp_ntz(publish_time)      as publish_ts,
        tags, 
        try_cast(views as number) as views,
        try_cast(likes as number) as likes,
        try_cast(dislikes as number) as dislikes,
        try_cast(comment_count as number) as comment_count,
        comments_disabled,
        ratings_disabled,
        video_error_or_removed
    from source
    where trending_date is not null    
)
        
select * from cleaned