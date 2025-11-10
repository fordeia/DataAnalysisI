import pandas as pd
from scipy import stats

# Sample data for three groups
ctr1 = [4.17, 5.58, 5.18, 6.11, 4.5, 4.61, 5.17, 4.53, 5.33, 5.14]
trt1 = [4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69]
trt2 = [6.31, 5.12, 5.54, 5.5, 5.37, 5.29, 4.92, 6.15, 5.8, 5.26]

# Create a DataFrame for easy summary
df = pd.DataFrame({
    'Control': ctr1,
    'Treatment 1': trt1,
    'Treatment 2': trt2
})

# Preview first few rows
print("Head of the data:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Perform the Kruskal-Wallis test
H_statistic, p_value = stats.kruskal(ctr1, trt1, trt2)

# Print the results
print("\nKruskal-Wallis Test Results:")
print("H statistic:", H_statistic)
print("P-value:", p_value)

# Check significance
alpha = 0.05
if p_value < alpha:
    print("The null hypothesis is rejected. There is a significant difference between the groups.")
else:
    print("The null hypothesis is not rejected. There is no significant difference between the groups.")
