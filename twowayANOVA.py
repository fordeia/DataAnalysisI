import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# File path
file_path = "C:/Users/fordeia/Desktop/cropData.txt"

# Load data
data = pd.read_csv(file_path, sep='\t')
data = data.rename(columns={'yield': 'Yield'})  # Avoid Python keyword

# Fit two-way ANOVA with interaction (no blocking)
model = ols('Yield ~ C(fertilizer) * C(density)', data=data).fit()

# Perform two-way ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)  # Type II ANOVA
print(anova_table)
