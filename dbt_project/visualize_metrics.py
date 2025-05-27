import pandas as pd
import matplotlib.pyplot as plt
import duckdb

# Query the fact_people_metrics model
con = duckdb.connect("dev.duckdb")

query = """
    SELECT *
    FROM fact_people_metrics
"""

df = con.execute(query).fetch_df()

# Bar plot: average height by gender
plt.figure(figsize=(8, 5))
plt.bar(df['gender'], df['avg_height'], color='skyblue')
plt.title('Average Height by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Height')
plt.tight_layout()
plt.savefig("visuals/avg_height_by_gender.png")
plt.show()

# Bar plot: average mass by gender
plt.figure(figsize=(8, 5))
plt.bar(df['gender'], df['avg_mass'], color='salmon')
plt.title('Average Mass by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Mass')
plt.tight_layout()
plt.savefig("visuals/avg_mass_by_gender.png")
plt.show()
