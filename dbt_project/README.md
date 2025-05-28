Welcome to your new dbt project!

# Star Wars People Data Pipeline with dbt and DuckDB

## Overview

This project downloads Star Wars character data from the SWAPI API, processes it using dbt and DuckDB into dimension and fact models, and generates visualizations for key metrics.

---

## Prerequisites

- Python 3.8+
- Virtual environment (`venv`) set up
- DuckDB Python package
- dbt version 1.9.4
- Required Python packages listed in `requirements.txt`

---

## Setup and Usage

1. **Activate your virtual environment**

   ```bash
   source venv/Scripts/activate    # Windows PowerShell
   # or
   source venv/bin/activate        # Linux/macOS terminal

2. **Install required packages**
   ```bash
    pip install -r requierments.txt

3. **Download the raw data**
    ```bash
    python fetch_swapi_people.py

4. **Load seed data into DuckDB**
    ```bash
    dbt seed --select swapi_people

5. **Run dbt models to build dimension and fact tables**
    ```bash
    dbt run

6. **Create Visuals**
    ```bash
    python visualize_metrics.py

