import scipy.stats as stats
import scikit_posthocs as sp
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Uploading the data
crop_data = pd.read_excel(r"./crop_data.xltx")
print(crop_data[:10])
df = pd.DataFrame(crop_data)

# Fit the ANOVA model with blocking
model = sm.OLS('yield ~ C(fertilizer) + C(block)', data=df).fit()

# Perform the ANOVA test
#anova_table = sm.stats.anova_lm(model, typ=

# Print the ANOVA table
#print(anova_table)

