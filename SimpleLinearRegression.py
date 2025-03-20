#Simple linear regression in Python
# x is work experience and y is salary
import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7]).reshape((-1, 1))
y = np.array([39343.00, 46205.00, 37731.00, 43525.00, 39891.00, 56642.00, 60150.00, 54445.00, 64445.00, 57189.00])

#Fitting the model
model = LinearRegression().fit(x, y)

#Obtaining R square
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

#Obtaining the intercept
print(f"intercept: {model.intercept_}")

#Obtaining the slope
print(f"slope: {model.coef_}")
