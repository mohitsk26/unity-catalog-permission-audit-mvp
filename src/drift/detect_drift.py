import os
import pandas as pd

# -----------------------------
# Paths
# -----------------------------
DAY1_PATH = "data/silver/validated_permissions_day1.csv"
DAY2_PATH = "data/silver/validated_permissions_day2.csv"

OUTPUT_DIR = "reports"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "drift_report.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Read CSV files
# -----------------------------
day1 = pd.read_csv(DAY1_PATH)
day2 = pd.read_csv(DAY2_PATH)

# -----------------------------
# Merge on unique keys
# -----------------------------
merged = day1.merge(
    day2,
    on=["user", "role", "table_name"],
    how="outer",
    suffixes=("_day1", "_day2")
)

# -----------------------------
# Detect drift
# -----------------------------
def detect(row):

    old = row["permission_day1"]
    new = row["permission_day2"]

    if pd.isna(old):
        return "New Permission Added"

    elif pd.isna(new):
        return "Permission Removed"

    elif old != new:
        return "Permission Changed"

    else:
        return "No Drift"


merged["drift_status"] = merged.apply(detect, axis=1)

# Keep only drift records
drift_report = merged[merged["drift_status"] != "No Drift"]

# Save report
drift_report.to_csv(OUTPUT_FILE, index=False)

print("\n Drift Detection Completed")
print(f" Drift records found : {len(drift_report)}")
print(f" Report saved at : {OUTPUT_FILE}")

print("\nDrift Summary:")
print(drift_report)