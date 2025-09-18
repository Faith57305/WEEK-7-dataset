# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby("species")["sepal_length"].mean()
print("\nAverage Sepal Length per Species:")
print(grouped)

# Example pattern: which species has longest average petals?
petal_means = df.groupby("species")["petal_length"].mean()
print("\nAverage Petal Length per Species:")
print(petal_means)
