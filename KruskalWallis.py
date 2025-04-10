from scipy import stats

# Sample data for three groups
group1 = [2, 5, 7, 1, 9]
group2 = [8, 3, 6, 4, 10]
group3 = [12, 15, 11, 13, 14]

# Perform the Kruskal-Wallis test
H_statistic, p_value = stats.kruskal(group1, group2, group3)

# Print the results
print("H statistic:", H_statistic)
print("P-value:", p_value)

# Check significance
alpha = 0.05
if p_value < alpha:
    print("The null hypothesis is rejected. There is a significant difference between the groups.")
else:
    print("The null hypothesis is not rejected. There is no significant difference between the groups.")
