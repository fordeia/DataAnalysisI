import statsmodels.api as sm
import pandas as pd

# Sample data (replace with your actual data)
data = pd.read_excel(r"./marketingData.xlsx")
df = pd.DataFrame(data)
# Define the dependent and independent variables
Y = df['sales']
X = df[['youtube', 'facebook']]

# Add a constant to the independent variables (for the intercept)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(Y, X).fit()

# Print the model summary
print(model.summary())
