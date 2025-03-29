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

# Create the boxplot
plt.boxplot([Men_bodyfat, Women_bodyfat], tick_labels=['Men bodyfat', 'Women bodyfat'])

# Add title and labels
plt.title('Side-by-Side Boxplot')
plt.ylabel('Values')

# Show the plot
plt.show()

# Shapiro-Wilk normality test for Men's body fat
from scipy.stats import shapiro
data = Men_bodyfat
statistic, p_value = shapiro(data)
print("Shapiro-Wilk Statistic:", statistic)
print("P-value:", p_value)

# Shapiro-Wilk normality test for Women's body fat
data = Women_bodyfat
statistic, p_value = shapiro(data)
print("Shapiro-Wilk Statistic:", statistic)
print("P-value:", p_value)

#Equal variance test
# Calculate F-statistic and p-value
x=Men_bodyfat
y=Women_bodyfat
f_stat = np.var(x, ddof=1) / np.var(y, ddof=1)
df1 = len(x) - 1
df2 = len(y) - 1
p_value = 1 - stats.f.cdf(f_stat, df1, df2)
print("F-statistic:",f_stat)
print("P-value:", p_value)

#Two sample t-test
t_statistic, p_value = stats.ttest_ind(Men_bodyfat, Women_bodyfat, equal_var=True)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

#Loading heart data
import pandas as pd
heart_data = pd.read_excel(r"C:\Users\fordeia\DataAnalysisI\heart_data.xlsx")
print(heart_data[:6])

#Multiple linearn regression 
import statsmodels.api as sm
import pandas as pd
df = pd.DataFrame(heart_data)
# Define the dependent and independent variables
Y = df['heart.disease']
X = df[['biking', 'smoking']]

# Add a constant to the independent variables (for the intercept)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(Y, X).fit()

# Print the model summary
print(model.summary())

#Use a residual plot to test the linearity and homoskedasticity (equal variance) assumptions.
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Calculate the residuals
residuals = model.resid

# Create the residual plot
plt.scatter(model.fittedvalues, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

# Create a histogram
plt.hist(residuals, bins=10, edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')
plt.show()

#Shapiro-Wilk test for normality of residuals
statistic, p_value = shapiro(residuals)
print("Shapiro-Wilk Statistic:", statistic)
print("P-value:", p_value)

#Use the variance inflated factor to test for multicollinearity. 
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(df, features):
   
    vif_data = pd.DataFrame()
    vif_data["Feature"] = features
    vif_data["VIF"] = [variance_inflation_factor(df[features].values, i)
                          for i in range(len(features))]
    return vif_data

# Example usage:

df = heart_data

features_to_check = ['biking', 'smoking']
vif_result = calculate_vif(df, features_to_check)
print(vif_result)




