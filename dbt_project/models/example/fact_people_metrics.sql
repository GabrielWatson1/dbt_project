with base as (
    select
        gender
        ,height
        ,mass
    from {{ ref('dim_people') }}
    where height is not null and mass is not null
)

select
    gender,
    count(*) as people_count
    ,avg(height) as avg_height
    ,avg(mass) as avg_mass
from base
group by gender