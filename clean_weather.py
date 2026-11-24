# Task 7 - Data Cleaning and Transformation

import pandas as pd

# Load raw weather data
df = pd.read_csv("weather_raw.csv")

# Inspect data before cleaning
print(df.head())
df.info()
print(df.isnull().sum())
print(df.duplicated().sum())

# Remove missing values and duplicates
df = df.dropna()
df = df.drop_duplicates()

# Remove measurement units
df["Temperature"] = df["Temperature"].str.replace(" °F", "")
df["Wind Speed"] = df["Wind Speed"].str.replace(" mph", "")

# Convert strings to numeric values
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
df["Wind Speed"] = pd.to_numeric(df["Wind Speed"], errors="coerce")

# Remove malformed entries
df = df.dropna()

# Inspect data after cleaning
print("After cleaning:")
print(df.head())
df.info()