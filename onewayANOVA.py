import scipy.stats as stats
import scikit_posthocs as sp
import pandas as pd
#Uploading the data
crop_data = pd.read_excel(r"C:\Users\fordeia\DataAnalysisI\crop_data.xltx")
print(crop_data[:10])
df = pd.DataFrame(crop_data)

df.boxplot(column='yield', by='fertilizer')
plt.title('Side-by-side Boxplots')
plt.suptitle('')  # Suppress the default title
plt.show()

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(df['yield'][df['fertilizer'] == 1],
                                    df['yield'][df['fertilizer'] == 2],
                                    df['yield'][df['fertilizer'] == 3])

print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the group means.")

# Tukey's HSD test
tukey_result = sp.posthoc_tukey(df, val_col='yield', group_col='fertilizer')
print("Tukey's HSD test:\n", tukey_result)
