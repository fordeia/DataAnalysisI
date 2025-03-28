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
x = [28,29,35,37,32,26,37,39,22,29,36,38]

# Hypothesized population mean
population_mean = 28

# Perform the one-sample t-test
t_statistic, p_value = stats.ttest_1samp(x, population_mean)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

#Two sample t test
Men_bodyfat = [13.3,6,20,8,14,19,18,25,16,24,15,1,15]
Women_bodyfat = [22,16,21.7,21,30,12,23.2,28,23]

#Count, mean and standard deviation
#Men 
#length(Men_bodyfat) 
#mean(Men_bodyfat) 
#sd(Men_bodyfat) 
#Women
#length(Women_bodyfat) 
#mean(Women_bodyfat) 
#sd(Women_bodyfat) 

import statistics
#Men
mean_value_stats_men = statistics.mean(Men_bodyfat)
print(f"mean_men: {mean_value_stats_men}")

#Women
mean_value_stats_women = statistics.mean(Women_bodyfat)
print(f"mean_women: {mean_value_stats_women}")
