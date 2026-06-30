import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Airbnb Dashboard", layout="wide")

st.title("🏡 Airbnb Data Engineering Dashboard")
st.markdown("### Data Exploration & Insights Platform")

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/listings.csv")
    return df

df = load_data()

# ----------------------------
# DATA CLEANING
# ----------------------------

# Clean price column safely
if "price" in df.columns:
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Clean availability if exists
if "availability_365" in df.columns:
    df["availability_365"] = pd.to_numeric(df["availability_365"], errors="coerce")

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("Filters")

if "neighbourhood" in df.columns:
    neighbourhood = st.sidebar.selectbox(
        "Select Neighbourhood",
        ["All"] + sorted(df["neighbourhood"].dropna().unique().tolist())
    )
    if neighbourhood != "All":
        df = df[df["neighbourhood"] == neighbourhood]

# ----------------------------
# KPI SECTION
# ----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Listings", len(df))

col2.metric(
    "Average Price",
    f"${df['price'].mean():.2f}" if "price" in df.columns else "N/A"
)

col3.metric(
    "Average Availability",
    f"{df['availability_365'].mean():.1f}" if "availability_365" in df.columns else "N/A"
)

st.divider()

# ----------------------------
# CHARTS
# ----------------------------
st.subheader("📊 Price Distribution")

if "price" in df.columns:
    st.bar_chart(df["price"].dropna().head(1000))

# ----------------------------
# DATA PREVIEW
# ----------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(df.head(50))