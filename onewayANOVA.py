import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

# Step 1: Import the text file
file_path = r"C:\Users\fordeia\DataAnalysisI\cropData.txt"  # adjust path
data = pd.read_csv(file_path, sep='\t')  # use sep=',' if comma-separated

# Step 2: Rename 'yield' to avoid keyword conflict
data = data.rename(columns={'yield': 'Yield'})

# Step 3: Fit a one-way ANOVA model on fertilizer
model = ols('Yield ~ C(fertilizer)', data=data).fit()

# Step 4: Generate ANOVA table
anova_table = sm.stats.anova_lm(model, typ=2)
print("One-Way ANOVA on Fertilizer:\n")
print(anova_table)

# Step 5 (Optional): Tukey’s HSD post-hoc test if fertilizer is significant
tukey = pairwise_tukeyhsd(endog=data['Yield'],
                          groups=data['fertilizer'],
                          alpha=0.05)

print("\nTukey HSD Test for Fertilizer:\n")
print(tukey)

# Step 6 (Optional): Plot Tukey results
tukey.plot_simultaneous()
plt.title("Tukey HSD - Fertilizer")
plt.show()
