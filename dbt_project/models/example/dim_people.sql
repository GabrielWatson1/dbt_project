select
    name,
    case 
      when height = 'unknown' then null
      else cast(height as float)
    end as height,
    case
      when mass = 'unknown' then null
      else cast(replace(mass, ',', '') as float)
    end as mass,
    birth_year,
    gender
from {{ ref('swapi_people') }}