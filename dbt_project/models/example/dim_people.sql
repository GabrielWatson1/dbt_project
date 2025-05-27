select
   name
  ,height
  ,mass
  ,gender
  ,birth_year
from {{ ref('swapi_people') }}