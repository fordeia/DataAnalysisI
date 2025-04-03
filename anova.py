import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Sample data (replace with your actual data)
data = {'Treatment': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        'Block': ['1', '1', '1', '2', '2', '2', '3', '3', '3'],
        'Response': [10, 12, 15, 11, 13, 16, 12, 14, 17]}
df = pd.DataFrame(data)

# Fit the ANOVA model with blocking
model = ols('Response ~ C(Treatment) + C(Block)', data=df).fit()

# Perform the ANOVA test
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)

df.boxplot(column='yield', by='fertilizer')
plt.title('Side-by-side Boxplots')
plt.suptitle('')  # Suppress the default title
plt.show()

# Tukey's HSD test
tukey_result = sp.posthoc_tukey(df, val_col='yield', group_col='fertilizer')
print("Tukey's HSD test:\n", tukey_result)
