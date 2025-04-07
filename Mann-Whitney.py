from scipy.stats import mannwhitneyu

# Sample data for two groups
group1 = [540,670,1000,960,1200,4650,4200]
group2 = [5000,4200,1300,900,7400,4500,7500]

# Perform the Mann-Whitney U test
statistic, pvalue = mannwhitneyu(group1, group2)

# Print results
print("Mann-Whitney U statistic:", statistic)
print("P-value:", pvalue)

# Interpret the results
alpha = 0.05
if pvalue < alpha:
    print("Reject the null hypothesis: There is a significant difference between the two groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the two groups.")
