select
   name
  ,height
  ,mass
  ,hair_color
  ,skin_color
  ,eye_color
  ,birth_year
  ,gender
from {{ ref('swapi_people') }}