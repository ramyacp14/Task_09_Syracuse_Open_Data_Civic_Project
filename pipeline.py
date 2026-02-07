"""
Phase 3 Development Pipeline
Crime + Poverty + Rental Registry Analysis

Author: Ramya Chowdary
"""

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.neighbors import BallTree
import matplotlib.pyplot as plt
import openai
from datetime import datetime

# =========================
# CONFIG
# =========================

DATA_DIR = Path("Datasets")

RENTAL_FILE = DATA_DIR / "rental_registry.csv"
CRIME_FILE = DATA_DIR / "crime_2024.csv"
KINDER_FILE = DATA_DIR / "kinder_poverty.csv"

OUTPUT_FILE = "processed_analysis.csv"

openai.api_key = "YOUR_API_KEY"


# =========================
# DATA ACQUISITION
# =========================

def load_data():
    rental = pd.read_csv(RENTAL_FILE)
    crime = pd.read_csv(CRIME_FILE)
    kinder = pd.read_csv(KINDER_FILE)
    return rental, crime, kinder


# =========================
# CLEANING LAYER
# =========================

def clean_rental(df):

    df = df.copy()
    df["completion_date"] = pd.to_datetime(df["completion_date"], errors="coerce")
    df["zip"] = df["zip"].astype(str)
    df = df.dropna(subset=["ADDRESS", "zip"])

    return df


def clean_crime(df):

    df = df.copy()

    df["DATEEND"] = pd.to_datetime(df["DATEEND"], errors="coerce")

    df = df.dropna(subset=["LAT", "LONG"])

    df["LAT"] = df["LAT"].astype(float)
    df["LONG"] = df["LONG"].astype(float)

    return df


def clean_kinder(df):

    df = df.copy()

    df = df.dropna(subset=["Latitude", "Longitude", "Cnss_Tr"])

    df["Latitude"] = df["Latitude"].astype(float)
    df["Longitude"] = df["Longitude"].astype(float)

    return df


# =========================
# SPATIAL JOIN
# =========================

def attach_crime_to_tract(crime, kinder):

    crime_coords = np.radians(crime[["LAT", "LONG"]])
    tract_coords = np.radians(kinder[["Latitude", "Longitude"]])

    tree = BallTree(tract_coords, metric="haversine")

    dist, ind = tree.query(crime_coords, k=1)

    crime["Cnss_Tr"] = kinder.iloc[ind.flatten()]["Cnss_Tr"].values

    return crime


# =========================
# AGGREGATION
# =========================

def aggregate(crime, kinder):

    crime_summary = (
        crime.groupby("Cnss_Tr")
        .size()
        .reset_index(name="crime_count")
    )

    merged = kinder.merge(crime_summary, on="Cnss_Tr", how="left")
    merged["crime_count"] = merged["crime_count"].fillna(0)

    return merged


# =========================
# ANALYSIS
# =========================

def correlation_analysis(df):

    corr = df[["crime_count", "PvrtyPr"]].corr()
    print("\nCorrelation Matrix:\n", corr)
    return corr


# =========================
# VISUALIZATION
# =========================

def plot(df):

    plt.scatter(df["PvrtyPr"], df["crime_count"])
    plt.xlabel("Poverty Percentage")
    plt.ylabel("Crime Count")
    plt.title("Crime vs Poverty by Census Tract")
    plt.show()


# =========================
# LLM INTEGRATION
# =========================

PROMPT = """
You are a data scientist.

Analyze relationship between crime_count and PvrtyPr.

Rules:
- No causal claims
- Use uncertainty language
- Describe correlation only

DATA:
{data}
"""

def llm_summary(df):

    sample = df[["crime_count","PvrtyPr"]].describe().to_string()

    prompt = PROMPT.format(data=sample)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )

    text = response.choices[0].message.content

    # validation
    assert "cause" not in text.lower()

    print("\nLLM Summary:\n")
    print(text)

    return text


# =========================
# QUALITY ASSURANCE
# =========================

def run_tests(crime, merged):

    assert crime[["LAT","LONG"]].isnull().sum().sum() == 0
    assert (merged["crime_count"] >= 0).all()

    print("QA tests passed")


# =========================
# EDGE CASE
# =========================

def safe_lookup(df, tract):

    if tract not in df["Cnss_Tr"].values:
        return "Tract not found"

    return df[df["Cnss_Tr"] == tract]


# =========================
# MAIN PIPELINE
# =========================

def main():

    print("Loading data...")
    rental, crime, kinder = load_data()

    print("Cleaning...")
    rental = clean_rental(rental)
    crime = clean_crime(crime)
    kinder = clean_kinder(kinder)

    print("Spatial join...")
    crime = attach_crime_to_tract(crime, kinder)

    print("Aggregating...")
    merged = aggregate(crime, kinder)

    print("Analysis...")
    correlation_analysis(merged)

    print("Plotting...")
    plot(merged)

    print("Running QA...")
    run_tests(crime, merged)

    print("Saving output...")
    merged.to_csv(OUTPUT_FILE, index=False)

    print("LLM Summary...")
    llm_summary(merged)

    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
