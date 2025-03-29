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
import statistics
#Men
count_men = len(Men_bodyfat)
print(f"count_men: {count_men}")
mean_value_stats_men = statistics.mean(Men_bodyfat)
print(f"mean_men: {mean_value_stats_men}")
std_dev_sample_men = statistics.stdev(Men_bodyfat)
print(f"Sample standard deviation: {std_dev_sample_men}")

#Women
mean_value_stats_women = statistics.mean(Women_bodyfat)
print(f"mean_women: {mean_value_stats_women}")
std_dev_sample_women = statistics.stdev(Women_bodyfat)
print(f"Sample standard deviation_women: {std_dev_sample_women}")
count_women = len(Women_bodyfat)
print(f"count_women: {count_women}")

#Creating a side-by-side boxplot
import matplotlib.pyplot as plt
import numpy as np

# Create the boxplot
plt.boxplot([Men_bodyfat, Women_bodyfat], labels=['Men bodyfat', 'Women bodyfat'])

# Add title and labels
plt.title('Side-by-Side Boxplot')
plt.ylabel('Values')

# Show the plot
plt.show()
