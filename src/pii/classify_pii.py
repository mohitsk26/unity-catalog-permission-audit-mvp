import os
import re
import pandas as pd

# ----------------------------------
# Paths
# ----------------------------------

RAW_DIR = "data/raw"
REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(REPORT_DIR, "pii_report.csv")

# ----------------------------------
# Regex Patterns
# ----------------------------------

EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

PHONE_REGEX = r'^[6-9]\d{9}$'

AADHAAR_REGEX = r'^\d{12}$'

PAN_REGEX = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

CARD_REGEX = r'^\d{16}$'

# ----------------------------------
# Results
# ----------------------------------

results = []

# ----------------------------------
# Scan all CSV files
# ----------------------------------

for file in os.listdir(RAW_DIR):

    if not file.endswith(".csv"):
        continue

    path = os.path.join(RAW_DIR, file)

    df = pd.read_csv(path)

    print(f"\nScanning {file}...")

    for column in df.columns:

        pii_type = "Not PII"

        column_lower = column.lower()

        # -----------------------------
        # Detect by column name
        # -----------------------------

        if "email" in column_lower:
            pii_type = "Email"

        elif "phone" in column_lower or "mobile" in column_lower:
            pii_type = "Phone"

        elif "aadhaar" in column_lower:
            pii_type = "Aadhaar"

        elif "pan" in column_lower:
            pii_type = "PAN"

        elif "card" in column_lower:
            pii_type = "Credit Card"

        # -----------------------------
        # Detect by sample values
        # -----------------------------

        else:

            sample_values = (
                df[column]
                .dropna()
                .astype(str)
                .head(10)
            )

            for value in sample_values:

                if re.match(EMAIL_REGEX, value):

                    pii_type = "Email"
                    break

                elif re.match(PHONE_REGEX, value):

                    pii_type = "Phone"
                    break

                elif re.match(AADHAAR_REGEX, value):

                    pii_type = "Aadhaar"
                    break

                elif re.match(PAN_REGEX, value):

                    pii_type = "PAN"
                    break

                elif re.match(CARD_REGEX, value):

                    pii_type = "Credit Card"
                    break

        results.append({

            "table_name": file,

            "column_name": column,

            "pii_type": pii_type

        })

# ----------------------------------
# Save Report
# ----------------------------------

report_df = pd.DataFrame(results)

report_df.to_csv(OUTPUT_FILE, index=False)

print("\nPII Classification Completed Successfully")
print(f"Report saved at: {OUTPUT_FILE}")