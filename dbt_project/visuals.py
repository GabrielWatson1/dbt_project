import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/swapi_people.csv')

# Plot Gender count
gender_counts = df['gender'].value_counts()
plt.figure(figsize=(6,4))
gender_counts.plot(kind='bar', color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('data/gender_distribution.png')
plt.close()

# Plot Average Height
plt.figure(figsize=(6,4))
df['height'] = pd.to_numeric(df['height'], errors='coerce')  # convert to numeric
df.boxplot(column='height', by='gender', grid=False)
plt.title('Height Distribution by Gender')
plt.suptitle('')
plt.xlabel('Gender')
plt.ylabel('Height (cm)')
plt.tight_layout()
plt.savefig('data/height_by_gender.png')
plt.close()