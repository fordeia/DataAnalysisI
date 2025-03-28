# Testing the normality assumption, Q-Q plot
import numpy as np 
import pylab 
import scipy.stats as stats
# read in the data
x = [28,29,35,37,32,26,37,39,22,29,36,38]  
stats.probplot(x, dist="norm", plot=pylab)
pylab.show()

#One sample t-test
# Sample data
sample = [28,29,35,37,32,26,37,39,22,29,36,38]

# Hypothesized population mean
population_mean = 28

# Perform the one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample, population_mean)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

#Two sample t test
Men_bodyfat = [13.3,6,20,8,14,19,18,25,16,24,15,1,15]
Women_bodyfat = [22,16,21.7,21,30,12,23.2,28,23]
