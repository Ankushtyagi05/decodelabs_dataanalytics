import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv", sep="\t")

# Show first rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Dataset information
print("\nDATASET INFO:")
print(df.info())

# Statistics
print("\nSTATISTICS:")
print(df.describe())

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Plot Closing Price Trend
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"])

plt.title("Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Close Price")

plt.show()