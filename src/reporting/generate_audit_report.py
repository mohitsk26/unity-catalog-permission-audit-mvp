import os
import pandas as pd
from datetime import datetime

# -----------------------------------
# Paths
# -----------------------------------

DRIFT_REPORT = "reports/drift_report.csv"

VALIDATION_DAY1 = "reports/validation_report_permissions_day1.txt"
VALIDATION_DAY2 = "reports/validation_report_permissions_day2.txt"

GOLD_DIR = "data/gold"
REPORT_DIR = "reports"

os.makedirs(GOLD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

AUDIT_REPORT = os.path.join(REPORT_DIR, "audit_report.txt")

# -----------------------------------
# Read Drift Report
# -----------------------------------

if os.path.exists(DRIFT_REPORT):

    drift_df = pd.read_csv(DRIFT_REPORT)

    total_drifts = len(drift_df)

    permission_changes = (
        drift_df["drift_status"] == "Permission Changed"
    ).sum()

    new_permissions = (
        drift_df["drift_status"] == "New Permission Added"
    ).sum()

    removed_permissions = (
        drift_df["drift_status"] == "Permission Removed"
    ).sum()

else:

    total_drifts = 0
    permission_changes = 0
    new_permissions = 0
    removed_permissions = 0

# -----------------------------------
# Generate Audit Report
# -----------------------------------

with open(AUDIT_REPORT, "w") as f:

    f.write("=" * 50 + "\n")
    f.write("Unity Catalog Permission Audit Report\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Generated On : {datetime.now()}\n\n")

    f.write("Validation Files\n")
    f.write("-----------------------------\n")
    f.write(f"Day 1 : {VALIDATION_DAY1}\n")
    f.write(f"Day 2 : {VALIDATION_DAY2}\n\n")

    f.write("Drift Summary\n")
    f.write("-----------------------------\n")
    f.write(f"Total Drift Records      : {total_drifts}\n")
    f.write(f"Permission Changes       : {permission_changes}\n")
    f.write(f"New Permissions Added    : {new_permissions}\n")
    f.write(f"Permissions Removed      : {removed_permissions}\n\n")

    if total_drifts > 0:

        f.write("Risk Level : HIGH\n\n")

        f.write("Drift Details\n")
        f.write("-----------------------------\n")

        for _, row in drift_df.iterrows():

            f.write(
                f"User : {row['user']}\n"
            )

            f.write(
                f"Role : {row['role']}\n"
            )

            f.write(
                f"Table : {row['table_name']}\n"
            )

            f.write(
                f"Old Permission : {row['permission_day1']}\n"
            )

            f.write(
                f"New Permission : {row['permission_day2']}\n"
            )

            f.write(
                f"Status : {row['drift_status']}\n"
            )

            f.write("\n")

    else:

        f.write("Risk Level : LOW\n")
        f.write("No Permission Drift Detected.\n")

print("\nAudit Report Generated Successfully")
print(f"Location : {AUDIT_REPORT}")