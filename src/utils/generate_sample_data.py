"""
=========================================================
Generate Sample Data

Project:
Unity Catalog Permission Audit & Drift Detector MVP

Purpose:
Generate synthetic enterprise datasets for
testing governance, PII detection and permission drift.

Author:
Mohit Singh Kashyap

=========================================================
"""

import os
import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

# ------------------------------------
# Create output directory if not exists
# ------------------------------------

OUTPUT_PATH = "data/raw"

os.makedirs(OUTPUT_PATH, exist_ok=True)


# ------------------------------------
# Generate Customers Dataset
# ------------------------------------

def generate_customers(n=1000):

    customers = []

    for i in range(1, n + 1):

        customers.append({

            "customer_id": i,

            "customer_name": fake.name(),

            "email": fake.email(),

            "phone": fake.msisdn()[:10],

            "pan": "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5))
                    + str(random.randint(1000, 9999))
                    + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),

            "aadhaar": str(random.randint(100000000000, 999999999999)),

            "salary": random.randint(300000, 2500000),

            "city": fake.city()

        })

    df = pd.DataFrame(customers)

    df.to_csv(f"{OUTPUT_PATH}/customers.csv", index=False)

    print("✅ customers.csv generated")


# ------------------------------------
# Generate Employees Dataset
# ------------------------------------

def generate_employees(n=300):

    departments = [
        "Finance",
        "HR",
        "IT",
        "Security",
        "Compliance",
        "Operations"
    ]

    employees = []

    for i in range(1, n + 1):

        employees.append({

            "employee_id": i,

            "employee_name": fake.name(),

            "department": random.choice(departments),

            "email": fake.email(),

            "phone": fake.msisdn()[:10],

            "salary": random.randint(400000, 2000000)

        })

    df = pd.DataFrame(employees)

    df.to_csv(f"{OUTPUT_PATH}/employees.csv", index=False)

    print("✅ employees.csv generated")


# ------------------------------------
# Permission Snapshot Day 1
# ------------------------------------

def generate_permissions_day1():

    permissions = [

        ["analyst01", "Data Analyst", "customers", "SELECT"],

        ["finance01", "Finance", "customers", "SELECT"],

        ["admin01", "Admin", "customers", "ALL"],

        ["hr01", "HR", "employees", "SELECT"],

        ["security01", "Security", "employees", "ALL"]

    ]

    df = pd.DataFrame(

        permissions,

        columns=[
            "user",
            "role",
            "table_name",
            "permission"
        ]

    )

    df.to_csv(f"{OUTPUT_PATH}/permissions_day1.csv", index=False)

    print("✅ permissions_day1.csv generated")


# ------------------------------------
# Permission Snapshot Day 2
# ------------------------------------

def generate_permissions_day2():

    permissions = [

        ["analyst01", "Data Analyst", "customers", "SELECT,UPDATE"],

        ["finance01", "Finance", "customers", "SELECT"],

        ["admin01", "Admin", "customers", "ALL"],

        ["hr01", "HR", "employees", "SELECT"],

        ["security01", "Security", "employees", "ALL"]

    ]

    df = pd.DataFrame(

        permissions,

        columns=[
            "user",
            "role",
            "table_name",
            "permission"
        ]

    )

    df.to_csv(f"{OUTPUT_PATH}/permissions_day2.csv", index=False)

    print("✅ permissions_day2.csv generated")


# ------------------------------------
# Main
# ------------------------------------

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("Generating Enterprise Sample Data")

    print("=" * 60)

    generate_customers()

    generate_employees()

    generate_permissions_day1()

    generate_permissions_day2()

    print()

    print("🎉 Sample datasets generated successfully.")