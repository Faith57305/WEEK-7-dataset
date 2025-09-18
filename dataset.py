import pandas as pd

# Load the Iris dataset (CSV format)
df = pd.read_csv("iris.csv")

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Check structure: datatypes and missing values
print("\nInfo about dataset:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# Clean dataset: (here Iris has no missing values, but let's handle if there were)
df = df.dropna()   # or df.fillna(value, inplace=True)
