#Two way ANOVA (with Interaction)
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

#Two way ANOVA (no interaction)
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Step 1: Set the file path
file_path = "C:/Users/fordeia/Desktop/cropData.txt"  # update as needed

# Step 2: Load the data
data = pd.read_csv(file_path, sep='\t')  # use sep=',' if comma-separated

# Step 3: Rename 'yield' column to avoid Python keyword issue
data = data.rename(columns={'yield': 'Yield'})

# Step 4: Fit the two-way ANOVA model without interaction
model = ols('Yield ~ C(fertilizer) + C(density)', data=data).fit()

# Step 5: Perform the ANOVA (each factor appears once)
anova_table = sm.stats.anova_lm(model, typ=2)
print("Two-Way ANOVA Table (No Interaction):\n")
print(anova_table)
