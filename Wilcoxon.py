from scipy import stats

# Sample data (paired observations)
Y1 = [81,105.4,119.7,109.7,98.3,146.6,142,150.7,191.5,145.7,82.3,77.3,78.4,131.3,89.6,119.8,121.4,124,140.8,124.8,98.9,89,69.1,89.3,104.1,86.9,77.1,78.9,101.8,96]
Y2 = [80.7,82.3,80.4,87.2,84.2,100.4,115.5,112.2,147.7,108.1,103.1,105.1,116.5,139.9,129.6,98.9,61.9,96.2,125.5,75.7,66.4,49.9,96.7,61.9,80.3,67.7,66.7,67.4,91.8,94.1]

# Perform the Wilcoxon signed-rank test
statistic, p_value = stats.wilcoxon(Y1, Y2)

# Print the results
print("Wilcoxon signed-rank test:")
print("Statistic:", statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the two samples.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the two samples.")
