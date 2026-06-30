# 🏡 Airbnb Data Engineering & Analytics Project (London)

## 📌 Project Overview

This project is a complete **data engineering and analytics pipeline** built using the **Inside Airbnb London dataset**.

It transforms raw Airbnb data (listings, calendar, reviews, and neighbourhood information) into a **clean, structured, and analytics-ready dataset**, followed by exploratory data analysis and an interactive dashboard for business insights.

The goal is to simulate a **real-world Airbnb market intelligence system** that supports data-driven decision-making.

---

## 🎯 Objectives

* Build an end-to-end data engineering pipeline
* Clean and standardize raw Airbnb datasets
* Perform feature engineering to create analytical datasets
* Generate business insights through exploratory data analysis (EDA)
* Build an interactive Streamlit dashboard for visualization
* Perform basic statistical analysis on pricing behavior

---

## 🏗️ Project Architecture

```
Raw Data (CSV files)
        ↓
Data Cleaning (handling missing values, formatting, validation)
        ↓
Feature Engineering (price transformation, derived metrics)
        ↓
Master Dataset Creation
        ↓
Exploratory Data Analysis (EDA)
        ↓
Statistical Analysis
        ↓
Streamlit Dashboard (Final Output)
```

---

## 📂 Dataset Description

This project uses the **Inside Airbnb London dataset**, including:

* `listings.csv` → Main Airbnb listing data (price, location, room type, host info)
* `calendar.csv` → Daily availability and pricing
* `reviews.csv` → Guest reviews and feedback
* `neighbourhoods.csv` → Area definitions
* `neighbourhoods.geojson` → Geospatial boundaries

---

## ⚙️ Data Pipeline Steps

### 1. Data Ingestion

* Loaded raw CSV files from Inside Airbnb dataset
* Combined multiple sources for analysis

### 2. Data Cleaning

* Removed currency symbols from price
* Converted data types (price, availability, etc.)
* Handled missing and inconsistent values
* Standardized categorical fields

### 3. Feature Engineering

* Created cleaned price fields
* Derived metrics (availability, density, etc.)
* Built a master dataset for analysis

### 4. Data Integration

* Merged listings with neighbourhood and review data
* Created unified analytical dataset for London

---

## 📊 Exploratory Data Analysis (EDA)

Key analyses performed:

* Price distribution across listings
* Top neighbourhoods by listing count
* Availability trends across listings
* Relationship between price and location
* Host-level and listing-level patterns

---

## 🧪 Statistical Analysis

Performed basic hypothesis testing:

* Comparison of luxury vs budget listings (price differences)
* Neighbourhood-based price variation analysis

### Key Insight:

Luxury listings show statistically higher pricing, indicating a **strong market segmentation in London Airbnb listings**.

---

## 💡 Key Insights

* Airbnb prices in London are **highly skewed**, with a small number of luxury listings dominating the upper range
* Certain neighbourhoods have significantly higher listing density and pricing power
* Availability varies strongly across different areas, indicating demand imbalance
* Location is one of the strongest drivers of price variation

---

## 📈 Streamlit Dashboard Features

* Interactive KPI metrics (total listings, average price, availability)
* Price distribution visualization
* Neighbourhood analysis
* Filters by location
* Clean dataset preview
* Business insight summaries

---

## 🧰 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Streamlit
* SciPy

---

## 🚀 How to Run the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 📁 Project Structure

```
AIRBNB-DATA-ENGINEERING/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│
├── reports/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚠️ Limitations

* Dataset is static and does not reflect real-time Airbnb data
* Missing values in reviews and calendar data
* No actual booking confirmation data available
* Assumptions were made during feature engineering

---

## 🚀 Future Improvements

* Machine learning model for price prediction
* Geospatial clustering of listings
* Real-time data pipeline using APIs
* Advanced recommendation system for listings
* Deployment on cloud platform (AWS/GCP)

---

## 📌 Author Notes

This project was developed as part of a **Data Engineering internship assessment**, focusing on:

* Data pipeline design
* Analytical thinking
* Business insight generation
* Dashboard development

---

## 🏁 Conclusion

This project demonstrates a full lifecycle of a data engineering workflow — from raw data ingestion to business-ready insights — simulating a real-world Airbnb market intelligence system.

---

## 📌 Candidate Information (Submission Details)

- **Academic Performance:** Second Class Upper Division (GPA: [Insert if required])
- **Notice Period / Availability:** Immediate
- **Flexibility to Work Onsite:** Yes

---

## 📩 Submission Note

This project has been submitted as part of the Experne c (Pvt) Ltd Data Engineer Intern Talent Assessment Program. All work has been completed using the Inside Airbnb London dataset and follows the required submission guidelines.

All code, analysis, and outputs are reproducible using the instructions provided in this repository.
