#Question 1 =========================================
#Q-Q Plot
import pylab
import scipy.stats as stats

measurements = [data1, data2, ...]
stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()

#One Sample t-test
# Hypothesized population mean
pop_mean = 3

# Perform the one-sample t-test
t_statistic, p_value = stats.ttest_1samp(measurements, pop_mean, alternative='greater')

# Adjust p-value for one-tailed test
p_value_one_tail = p_value


print("T-statistic:", t_statistic)
print("P-value:", p_value)

#Check for significance
alpha = 0.05
if p_value < alpha:
  print("Reject null hypothesis")
else:
  print("Fail to reject null hypothesis")

#Question 2 ==============================================
#Contingency table example
import numpy as np
from scipy.stats import chi2_contingency

# Observed data in a contingency table
observed_values = np.array([[50, 75],
                           [125,175],[90,30],[45,10]])

# Chi-square test for independence example 
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


