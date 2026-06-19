import os
import pandas as pd

# -----------------------------------
# Directories
# -----------------------------------
BRONZE_DIR = "data/bronze"
SILVER_DIR = "data/silver"
REPORT_DIR = "reports"

os.makedirs(SILVER_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# -----------------------------------
# Files to validate
# -----------------------------------
FILES = [
    "permissions_day1.csv",
    "permissions_day2.csv"
]

# -----------------------------------
# Valid permission values
# -----------------------------------
ALLOWED_PERMISSIONS = {
    "SELECT",
    "UPDATE",
    "INSERT",
    "DELETE",
    "MODIFY",
    "ALL"
}


def is_valid_permission(permission):

    if pd.isna(permission):
        return False

    permissions = [p.strip() for p in str(permission).split(",")]

    return all(p in ALLOWED_PERMISSIONS for p in permissions)


# -----------------------------------
# Validate each file
# -----------------------------------
for file in FILES:

    input_path = os.path.join(BRONZE_DIR, file)

    output_path = os.path.join(
        SILVER_DIR,
        f"validated_{file}"
    )

    report_path = os.path.join(
        REPORT_DIR,
        f"validation_report_{file.replace('.csv','.txt')}"
    )

    print(f"\nProcessing {file}...")

    # Read file
    df = pd.read_csv(input_path)

    total_records = len(df)

    # -----------------------------
    # Remove duplicates
    # -----------------------------
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    # -----------------------------
    # Remove missing values
    # -----------------------------
    missing_records = df.isnull().any(axis=1).sum()
    df = df.dropna()

    # -----------------------------
    # Validate permissions
    # -----------------------------
    invalid_mask = ~df["permission"].apply(is_valid_permission)

    invalid_permissions = invalid_mask.sum()

    df = df[~invalid_mask]

    valid_records = len(df)

    # -----------------------------
    # Save validated data
    # -----------------------------
    df.to_csv(output_path, index=False)

    # -----------------------------
    # Save validation report
    # -----------------------------
    with open(report_path, "w") as f:

        f.write("Validation Report\n")
        f.write("=========================\n\n")

        f.write(f"File                 : {file}\n")
        f.write(f"Total Records        : {total_records}\n")
        f.write(f"Duplicates Removed   : {duplicates}\n")
        f.write(f"Missing Records      : {missing_records}\n")
        f.write(f"Invalid Permissions  : {invalid_permissions}\n")
        f.write(f"Valid Records        : {valid_records}\n")

    print("Validation Completed Successfully")
    print(f"Validated file saved at: {output_path}")
    print(f"Validation report saved at: {report_path}")

print("\nAll files validated successfully.")