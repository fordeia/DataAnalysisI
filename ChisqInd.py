import numpy as np
from scipy.stats import chi2_contingency

# Observed data in a contingency table
observed_values = np.array([[50, 75],
                           [125,175],[90,30],[45,10]])

# Chi-square test
chi2, p_value, degrees_of_freedom, expected_values = chi2_contingency(observed_values)

print("Chi-square statistic:", chi2)
print("P-value:", p_value)
print("Degrees of freedom:", degrees_of_freedom)
print("Expected values:\n", expected_values)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant association between the variables.")
else:
    print("Fail to reject the null hypothesis: There is no significant association between the variables.")
