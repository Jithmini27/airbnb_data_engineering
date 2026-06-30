import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Airbnb Analytics Platform", layout="wide")

st.title("🏡 Airbnb Analytics Platform")
st.markdown("### Data Engineering & Business Insights Dashboard")

# ----------------------------
# DATA LOADING (ENGINEERING STYLE)
# ----------------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

# ----------------------------
# DATA CLEANING PIPELINE
# ----------------------------
def clean_data(df):
    df = df.copy()

    # Price cleaning
    if "price" in df.columns:
        df["price"] = (
            df["price"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Availability cleaning
    if "availability_365" in df.columns:
        df["availability_365"] = pd.to_numeric(df["availability_365"], errors="coerce")

    return df

# ----------------------------
# INSIGHT FUNCTIONS
# ----------------------------
def generate_insights(df):
    insights = []

    if "price" in df.columns:
        insights.append(f"💰 Average listing price is ${df['price'].mean():.2f}")
        insights.append(f"📊 Median price is ${df['price'].median():.2f}")

    if "neighbourhood" in df.columns:
        top_area = df["neighbourhood"].value_counts().idxmax()
        insights.append(f"📍 Most active area: {top_area}")

    if "availability_365" in df.columns:
        insights.append(f"📆 Avg availability: {df['availability_365'].mean():.1f} days")

    return insights

# ----------------------------
# LOAD + CLEAN
# ----------------------------
df = load_data("data/raw/listings.csv")
df = clean_data(df)

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("Filters")

if "neighbourhood" in df.columns:
    selected_area = st.sidebar.selectbox(
        "Select Neighbourhood",
        ["All"] + sorted(df["neighbourhood"].dropna().unique())
    )

    if selected_area != "All":
        df = df[df["neighbourhood"] == selected_area]

# ----------------------------
# KPI SECTION
# ----------------------------
st.subheader("📌 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Listings", len(df))

col2.metric(
    "Avg Price",
    f"${df['price'].mean():.2f}" if "price" in df else "N/A"
)

col3.metric(
    "Median Price",
    f"${df['price'].median():.2f}" if "price" in df else "N/A"
)

col4.metric(
    "Avg Availability",
    f"{df['availability_365'].mean():.1f}" if "availability_365" in df else "N/A"
)

st.divider()

# ----------------------------
# INSIGHTS SECTION
# ----------------------------
st.subheader("💡 Key Insights")

for i in generate_insights(df):
    st.write(i)

st.divider()

# ----------------------------
# PRICE DISTRIBUTION
# ----------------------------
st.subheader("📊 Price Distribution")

if "price" in df.columns:
    fig, ax = plt.subplots()
    ax.hist(df["price"].dropna(), bins=30)
    ax.set_title("Distribution of Airbnb Prices")
    ax.set_xlabel("Price")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# ----------------------------
# TOP NEIGHBOURHOODS
# ----------------------------
st.subheader("🏙️ Top Neighbourhoods")

if "neighbourhood" in df.columns:
    top = df["neighbourhood"].value_counts().head(10)

    fig, ax = plt.subplots()
    top.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Neighbourhoods")
    ax.set_ylabel("Listings")
    st.pyplot(fig)

# ----------------------------
# CORRELATION ANALYSIS (A+ FEATURE)
# ----------------------------
st.subheader("📈 Correlation Analysis")

numeric_df = df.select_dtypes(include=np.number)

if numeric_df.shape[1] > 1:
    corr = numeric_df.corr()

    fig, ax = plt.subplots()
    cax = ax.imshow(corr, cmap="coolwarm")
    ax.set_title("Feature Correlation Heatmap")
    plt.colorbar(cax)
    st.pyplot(fig)

# ----------------------------
# DATA PREVIEW
# ----------------------------
st.subheader("📄 Processed Dataset Preview")
st.dataframe(df.head(50))

# ----------------------------
# DOWNLOAD PROCESSED DATA
# ----------------------------
st.subheader("⬇️ Export Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Cleaned Dataset",
    data=csv,
    file_name="airbnb_processed_data.csv",
    mime="text/csv"
)

# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")
st.markdown("🚀 Built as Data Engineering Portfolio Project | Airbnb Analytics Pipeline")