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
#residual plot
plot(model, which=1)
