# Star Wars People Insights

## Overview

This report highlights key insights from the Star Wars people dataset fetched from the [SWAPI](https://swapi.dev) API and transformed using dbt and DuckDB.

---

## 1. Average Height and Mass

```sql
SELECT
    AVG(CAST(height AS FLOAT)) AS avg_height,
    AVG(CAST(mass AS FLOAT)) AS avg_mass
FROM people;

## 2. Gender count

SELECT
    gender,
    COUNT(*) AS count
FROM people
GROUP BY gender
ORDER BY count DESC;

## 3. Most common birth years

SELECT
    birth_year,
    COUNT(*) AS count
FROM people
GROUP BY birth_year
ORDER BY count DESC
LIMIT 5;
