# 🛡️ Unity Catalog Permission Audit & Drift Detector MVP

## Enhanced with PII Auto-Classification & Masking Recommendation Engine

### Author

**Mohit Singh Kashyap**

---

# 📌 Project Overview

The **Unity Catalog Permission Audit & Drift Detector MVP** is an enterprise Data Governance and Compliance solution inspired by real-world Databricks governance use cases.

The project automatically audits permission snapshots, detects permission drift over time, classifies Personally Identifiable Information (PII), generates masking recommendations, and produces governance reports to improve data security and regulatory compliance.

This MVP demonstrates how organizations in **Government, BFSI, Healthcare, and Pharma** can strengthen data governance using a Medallion Architecture approach.

---

# 🎯 Business Problem

Large enterprises manage thousands of datasets and hundreds of users.

Over time:

* Users gain unnecessary permissions
* Sensitive data remains unidentified
* Compliance violations increase
* Manual audits become difficult

This project automates governance by identifying sensitive data, detecting permission changes, and generating audit reports.

---

# 🚀 Solution

The MVP provides:

* Synthetic enterprise data generation
* Data ingestion using Medallion Architecture
* Permission validation
* Permission drift detection
* PII auto-classification
* Masking recommendation generation
* Governance report generation
* Enterprise governance dashboard

---

# 🏗️ Architecture

```
Generate Sample Data
         │
         ▼
      Raw Layer
         │
         ▼
 Data Ingestion
         │
         ▼
    Bronze Layer
         │
         ▼
Permission Validation
         │
         ▼
    Silver Layer
         │
 ┌───────┴────────┐
 ▼                ▼
Permission      PII
Drift        Classification
Detection          │
     │             ▼
     │     Masking Recommendation
     └──────────┬───────────┘
                ▼
      Governance Reports
                │
                ▼
           Dashboard
```

---

# 📁 Project Structure

```
unity-catalog-permission-audit-mvp/

│

├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│

├── reports/

├── metadata/

├── src/
│   ├── utils/
│   ├── ingestion/
│   ├── validation/
│   ├── drift/
│   ├── pii/
│   ├── reporting/
│   └── dashboard/
│

├── config.py

├── main.py

├── requirements.txt

└── README.md
```

One more thing (highly recommended)

Since you now have src/main.py, make it an orchestrator that executes every module in sequence.

Then users can run the entire project with one command:

python -m src.main

while still having the flexibility to execute individual modules such as:

python -m src.validation.validate_permissions
python -m src.drift.detect_drift
python -m src.reporting.generate_audit_report

This dual approach is common in enterprise ETL pipelines: one orchestration entry point for end-to-end execution and 
separate module entry points for development, testing, and debugging. It will make your project look significantly more production-ready.

---
## 🚀 Running the Project

Run all commands from the project root directory.

### 1. Generate Sample Data

```bash
python -m src.utils.generate_sample_data
```

### 2. Ingest Data (Raw → Bronze)

```bash
python -m src.ingestion.ingest_data
```

### 3. Validate Permissions (Bronze → Silver)

```bash
python -m src.validation.validate_permissions
```

### 4. Detect Permission Drift

```bash
python -m src.drift.detect_drift
```

### 5. Generate Audit Report

```bash
python -m src.reporting.generate_audit_report
```

### 6. Classify PII

```bash
python -m src.pii.classify_pii
```

### 7. Generate Masking Recommendations

```bash
python -m src.pii.masking_recommendation
```

---

### Complete Pipeline Execution Order

```text
Generate Sample Data
        │
        ▼
Data Ingestion
        │
        ▼
Bronze Layer
        │
        ▼
Validation
        │
        ▼
Silver Layer
        │
        ▼
Permission Drift Detection
        │
        ▼
Audit Report Generation
        │
        ▼
PII Auto Classification
        │
        ▼
Masking Recommendation
        │
        ▼
Gold Layer Outputs
```


# ⚙️ Technology Stack

* Python
* Pandas
* PySpark
* Faker
* Streamlit
* Plotly

---

# ✨ Features

* Generate enterprise sample datasets
* Medallion Architecture implementation
* Permission validation engine
* Permission drift detection
* PII auto-classification
* Masking recommendation generation
* Governance reporting
* Interactive dashboard

---

# ▶️ How to Run

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Pipeline

```bash
python main.py
```

---

## Launch Dashboard

```bash
streamlit run src/dashboard/dashboard.py
```

---

# 📊 Generated Reports

The pipeline generates:

* pii_report.csv
* drift_report.csv
* masking_recommendation.csv
* audit_report.txt
* validation reports

---

# 🏛️ Enterprise Use Cases

* Government Agencies
* Banking & Financial Services
* Insurance
* Healthcare
* Pharmaceutical Companies
* Enterprise Data Platforms

---

# 🔮 Future Enhancements

* Unity Catalog API Integration
* Automatic Policy Enforcement
* Email Alerts
* Databricks Workflows
* Delta Live Tables Integration
* Role-Based Access Control Dashboard
* Real-Time Monitoring

---

# 📌 MVP Scope

This project is a **Minimum Viable Product (MVP)** designed to demonstrate enterprise governance concepts including permission auditing, permission drift detection, PII classification, masking recommendations, and governance reporting.

---

# 👨‍💻 Author

**Mohit Singh Kashyap**

Unity Catalog Permission Audit & Drift Detector MVP

Enterprise Data Governance & Compliance Project
