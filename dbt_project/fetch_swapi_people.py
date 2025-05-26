import requests
import csv
import os

def fetch_people():
    url = "https://swapi.dev/api/people/"
    people = []

    while url:
        print(f"Fetching: {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        people.extend(data['results'])
        url = data['next']

    return people

def save_to_csv(data, filename):
    # Ensure data folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Pick columns to save
    keys = ['name', 'height', 'mass', 'gender', 'birth_year']

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, '') for key in keys}
            writer.writerow(row)

if __name__ == "__main__":
    people = fetch_people()
    save_to_csv(people, "data/swapi_people.csv")
    print("Saved data/swapi_people.csv")
