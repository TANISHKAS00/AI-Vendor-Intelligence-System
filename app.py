
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vendor Intelligence System")

st.title("AI Powered Vendor Intelligence System")

df = pd.read_csv("Vendor_Intelligence_Output.csv")

st.header("Dataset Overview")
st.write(df.shape)
st.dataframe(df.head())

st.header("Fraud Detection Summary")
st.write(df["FraudFlag"].value_counts())

fraud_cases = df[df["FraudFlag"] == -1]

st.header("Suspicious Invoices")
st.dataframe(fraud_cases.head(20))

top_vendors = (
    df.groupby("VendorName")["Dollars"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.header("Top Vendors")
st.bar_chart(top_vendors)

duplicates = df[
    df.duplicated(
        subset=["VendorNumber","PONumber","Dollars"],
        keep=False
    )
]

st.header("Duplicate Invoices")
st.dataframe(duplicates.head(20))
