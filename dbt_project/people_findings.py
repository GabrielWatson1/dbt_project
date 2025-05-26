import duckdb
import pandas as pd

# Connect to DuckDB
con = duckdb.connect('duckdb.db')

# Query all data from swapi_people
df = con.execute('SELECT * FROM swapi_people').df()

# Calculate the stats
total_characters = len(df)
avg_height = round(pd.to_numeric(df['height'], errors='coerce').mean(), 2)
avg_mass = round(pd.to_numeric(df['mass'], errors='coerce').mean(), 2)
oldest_birth_year = df['birth_year'].min()

# Print the results
print(f"Total characters: {total_characters}")
print(f"Average height: {avg_height} cm")
print(f"Average mass: {avg_mass} kg")
print(f"Oldest birth year: {oldest_birth_year}")