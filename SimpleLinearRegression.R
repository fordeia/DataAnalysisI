# Create the data frame
data <- data.frame(
  Years_Exp = c(1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7),
  Salary = c(39343.00, 46205.00, 37731.00, 43525.00,
             39891.00, 56642.00, 60150.00, 54445.00, 64445.00, 57189.00)
)

# Fitting Simple Linear Regression to the Training set
lm.r= lm(formula = Salary ~ Years_Exp,
         data = data)
#Summary of the model
summary(lm.r)

#Testing the assumptions of the model

# Create the scatter plot to test the linearity assumption
plot(data$Years_Exp, data$Salary,
     xlab = "Years Experienced",
     ylab = "Salary",
     main = "Scatter Plot of Years Experienced vs Salary")

#Testing the normality assumption of the residuals using a Q-Q plot and the Shapiro Wilk test
qqnorm(residuals(lm.r))
qqline(residuals(lm.r), col = "steelblue", lwd = 2)

#Testing the normality assumption of the residuals using the Shapiro-Wilk test
shapiro.test(residuals(lm.r))

#Making predictions
predictions <- predict(lm.r, newdata = data$Years_Exp)
predictions

