import os
import pandas as pd

# ---------------------------------
# Paths
# ---------------------------------

PII_REPORT = "reports/pii_report.csv"

REPORT_DIR = "reports"
GOLD_DIR = "data/gold"

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(GOLD_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(
    REPORT_DIR,
    "masking_recommendation.csv"
)

# ---------------------------------
# Read PII Report
# ---------------------------------

df = pd.read_csv(PII_REPORT)

# ---------------------------------
# Mapping
# ---------------------------------

masking_policy = {

    "Email": "SHA256 Hash",

    "Phone": "Partial Mask (XXXXXX1234)",

    "PAN": "Tokenization",

    "Aadhaar": "Full Mask",

    "Credit Card": "Last 4 Digits Visible",

    "Not PII": "No Masking Required"

}

# ---------------------------------
# Generate Recommendation
# ---------------------------------

df["masking_policy"] = df["pii_type"].map(masking_policy)

df["masking_policy"] = df["masking_policy"].fillna(
    "Manual Review Required"
)

# ---------------------------------
# Risk Level
# ---------------------------------

def get_risk(pii):

    if pii in ["Aadhaar", "PAN", "Credit Card"]:

        return "HIGH"

    elif pii in ["Email", "Phone"]:

        return "MEDIUM"

    else:

        return "LOW"


df["risk_level"] = df["pii_type"].apply(get_risk)

# ---------------------------------
# Save Report
# ---------------------------------

# Save in reports folder
df.to_csv(OUTPUT_FILE, index=False)

# Save in Gold layer
gold_output = os.path.join(
    GOLD_DIR,
    "masking_recommendation.csv"
)

df.to_csv(gold_output, index=False)

print("\nMasking Recommendation Generated Successfully")

print(f"\nReport saved at: {OUTPUT_FILE}")

print(f"Gold layer file saved at: {gold_output}")

print("\nPreview:\n")

print(df.head())