library(tidyverse)
#Down loading the data
data("marketing", package = "datarium")
head(marketing)

#Fitting the model
model <- lm(sales ~ youtube + facebook + newspaper, data = marketing)
summary(model)

#Removing the insignificant variable and refitting the model
model  <- lm(sales ~ youtube + facebook, data = marketing)
summary(model)

#Use a residual plot to test the linearity and homoskedasticity (equal variance) assumptions.
plot(model, which=1)

#Use a normal probability plot to test the normality assumption.
plot(model, which=2)

#Testing the normality assumption using a histogram
hist(residuals(model))

#Use the variance inflated factor to test for multicollinearity. 
install.packages("usdm")
install.packages("car")
library(usdm)
library(car)
vif(model)
