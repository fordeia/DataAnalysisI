import scipy.stats as stats
import pandas as pd
#Uploading the data
crop_data = pd.read_excel(r"C:\Users\fordeia\DataAnalysisI\crop_data.xltx")
print(crop_data)
df = pd.DataFrame(crop_data)

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(df['yield'][df['fertilizer'] == '1'],
                                    df['yield'][df['fertilizer'] == '2'],
                                    df['yield'][df['fertilizer'] == '3'])

print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the group means.")
