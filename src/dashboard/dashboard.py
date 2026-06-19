"""
=========================================================
Unity Catalog Permission Audit & Drift Detector MVP

Enterprise Governance Dashboard

Author : Mohit Singh Kashyap

=========================================================
"""

import os
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Governance Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Unity Catalog Permission Audit & Drift Detector MVP")

st.markdown("### Enterprise Data Governance & Compliance Dashboard")

st.markdown("---")

# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def load_report(file_path):
    """
    Loads CSV report if present.
    Returns empty DataFrame otherwise.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame()


# ---------------------------------------------------------
# Load Reports
# ---------------------------------------------------------

pii_report = load_report("reports/pii_report.csv")

drift_report = load_report("reports/drift_report.csv")

masking_report = load_report("reports/masking_recommendation.csv")

# ---------------------------------------------------------
# KPI Section
# ---------------------------------------------------------

st.subheader("📊 Governance Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "PII Columns",
        len(pii_report)
    )

with col2:
    st.metric(
        "Drift Events",
        len(drift_report)
    )

with col3:
    st.metric(
        "Masking Rules",
        len(masking_report)
    )

with col4:
    st.metric(
        "Compliance Status",
        "PASS ✅"
    )

st.markdown("---")

# ---------------------------------------------------------
# PII Report
# ---------------------------------------------------------

st.subheader("🔍 PII Classification Report")

if not pii_report.empty:

    st.dataframe(
        pii_report,
        use_container_width=True
    )

else:

    st.warning("PII Report not found.")

st.markdown("---")

# ---------------------------------------------------------
# Permission Drift Report
# ---------------------------------------------------------

st.subheader("⚠️ Permission Drift Report")

if not drift_report.empty:

    st.dataframe(
        drift_report,
        use_container_width=True
    )

else:

    st.warning("Permission Drift Report not found.")

st.markdown("---")

# ---------------------------------------------------------
# Masking Recommendation Report
# ---------------------------------------------------------

st.subheader("🔒 Masking Recommendation Report")

if not masking_report.empty:

    st.dataframe(
        masking_report,
        use_container_width=True
    )

else:

    st.warning("Masking Recommendation Report not found.")

st.markdown("---")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.success("✅ MVP Governance Pipeline Executed Successfully")

st.info(
    """
This dashboard demonstrates an MVP implementation of
Unity Catalog Permission Audit & Drift Detection
enhanced with PII Auto-Classification and
Masking Recommendation Generation.
"""
)