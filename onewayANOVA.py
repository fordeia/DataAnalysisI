import scipy.stats as stats
import scikit_posthocs as sp
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Uploading the data
crop_data = pd.read_excel(r"C:\Users\fordeia\DataAnalysisI\crop_data.xltx")
#print(crop_data[:10])
df = pd.DataFrame(crop_data)
print(df[:5])
# Fit the ANOVA model with blocking
model = ols('yield ~ C(fertilizer) + C(block)', data=df).fit()

# Perform the ANOVA test
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)

