
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vendor Intelligence System")

st.title("AI Powered Vendor Intelligence System")

df = pd.read_csv("Vendor_Intelligence_Output.csv")

# Dataset Overview
st.header("Dataset Overview")
st.write(df.shape)
st.dataframe(df.head())

# Fraud Detection Summary
st.header("Fraud Detection Summary")
st.write(df["FraudFlag"].value_counts())

fraud_cases = df[df["FraudFlag"] == -1]

st.header("Suspicious Invoices")
st.dataframe(fraud_cases.head(20))

# Top Vendors
top_vendors = (
    df.groupby("VendorName")["Dollars"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.header("Top Vendors")
st.bar_chart(top_vendors)

# Duplicate Invoices
duplicates = df[
    df.duplicated(
        subset=["VendorNumber", "PONumber", "Dollars"],
        keep=False
    )
]

st.header("Duplicate Invoices")
st.dataframe(duplicates.head(20))

# Manual Fraud Prediction
st.header("Manual Fraud Prediction")

quantity = st.number_input("Quantity", min_value=0)
dollars = st.number_input("Dollars", min_value=0.0)
freight = st.number_input("Freight", min_value=0.0)
payment_delay = st.number_input("Payment Delay", min_value=0)
po_processing = st.number_input("PO Processing Time", min_value=0)
cost_per_unit = st.number_input("Cost Per Unit", min_value=0.0)

if st.button("Predict Fraud Risk"):

    if (
        dollars > 100000
        or freight > 1000
        or payment_delay > 45
        or cost_per_unit > 100
    ):
        st.error("⚠ High Risk / Suspicious Transaction")
    else:
        st.success("✅ Normal Transaction")
