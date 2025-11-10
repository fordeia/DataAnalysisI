import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from itertools import combinations

# Sample data for three groups
ctr1 = [4.17, 5.58, 5.18, 6.11, 4.5, 4.61, 5.17, 4.53, 5.33, 5.14]
trt1 = [4.81, 4.17, 4.41, 3.59, 5.87, 3.83, 6.03, 4.89, 4.32, 4.69]
trt2 = [6.31, 5.12, 5.54, 5.5, 5.37, 5.29, 4.92, 6.15, 5.8, 5.26]

# Create a DataFrame for easier handling
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

# ==============================
# Comparative Box Plots
# ==============================
plt.figure(figsize=(8, 6))
sns.boxplot(data=df)
plt.title('Comparative Box Plot of Groups')
plt.ylabel('Values')
plt.show()

# ==============================
# Mean Plot with Error Bars
# ==============================
means = df.mean()
stds = df.std()
n = len(df)

# Calculate standard error
sem = stds / np.sqrt(n)

plt.figure(figsize=(8, 6))
plt.errorbar(means.index, means.values, yerr=sem.values, fmt='o', capsize=5, linestyle='None', markersize=8)
plt.title('Mean Plot with Error Bars (SEM)')
plt.ylabel('Mean Values')
plt.show()

# ==============================
# Kruskal-Wallis Test
# ==============================
H_statistic, p_value = stats.kruskal(ctr1, trt1, trt2)

print("\nKruskal-Wallis Test Results:")
print("H statistic:", H_statistic)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("The null hypothesis is rejected. There is a significant difference between the groups.")
else:
    print("The null hypothesis is not rejected. There is no significant difference between the groups.")

# ==============================
# Pairwise Comparisons (Wilcoxon rank-sum / Mann-Whitney U)
# ==============================
print("\nPairwise comparisons (Wilcoxon rank-sum test with continuity correction):")
groups = df.columns
for g1, g2 in combinations(groups, 2):
    stat, p = stats.ranksums(df[g1], df[g2])  # Wilcoxon rank-sum test
    print(f"{g1} vs {g2}: statistic={stat:.4f}, p-value={p:.4f}")
