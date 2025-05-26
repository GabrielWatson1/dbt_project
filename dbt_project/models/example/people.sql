select
   name
  ,height
  ,mass
  ,birth_year
from {{ ref('swapi_people') }}