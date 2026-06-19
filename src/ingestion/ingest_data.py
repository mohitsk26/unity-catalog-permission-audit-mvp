"""
=========================================================
Data Ingestion Module

Project:
Unity Catalog Permission Audit & Drift Detector MVP

Purpose:
Read raw datasets and ingest them into
the Bronze layer.

Author:
Mohit Singh Kashyap
=========================================================
"""

import os
import shutil
import pandas as pd

from config import RAW_DATA_PATH, BRONZE_PATH


# ----------------------------------------
# Create bronze directory if not exists
# ----------------------------------------

os.makedirs(BRONZE_PATH, exist_ok=True)


# ----------------------------------------
# Ingest single file
# ----------------------------------------

def ingest_file(filename):

    source_path = os.path.join(RAW_DATA_PATH, filename)

    destination_path = os.path.join(BRONZE_PATH, filename)

    if not os.path.exists(source_path):

        print(f"❌ {filename} not found.")

        return

    df = pd.read_csv(source_path)

    print(f"\nReading {filename}")

    print(f"Rows : {len(df)}")

    print(f"Columns : {len(df.columns)}")

    shutil.copy(source_path, destination_path)

    print("✅ Moved to Bronze Layer")


# ----------------------------------------
# Main Ingestion Pipeline
# ----------------------------------------

def ingest_all():

    files = [

        "customers.csv",

        "employees.csv",

        "permissions_day1.csv",

        "permissions_day2.csv"

    ]

    for file in files:

        ingest_file(file)


if __name__ == "__main__":

    print()

    print("=" * 60)

    print("BRONZE LAYER INGESTION")

    print("=" * 60)

    ingest_all()

    print()

    print("🎉 Bronze Layer Created Successfully")