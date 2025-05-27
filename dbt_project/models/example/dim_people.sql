select
   name
  ,CASE WHEN TRY_CAST(height AS FLOAT) IS NOT NULL THEN height ELSE NULL END as height
  ,CASE WHEN TRY_CAST(mass AS FLOAT) IS NOT NULL THEN mass ELSE NULL END as mass
  ,gender
  ,birth_year
from {{ ref('swapi_people') }}